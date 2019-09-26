# secure-file-storage

Example
``` python
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
```

Output

```
----- input -----

{'boolean1': True,
 'boolean2': False,
 'float': 12345.6789,
 'int': 1234567890,
 'list': ['ไทย', 'English', '日本語'],
 'tuple': (12345, 6.789, True, False)}

----- output -----

{'boolean1': True,
 'boolean2': False,
 'float': 12345.6789,
 'int': 1234567890,
 'list': ['ไทย', 'English', '日本語'],
 'tuple': [12345, 6.789, True, False]}
```
