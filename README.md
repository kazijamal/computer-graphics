# graphics-work

## Monday 02/03/20

### Line Algorithm

The coordinate grid in graphics has octants instead of quadrants

| octant | properties | potential pixels   |
| ------ | ---------- | ------------------ |
| I      | 0 < m < 1  | right or top-right |

input = 2 endpoints

#### Outline
```
for x in x0 -> x1:
  TEST (x+1, y)
  TEST (x+1, y+1)
  PLOT BEST RESULT
```

- slope-intercept form: y = mx + b
- standard form: Ax + By + C = 0
- A = change in y, B = negative change in x, C = change in x times b

## Thursday 01/30/20

### PPM (Portable PixMap)
- Uncompressed raster format
- NetPBM is a family of related formats
- Pixel data is represented by RGB triplets in either ASCII or binary
- All whitespace is equivalent

### ImageMagick
- Can use display command to open image file formats
- Can use convert command all image file formats

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