### Bytearray

The function **bytearray** is a built-in and **bytearray** is a type.  A bytearray has a representation that looks like binary data, but it is really [int].

[docs](https://docs.python.org/3.1/library/functions.html#bytearray)

The init function can take a string, an int or an iterable.  

Here we feed it a list of ints:  0..255.

```python
>>> ba = bytearray([0,255])
>>> type(ba)
<type 'bytearray'>
>>> ba
bytearray(b'\x00\xff')`
>>>
```

At this point, it might seem as if bytearray is a special kind of string.  It is not.  It is a 

> The bytearray class is a mutable sequence of integers in the range 0 <= x < 256

with a special representation.

```python
>>> list(ba)
[0, 255]
>>> [n + 1 for n in ba]
[1, 256]
>>> for c in ba:  print c   // an int!
... 
0
255
>>>
```

Here we make a new bytearray by passing a single integer (for the size of a zeroed array).  

We also can use a string.  For a string, the encoding must then be specified:

```python
>>> bytearray(6)
bytearray(b'\x00\x00\x00\x00\x00\x00')
>>> bytearray('00ff', encoding='hex')
bytearray(b'00ff')
>>> 
```

Binary digits can give *surprising* results with **bytearray**

```python
>>> b = bin(255)
>>> b
'0b11111111'
>>> type(b)
<type 'str'>
>>> ba = bytearray(b)
>>> ba
bytearray(b'0b11111111')
>>> 
>>>
>>> for c in ba:  print c
... 
48
98
49
49
49
49
49
49
49
49
>>>
```

What?  How did ``b'11111111`` turn into

```
[48, 98, 49, 49, 49, 49, 49, 49, 49, 49]
```
I simply note that the docs do not list binary numbers as acceptable input.  

> If it is an iterable, it must be an iterable of integers in the range 0 <= x < 256, which are used as the initial contents of the array

