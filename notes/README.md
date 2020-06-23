# graphics-work

## Thursday 03/12/20

### Torus
- given information
	- center
	- radius of cross section (r)
	- distance from torus center to cross-section center (R)
- defining points
	- points on the surface
- torus = circle + translation x + rotation y
- torus = circle + translation y + rotation x
- x = cosΦ(rcosθ + R) + Cx
- y = rsinθ + Cy
- z = -sinΦ(rcosθ R) + Cz

---

## Wednesday 03/11/20

### 3D Shapes
- Box (Rectangular Prism)
- Sphere
- Torus

### Box
- given information
	- vertex (front-top-left)
	- width (x), height (y), depth (z)
- defining points
	- 8 verticies

### Sphere
- given information
	- center
	- radius
- defining points
	- points on the surface
- x = rcosθ + Cx
- y = rsinθcosΦ + Cy
- z = rsinθsinΦ + Cz
- θ: circle creation: 0 - 2π
- Φ: rotation: 0 - π
```
for rot: 0 - 1
	for circ: 0 - 1
		x = rcos(π * circ) + Cx
		y = rsin(π * circ)cos(2π * rot) + Cy
		z = rsin(π * circ)sin(2π * rot) + Cz
```

---

## Thursday 03/05/20

### Cubic
- Rt = ((1-t)^3)P0 + (3t(1-t)^3)P1 + (3(t^2)(1-t))P2 + (t^3)P3

### Hermite Curves
- defined by:
	- 2 endpoints: (P0, P1)
	- rates of change at each endpoint: (R0, R!)
- f(t) = at^3 + bt^2 + ct + d
	- points on the curve
- f'(t) = 3at^2 + 2bt + c
	- rates of change
- f(0) = d = P0
- f'(0) = c = R0
- f(1) = a + b + c + d = P1
- f'(1) = 3a + 2b + c = R1

---

## Tuesday 03/03/20

### Splines
- Curves (cubic) that can be connected to appear smooth/continous

### Bezier Curves
- defined by 4 control points
- P0 and P3: endpoints
- P1 and P2: influence points

### Line
![bezier line](https://upload.wikimedia.org/wikipedia/commons/0/00/B%C3%A9zier_1_big.gif)
- Pt = (1-t)P0 + t(P1)

### Quadratic
![quadratic bezier curve](https://upload.wikimedia.org/wikipedia/commons/3/3d/B%C3%A9zier_2_big.gif)
- Qt = (1-t)Q0 + t(Q1)
- Qt = ((1-t)^2)P0 + 2t(1-t)P1 + (t^2)P2

---

## Monday 03/02/20

### Parametric Equations
- Define curves as systems of equations in terms of a signel independent variable

- Non Parametric
	- y = f(x)
- Parametric
	- y = f(t)
	- x = g(t)

### Parametric Line
(x0, y0) -> (x1, y1)
x = x0 + (x1 - x0)t
y = y0 + (y1 - y0)t

### Circle
x = rcosθ + Cx => x = rcos(2πt) + Cx
y = rsinθ + Cy => y = rsin(2πt) + Cy

---

## Tuesday 02/25/20

### Rotate about x-axis
- (x, y, z) --- R x-axis, θ ---> (x, ycosθ - zsinθ, ysinθ + zcosθ)
- multiply by the following matrix:

| 1 0 0 0 |

| 0 cosθ -sinθ 0 |

| 0 sinθ cosθ 0 |

| 0 0 0 1 |

### Rotate about y-axis
- (x, y, z) --- R y-axis, θ ---> (xcosθ + zsinθ, y, -xsinθ + zcosθ)
- multiply by the following matrix:

| cosθ 0 sinθ 0 |

| 0 1 0 0 |

| -sinθ 0 cosθ 0 |

| 0 0 0 1 |

### Combining Transformations
E0: Edge Matrix, T: Translate Matrix, R: Rotate Matrix, S: Scale Matrix
- T * E0 = E1 (Translated)
- R * E1 = E2 (Translated, Rotated)
- S * E2 = E3 (Translated, Rotated, Scaled)
- E3 = S * R * T * E0

---

## Monday 02/24/20

### Transformations
- scaling (dilation)
- translating
- rotating
- will be done via matrix multiplication

### Scale
- (x, y, z) --- S a, b, c ---> (ax, by, cz)
- multiply by the following matrix:

| a 0 0 0 |

| 0 b 0 0 |

| 0 0 c 0 | 

| 0 0 0 1 | 

### Translate
- (x, y, z) --- T a, b, c ---> (x+a, y+b, z+c)
- multiply by the following matrix:

| 1 0 0 a |

| 0 1 0 b |

| 0 0 1 c |

| 0 0 0 1 |

### Rotate about z-axis
- (x, y, z) --- R z-axis, θ ---> (xcosθ - ysinθ, xsinθ + ycosθ, z)
- multiply by the following matrix:

| cosθ -sinθ 0 0 |

| sinθ cosθ 0 0 |

| 0 0 1 0 |

| 0 0 0 1 |

---

## Wednesday 02/12/20

### Matrix Multiplication
- row r and column c of the product matrix is dot product of row r of matrix 1 and column c of matrix 2
- all our multiplication will be 4x4 (square matrices) times 4xN (edge matrices)

---

## Tuesday 02/11/20

### Matrices in Graphics
- our images will be stored as a list/matrix of edges (edge matrices)
- each 2 entries will represent a line
- [ P0, P1, P2, P3, P4, P5 ... Pn ]
- each point is an (x,y) or (x,y,z) set of coordinates

| x0 x1 ... xn |

| y0 y1 ... yn |

| z0 z1 ... zn |

  P0 P1 ... Pn

### Matrix Math
- matrix multiplication
  - M0 * M1 != M1 * M0 (not commutative)
  - number of columns in first matrix must equal number of rows in second matrix
  - dimensions of product: rows of first matrix and columns of second matrix
  - multiply edge matrices with 3x3 matrices to have a product that is 3xN
    - the first matrix should be the 3x3 matrix, and the second matrix should be the 3xN matrix
- multiplicative identity
  - I * M0 = M0
  - I is a square with diagonal 1s

| 1 0 0 |

| 0 1 0 |

| 0 0 1 |

---

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

---

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

---

## Thursday 01/30/20

### PPM (Portable PixMap)
- Uncompressed raster format
- NetPBM is a family of related formats
- Pixel data is represented by RGB triplets in either ASCII or binary
- All whitespace is equivalent

### ImageMagick
- Can use display command to open image file formats
- Can use convert command all image file formats

---

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