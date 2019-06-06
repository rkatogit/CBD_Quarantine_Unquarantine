# CBD_Quarantine_Unquarantine
[CB Defense] Quarantine/Unquarantine via script   
python 2.x

## Usage
fill your credential into arguments of "__init__".   
ex.
```
def __init__(self, user='hoge@fuga.com', passwd='password'):
```

then

```
python quarantine.py <device id> <on/off>

#quarantine
python quarantine.py 12345 on

#unquarantine
python quarantine.py 12345 off
```


