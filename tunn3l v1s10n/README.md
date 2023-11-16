AS mentionned in https://en.wikipedia.org/wiki/BMP_file_format
The first 2 bytes of the BMP file format are the character "B" then the character "M" in ASCII encoding that make us knowing the type of the file or with exiftool
So the bmp file contain three main components : 
The header of bmp image is composed by to party :
  - Bitmap file header : containing 14 bytes where the last 4 bytes indicate the begining of the pixel array data 
  - DIB header (bitmap information header) :  This block of bytes tells the application detailed information about the image which has a size of 40 byte as windows created image
The data in the form of array pixel
Analyse :
As mentionned in image 1 the first 10 byte are coorect but the 4 last byte with offset 0A are givening false information about The offset, i.e. starting address, of the byte where the bitmap image data (pixel array) can be found. 
