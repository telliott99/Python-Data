### Binary data to ints

Reading from binary data, use **ord**

```python
>>> s = '\x00\xff'
>>> [ord(c) for c in s]
[0, 255]
>>>
```

Perhaps more elegantly, use **map** and **ord**:

```python
>>> s = '\x00\xff'
>>> map(ord, s)
[0, 255]
>>>

```

### Ints to binary data

Use **bytearray**.  ([More](ByteArray.md) about bytearray).

```python
>>> import utils as ut
>>> b = bytearray([0,255])
>>> b
bytearray(b'\x00\xff')
>>> ut.write('out.bin',b)
>>> ut.read('out.bin', mode='rb')
'\x00\xff'
>>>
```

Or you could use [struct](files/Struct.md)

[docs](https://docs.python.org/2/library/struct.html#format-characters) on struct.
