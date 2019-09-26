from cryptography.fernet import Fernet
import json

class SecureFileStorage:

    def __init__(self, key_path=None):
        self.fernet = None
        self.storage = None

        if key_path is not None:
            self.load_key(key_path)

    def gen_key(self, key_path):
        key = Fernet.generate_key()
        with open(key_path, 'wb') as f:
            f.write(key)

    def load_key(self, key_path):
        with open(key_path, 'rb') as f:
            self.fernet = Fernet(f.read())

    def save(self, data, json_path):
        json_str = json.dumps(data)
        json_ba = json_str.encode()
        encrypted = self.fernet.encrypt(json_ba)
        with open(json_path, 'wb') as f:
            f.write(encrypted)

    def load(self, json_path):
        with open(json_path, 'rb') as f:
            encrypted = f.read()
        json_ba = self.fernet.decrypt(encrypted)
        json_str = json_ba.decode('utf-8')
        return json.loads(json_str)

if __name__ == '__main__':

    from pprint import pprint as pp

    key_path = './secret.key'
    out_path = './out'

    # input
    in_obj = {
        'boolean1': True,
        'boolean2': False,
        'int': 1234567890,
        'float': 12345.6789,
        'list': [
            'ไทย',
            'English',
            '日本語',
        ],
        'tuple': (
            12345,
            6.789,
            True,
            False,
        ),
    }
    print('\n----- input -----\n')
    pp(in_obj)

    # gen key -- first time only
    #sfs = SecureFileStorage()
    #sfs.gen_key(key_path)

    sfs = SecureFileStorage(key_path)

    # save data
    sfs.save(in_obj, out_path)

    # load data
    out_obj = sfs.load(out_path)

    # print output
    print('\n----- output -----\n')
    pp(out_obj)
