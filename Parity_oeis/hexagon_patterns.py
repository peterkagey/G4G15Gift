from supporting.A338031_list import *
import svg
import math

# At one point, based on triangle_in_triangle code.

class ParityTriangleDrawer():
  def __init__(self, sequence_data, rows):
    self.sequence_data = sequence_data
    self.rows = rows

  def triangle_elements(self, x, y, width, rows):
    r = width/(rows+1)/2
    r0 = r*2/math.sqrt(3)
    h = math.sqrt(3)/2*width
    elements = []#[svg.Polygon(fill="none",points=[(x,y+width*math.sqrt(3)/2),(x+width,y+width*math.sqrt(3)/2),(x+width/2,y)])]
    for i in range(rows):
      for j in range(i+1):
        x0 = x + r*(2*i+2 - j)
        y0 = y + h - r0*(3*j+2)/2
        elements.append(
          ParityTriangleDrawer.polygon_element(r0, x0, y0)
        )
    return elements

  @classmethod
  def polygon_points(cls, n, r, center, rotate_degrees):
    (x_c,y_c) = center
    points = []
    for i in range(n):
      x = x_c + r*math.cos(2*math.pi * (i/n + rotate_degrees/360))
      y = y_c + r*math.sin(2*math.pi * (i/n + rotate_degrees/360))
      points += [x, y]
    return points

  @classmethod
  def polygon_element(cls, r, x, y):
    return svg.Polygon(
        points=ParityTriangleDrawer.polygon_points(6, r, (x,y), 30)
      )

elements = [svg.Rect(x=0, y=0, width=1000, height=1000, fill="none", stroke="red")]
for i in range(2,8):
  elements += ParityTriangleDrawer(0,0).triangle_elements(x=50, y=100, width=300, rows=round((i*(i-1))/2))
# print(len(triangle_of_points))
# for n in range(len(triangle_of_points)):
#   for k in range(n+1):
#     x = WIDTH/2 + box_size * (k - n/2)
#     y = box_size * (n + 1) * math.sqrt(3)/2
#     elements += svg_hexagons(x, y, fill = triangle_of_points[n][k] % 2 == 0)

# elements.append(svg.Text(x=0, y=HEIGHT-25, font_size=50, text="A338031", font_family="square deal"))
# elements.append(svg.Text(x=0, y=HEIGHT+5, font_size=20, text="Parity Triangles from the OEIS", font_family="Menlo"))
# elements.append(svg.Text(x=0, y=HEIGHT+35, font_size=20, text="Peter Kagey", font_family="square deal"))

canvas = svg.SVG(
  width=1000,
  height=1000,
  style="fill:none;stroke:#000000;",
  elements=elements
)

file_name = "_".join(["hexagon", "patterns"])
with open("/Users/peter/Programming/MathArt/AxiDrawV3/G4G/assets/" + file_name + ".svg", "w") as f:
  f.write(canvas.as_str())
