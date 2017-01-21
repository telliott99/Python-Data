## Binary representation

Not to be confused with binary data.

### Int - > Binary - > Int

```python
>>> b = bin(17)
>>> b
'0b10001'
>>> bin(33)
'0b100001'
>>> int(b, 2)
17
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

todo:
'{:b}'.format(257)