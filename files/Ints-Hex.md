## Ints and hex

### From Int To Hex

The best way to do this is to use a format string:

```python
>>> '{:x}'.format(255)
'ff'
>>> '{:x}'.format(257)
'101'
>>>
```

**hex** will also do it.

```python
>>> hex(65)
'0x41'
>>> hex(3)
'0x3'
>>>
```
But you see the problems (added prefix and truncation).  We can deal with this manually, like:

```python
>>> L = [hex(n)[2:] for n in [1,255,37]]
>>> L = ['0' + c if len(c) == 1 else c for c in L]
>>> L
['01', 'ff', '25']
>>>
```

or, better

```python
>>> b = bin(65)
>>> b = '0b' + b[2:].zfill(8)
>>> b
'0b01000001'
>>>
```

But it's best to just use the format string.

### From Hex to Int

The best way goes through binary data as an intermediate

```python
>>> data = bytearray.fromhex('00ff')
>>> [int(b) for b in data]
[0, 255]
>>>
```

We can use the venerable **int** function on a single hex byte or multiple bytes

```python
>>> int('0f', 16)
15
>>> int('49276d', 16)
4794221
>>> int('\x04', 16)     # error
```

Probably, though, you wanted a list of ints.  I think the best way is

```python
>>> h = "49276d"
>>> h.decode('hex')
"I'm"
>>> [ord(c) for c in h.decode('hex')]
[73, 39, 109]
>>>
```

Here is yet another way:

add to **utils.py**

```python
def chunks(s, n=2):
    rL = list()
    while s:
        rL.append(s[:2])
        s = s[2:]
    return rL
```

Then

```
>>> import utils as ut
>>> [int(d,16) for d in ut.chunks("49276d")]
[73, 39, 109]
>>>
```



