## Binary data and hex

### Int - > Hex

```python
>>> hex(255)
'0xff'
>>> hex(65537)
'0x10001'
>>>
```

### [Int] -> Binary Data - > Hex

```python
>>> import binascii
>>> b = bytearray([0,255])
>>>
>>> binascii.hexlify(b)
'00ff'
>>>
```


### Hex - > Binary Data - > [Int]

```python
>>> data = bytearray.fromhex('00ff')
>>> [int(b) for b in data]
[0, 255]
>>>
```

or

```python
>>> import binascii
>>> u = binascii.unhexlify
>>> 
>>> data = u('00ff')
>>> >>> data
'\x00\xff'
>>> [ord(c) for c in data]
[0, 255]
>>> 
```