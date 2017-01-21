## Working with data

The Crypto Pals guys give great advice, you should do all calculations with bytes as integers 0..255.

To the extent we can, we will stick with that.

### Python reads binary data

I'm still running Python 2.7, so this write-up is specific for old style Python, which is much different than Python 3.X.

Python 2 writes data to and reads it from disk as strings composed of "binary data".  So what is:

* [binary data](files/BinaryData.md)

* a [bytearray](files/ByteArray.md)

### Read and write Binary Data

These functions read binary data from and write it to disk.

* I/O with [binary data](files/Binary-IO.md)

### Conversions

* [Convert Ints to and from binary data](files/Binary-Ints.md).

* [Ints to and from hex](files/Ints-Hex.md) 

* Binary data [directly to hex](files/Binary-Hex.md)

* Zeros and Ones:  [binary-encoded data](files/Binary-rep.md)

### Useful modules

* [Struct](files/Struct.md)

* [binascii](files/BinAscii.md)

