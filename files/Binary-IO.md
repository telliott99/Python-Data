### Binary Data < - > disk

If we weren't using Python, we could just use bash to write:

```bash
> printf '\x00\xff' > out.bin
> 
```

### We will use two utility functions to wrap boilerplate:

**utils.py**

```python
def readData(fn, mode = 'r'):
    FH = open(fn, mode)
    data = FH.read()
    FH.close()
    return data

def writeData(fn, data, mode = 'w'):
    FH = open(fn, mode)
    FH.write(data)
    FH.close()
```

#### Write data

```python
>>> import utils as ut
>>> s = '\x00\xff'
>>> ut.writeData('out.bin', s, 'wb')
>>>
```

Check it in Terminal:

```bash
> hexdump out.bin
0000000 00 ff                                          
0000002
>
```

#### Read data

```python
>>> ut.readData('out.bin','rb')
'\x00\xff'
>>>
```

What follows is not really important for the topic.

It surprises me that the default mode works here.  The ``'rb'`` is unnecessary.  

According to the [docs](https://docs.python.org/2/library/functions.html#open)

> If mode is omitted, it defaults to 'r'. The default is to use text mode, which may convert '\n' characters to a platform-specific representation on writing and back on reading. Thus, when opening a binary file, you should append 'b' to the mode value to open the file in binary mode, which will improve portability. (Appending 'b' is useful even on systems that don’t treat binary and text files differently, where it serves as documentation.)

So, for example:

```python
>>> ut.writeData('out.bin','\x00\xff\n','wb')
>>> ut.readData('out.bin')
'\x00\xff\n'
>>> ut.writeData('out.bin','\x00\xff\n','w')
>>> ut.readData('out.bin')
'\x00\xff\n'
>>>
```

No difference.