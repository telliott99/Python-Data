### Binary data to ints

Going from binary data to ints, new style:  use a **bytearray**

```python
>>> ba = bytearray('\x00\xff')
>>> list(ba)
[0, 255]
>>>
```

Or, simply use **ord**

```python
>>> [ord(c) for c in '\x00\xff']
[0, 255]
>>>
```

Perhaps more elegantly, use **map** and **ord**:

```python
>>> map(ord, '\x00\xff')
[0, 255]
>>>

```

### Ints to binary data

Old style:  use **chr**.

```
>>> ''.join([chr(c) for c in [0,255]])
'\x00\xff'
>>>
```


Or use **bytearray**.  ([More](ByteArray.md) about bytearray).

```python
>>> import utils as ut
>>> b = bytearray([0,255])
>>> b
bytearray(b'\x00\xff')
>>> ut.write('out.bin', mode = 'b')
>>> ut.read('out.bin', mode='rb')
'\x00\xff'
>>>
```

You could use [struct](Struct.md)

```But that's pretty excessives
>>> import struct
>>> data = [0, 255]
>>> struct.pack('B B', *data)
'\x00\xff'
>>>
```

But that really does seem excessive.

[docs](https://docs.python.org/2/library/struct.html#format-characters) on struct.
