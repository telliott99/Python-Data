**utils.py**

```python
def read(fn, mode = 'r'):
    FH = open(fn, mode)
    data = FH.read()
    FH.close()
    return data

def write(fn, data, mode = 'w'):
    FH = open(fn, mode)
    FH.write(data)
    FH.close()
```
