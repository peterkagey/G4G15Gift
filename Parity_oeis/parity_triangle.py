from supporting.A338031_list import *
import svg
import math

def list_to_triangle(list_of_points):
  i = 1
  triangle = []
  while len(list_of_points) >= i:
    row = []
    for _ in range(i):
      row.append(list_of_points.pop(0))
    triangle.append(row)
  return triangle

triangle_of_points = list(map(lambda i: A338031[i*(i+1)//2:(i+1)*(i+2)//2], range(50)))
LAYERS = 3
box_size = 10
WIDTH = len(triangle_of_points) * box_size + 4
HEIGHT = WIDTH

def polygon_points(n, r, center, rotate_degrees):
  (x_c,y_c) = center
  points = []
  for i in range(n):
    x = x_c + r*math.cos(2*math.pi * (i/n + rotate_degrees/360))
    y = y_c + r*math.sin(2*math.pi * (i/n + rotate_degrees/360))
    points += [x, y]
  return points

def svg_hexagons(x, y, fill=False):
  hexagons = []
  if fill:
    concentric_count = LAYERS
  else:
    concentric_count = 1
  for i in range(0,concentric_count):
    r = box_size/math.sqrt(3) * (1 - 2*i/(2*LAYERS - 1))
    hexagons.append(
      svg.Polygon(
        stroke="#000000",
        stroke_width=0.3,
        fill="none",
        points=polygon_points(6, r, (x,y), 30)
      )
    )
  return hexagons


elements = []
print(len(triangle_of_points))
for n in range(len(triangle_of_points)):
  for k in range(n+1):
    x = WIDTH/2 + box_size * (k - n/2)
    y = box_size * (n + 1) * math.sqrt(3)/2
    elements += svg_hexagons(x, y, fill = triangle_of_points[n][k] % 2 == 0)

elements.append(svg.Text(x=0, y=HEIGHT-25, font_size=50, text="A338031", font_family="square deal"))
elements.append(svg.Text(x=0, y=HEIGHT+5, font_size=20, text="Parity Triangles from the OEIS", font_family="Menlo"))
elements.append(svg.Text(x=0, y=HEIGHT+35, font_size=20, text="Peter Kagey", font_family="square deal"))

canvas = svg.SVG(
  width=WIDTH,
  height=HEIGHT + 200,
  elements=elements
)

file_name = "_".join(["parity", "triangle"])
with open("/Users/peter/Programming/MathArt/AxiDrawV3/G4G/assets/" + file_name + ".svg", "w") as f:
  f.write(canvas.as_str())
