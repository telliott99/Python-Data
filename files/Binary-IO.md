### Binary Data to and from disk

#### Write

```python
>>> import utils as ut
>>> s = '\x00\xff'
>>> type(s)
<type 'str'>
>>> ut.write('out.bin', s, 'wb')
>>>
```

Check it directly:

```bash
> hexdump out.bin
0000000 00 ff                                          
0000002
>
```

If we weren't using Python, we could just use bash to write:

```bash
> printf '\x00\xff' > out.bin
> 
```

#### Read

```python
>>> ut.read('out.bin','rb')
'\x00\xff'
>>>
```

