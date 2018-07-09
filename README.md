# Questions

## What's `stdint.h`?
Sources: https://en.wikibooks.org/wiki/C_Programming/stdint.h

header file library

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

To specify the signing of integers(postive or negative or both) and the byte sizes they take

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE: 1 byte unsigned integer
DWORD: 4 bytes unsigned integer
LONG: 4 bytes signed integer
WORD: 2 bytes unsigned integer

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

0x42 0x4D in hexadecimal, same as BM in ASCII

## What's the difference between `bfSize` and `biSize`?

bfSize is the size in bytes of the bitmap file whereas bisize is the number of bytes required by a structure

## What does it mean if `biHeight` is negative?

It means a top-down DIB

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount provides the number of bits per pixel and the max number of colours in the bitmap

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

Either could not open infile or could not create outfile . NULL here means the pointer does not refer to a valid object.

## Why is the third argument to `fread` always `1` in our code?

Because we are only reading or writng 1 byte at a time
fread's general syntax is as follows: fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

= (4-(3*3)%4)%4 = 3%4 = 3

## What does `fseek` do?
http://www.cplusplus.com/reference/cstdio/fseek/

skip over padding if any

## What is `SEEK_CUR`?

Current position of the file pointer
