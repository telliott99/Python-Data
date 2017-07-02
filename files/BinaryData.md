### Binary Data

In Python 2.X, binary data can be stored in a string with a special format, for example: ``'\xff'``.

These are called [string literals](https://docs.python.org/2.7/reference/lexical_analysis.html#string-literals).

The backslash "escapes" the ``x`` and signifies that the two characters following are hex.  Another example is of course the Unix newline ``'\n'`` or tab ``'\t'``.

```python
>>> s = '\xff'
>>> len(s)
1
>>> type(s)
<type 'str'>
>>>
```

There must be at least two valid hex characters ``[0..9][a..f]`` following ``'\x'``:

```python
>>> '\xf'
ValueError: invalid \x escape
>>>
```

A string can mix ``\x`` characters with regular characters.

```python
>>> s = '\xffae'
>>> len(s)
3
>>> s = '\xff\xae'
>>> len(s)
2
>>>
```

In fact, the ASCII characters "a" and "e" can be thought of as data (equivalent to 97 and 101), and they, along with ``\xff``,  can be converted to ints:

```
python >>> s = '\xffae'
>>> [ord(c) for c in s]
[255, 97, 101]
>>>
```

Look closely:

```
>>>  s = '\xff\xae'
>>> [ord(c) for c in s]
[255, 174]
>>>
```

Such string literals can be concatenated, sliced or repeated justlike any other string.

```python
>>> s = '\x00\xff'
>>> s += '\xae'
>>> s
'\x00\xff\xae'
>>>
>>> c = '\xff'
>>> c*3
'\xff\xff\xff'
>>>
```
Here is anothe example of binary data in Python:  a digest of the string ``'hello'``

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

In displaying binary data, if a printable character is available, Python will use it.  Otherwise it prints ``\x`` plus the hex representation.  

In the above string, there are eight printable characters, each of one byte ``(]A@*K*vq)``, plus another eight explicit bytes.

#### PKCSF#7

For PKCSF#7 padding the pad character depends on the length.

I solved this with a lookup dictionary

```python
D = {0:  '\x00', 1:  '\x01', 2:  '\x02', 3:  '\x03', 
     4:  '\x04', 5:  '\x05', 6:  '\x06', 7:  '\x07', 
     8:  '\x08', 9:  '\x09', 10: '\x0a', 11: '\x0b', 
     12: '\x0c', 13: '\x0d', 14: '\x0e', 15: '\x0f' }
```

In the interpreter:

```python
>>> D = {0:  '\x00', 1:  '\x01', 2:  '\x02', 3:  '\x03', 
...      4:  '\x04', 5:  '\x05', 6:  '\x06', 7:  '\x07', 
...      8:  '\x08', 9:  '\x09', 10: '\x0a', 11: '\x0b', 
...      12: '\x0c', 13: '\x0d', 14: '\x0e', 15: '\x0f' }
>>> 
>>> D[4]*4
'\x04\x04\x04\x04'
>>>
```
