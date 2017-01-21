## Working with data

The Crypto Pals guys give great advice, you should do all calculations with bytes as integers 0..255.

To the extent we can, we will stick with that.

### Python reads binary data

However, Python 2 actually writes data to and reads it from disk as "binary data".

So what is that:

* [binary data](files/BinaryData.md)

* [bytearray](files/ByteArray.md)

### Utilities

First, to read and write data from disk we use some 

* [Utility functions](files/Utilities.md)

These functions read binary data from and write it to disk.

### Read and write Binary Data

* I/O with [binary data](files/Binary-IO.md)

### Conversions

* [Convert Ints to and from binary data](files/Binary-Ints.md).

* [Ints to and from hex](files/Ints-Hex.md) 

* Binary data [directly to hex](files/Binary-Hex.md)

* Zeros and Ones:  [binary-encoded data](files/Binary-rep.md)

### Useful modules

* [Struct](files/Struct.md)

* [binascii](files/BinAscii.md)

