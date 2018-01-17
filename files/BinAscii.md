Python module:  **binascii**

[docs](https://docs.python.org/2/library/binascii.html)

The module has two principal functions

* hexlify

```python
>>> import binascii
>>> h = binascii.hexlify
>>> 
>>> h('\x00\xff')
'00ff'
>>>
>>> h('abc')
'616263'
>>>
```

Given a string with hex formatted bytes, it generates the equivalent hex-encoded string.  Notice that we get the correct padding.

* unhexlify

```
python >>> u = binascii.unhexlify
>>> u('616263')
'abc'
>>> u('00ff')
'\x00\xff'
>>>
```