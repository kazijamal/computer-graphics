# graphics-work

## Tuesday 02/11/20

### Matrices in Graphics
- our images will be stored as a list/matrix of edges
- each 2 entries will represent a line
- [ P0, P1, P2, P3, P4, P5 ... Pn ]
- each point is an (x,y) or (x,y,z) set of coordinates

| x0 x1 ... xn |

| y0 y1 ... yn |

| z0 z1 ... zn |

  P0 P1 ... Pn

### Matrix Math
- matrix multiplication
  - M0 * M1 != M1 * M0
  - number of columns in first matrix but equal number of rows in second matrix
  - dimensions of product: rows of first matrix and columns of second matrix
  - multiply edge matrices with 3x3 matrices to have a product that is 3xN
    - the first matrix should be the 3x3 matrix, and the second matrix should be the 3xN matrix
- multiplicative identity
  - I * M0 = M0
  - I is a square with diagonal 1s

| 1 0 0 |

| 0 1 0 |

| 0 0 1 |

----------------------------------------------------------------------

## Tuesday 02/04/20

### Line Algorithm Continued
```
f(x,y) = Ax + By + C
IF f(x,y) = 0
  THEN (x,y) IS ON THE LINE

x = 0, y = y0
FOR X: x0 -> x1
  v0 = f(x+1,y+1)
  v1 = f(x+1,y)
  IF (abs(v0) < abs(v1))
    PLOT (x+1,y+1)
  ELSE
    PLOT (x+1,y)
```

#### Optimize Using Midpoint
- 2 options: (x+1,y) or (x+1,y+1)
- midpoint: (x+1, y+1/2)
  - if midpoint is 0, pick either option
  - if midpoint > 0 -> midpoint is below the line -> pick top pixel (x+1,y+1)
  - if midpoint < 0 -> midpoint is above the line -> pick bottom pixel (x+1,y)
```
x = x0, y = y0
FOR X: x0 -> x1
  d = f(x+1,y+1/2)
  IF (d > 0)
    y += 1
  x += 1
  PLOT (x, y)
```

#### Optimize f(x,y)
- f(x0,y0) = 0
- f(x0+1, y0+1/2) = A(x0+1) + B(y0+1/2) + C 
  - = Ax0 + A + By0 + 1/2B + C
  - = Ax0 + By0 + C + A + 1/2B 
  - = A + 1/2B

----------------------------------------------------------------------

## Monday 02/03/20

### Line Algorithm

The coordinate grid in graphics has octants instead of quadrants

| octant | properties | potential pixels   |
| ------ | ---------- | ------------------ |
| I      | 0 < m < 1  | right or top-right |

input = 2 endpoints

#### Outline
```
FOR X: x0 -> x1
  TEST (x+1,y)
  TEST (x+1,y+1)
  PLOT BEST RESULT
```

- slope-intercept form: y = mx + b
- standard form: Ax + By + C = 0
- A = change in y, B = negative change in x, C = change in x times b

----------------------------------------------------------------------

## Thursday 01/30/20

### PPM (Portable PixMap)
- Uncompressed raster format
- NetPBM is a family of related formats
- Pixel data is represented by RGB triplets in either ASCII or binary
- All whitespace is equivalent

### ImageMagick
- Can use display command to open image file formats
- Can use convert command all image file formats

----------------------------------------------------------------------

## Wednesday 01/29/20

### Color Depth
The amount of data used to represent a single pixel

| size   | color options                           |
| ------ | --------------------------------------- |
| 1 bit  | 1 color, on/off                         |
| 2 bit  | 1 color with intensity                  |
| 3 bit  | red, green, blue, on/off                |
| 4 bit  | RGB with intensity                      |
| 6 bit  | RGB, each color has its own intensity   |
| 3 byte | RGB, each with 256 possible intensities |

### Other Color Spaces
- RGBA : Red, Green, Blue + Alpha (transparency)
- HSB : Hue, Saturation, Brightness

### Image File Formats
- Raster vs. Vector
  - vector formats represent images as a series of drawing instructions
    - infinitely scalable
    - SVG (Scalable Vector Graphics)
  - raster formats represent images as a grid of pixels
- Uncompressed vs. Compressed (Raster)
  - uncompressed formats contain data for each pixel
    - BMP, TIFF, RAW
  - compressed formats use a compression algorithm to minimize file size
    - Lossless vs. Lossy
      - lossless compression algorithms contain enough information to exactly recreate the original image
      	- run length encoding (turns a row that is RRRRRRGGBBB into 6R2G3B)
      	- PNG (Portable Network Graphics), GIF (Graphics Interchange Format)
      - lossy compression algorithms do not retain all the details of the original image
      	- JPEG (Joint Photographic Experts Group)