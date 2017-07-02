## Binary data

The Crypto Pals guys give great advice, do calculations with bytes as integers 0..255.

So we will convert to and from hex, binary and so on only for display or input.

* Convert [Int to Hex](#int-to-hex)

* Convert [Hex to Int](#hex-to-int)

* Write [Hex to disk](#hex-to-disk)

* Read [Disk to ints](#disk-to-ints)


## Hex

<a name="int-to-hex"></a>

### Ints to hex

```python
>>> hex(65)
'0x41'
>>> hex(65537)
'0x10001'     # 16**4 + 1
>>> L = [hex(n)[2:] for n in [1,255,37]]
>>> >>> L
['1', 'ff', '25']
```

```python
>>> L = [hex(n)[2:] for n in [1,255,37]]
>>> L = ['0' + c if len(c) == 1 else c for c in L]
>>> L
['01', 'ff', '25']
>>> ''.join(L)
'01ff25'
>>>
```

So that makes it complicated.  Do you want the leading '0x', and how do you pad out to 2 characters for very low bytes?

<a name="hex-to-int"></a>

### Hex to Int

```python
>>> int('0f', 16)
15
>>> int('49276d', 16)
4794221 
>>>  int('\x04', 16)    # ValueErrror: invalid literal
```
which can work as input for something like XOR.

### Hex to ints

For a multi-byte hex string, you can generate an integer as in the above example.

Or you can get chunks first.  For example

```python
def chunks(s, n=2):
    rL = list()
    while s:
        rL.append(s[:2])
        s = s[2:]
    return rL

print [int(d, 16) for d in chunks("49276d")] 
//   [73, 39, 109]
```

Or you can do:

```
>>> h = '49276d'
>>> h.decode('hex')
"I'm"
>>> [ord(c) for c in h.decode('hex')]
[73, 39, 109]
>>>
```

<a name="hex-to-disk"></a>

### Hex to disk as ints

```python
h = '49276d'
FH = open('out.bin','wb')
FH.write(h.decode("hex"))
FH.close()
```

```
> hexdump -C out.bin
00000000  49 27 6d                                          |I'm|
00000003
> 
```

<a name="disk-to-ints"></a>

### From disk to ints

```python
>>> FH = open('out.bin','rb')
>>> data = FH.read()
>>> FH.close()
>>> 
>>> data
"I'm"
>>> [ord(c) for c in data]
[73, 39, 109]
>>>
```

## Binary representation

```bash
>>> bin(17)
'0b10001'
>>> bin(33)
'0b100001'
>>>
```

Note the same issue with padding that we had with hex.

#### fancy formatting

``` python
>>> b = bin(65)
>>> b
'0b1000001'
>>> b = '0b' + b[2:].zfill(8)
>>> b
'0b01000001'
```

Two other ways use fancy formatting

```python
>>> b = bin(65)
>>> '{:08b}'.format(65)
'01000001'
>>> format(65, '#010b')
'0b01000001'
>>> 
```

## Binary data

```python
>>> data = bytearray.fromhex('00ff')
>>> [int(b) for b in data]
[0, 255]
>>>
```

```python
>>> import hashlib
>>> m = hashlib.md5()
>>> m.update('hello')
>>> d = m.digest()
>>> len(d)
16
>>> type(d)
<type 'str'>
>>> d
']A@*\xbcK*v\xb9q\x9d\x91\x10\x17\xc5\x92'
>>>
```

If a printable character is available, Python will print that.  Otherwise it prints ``\x`` plus the hex representation.  In the above string, there are eight printable characters, each one byte (]A@*K*vq), plus another eight explicit bytes.

If you want the hexadecimal representation for all 16 of them, you could use ``ord`` to convert each value to an integer:

```python
>>> L = [ord(y) for y in d]
>>> L[:4]
[93, 65, 64, 42]
>>>`
```

```python
>>> c = chr(146)
>>> c
'\x92'
>>>
```


