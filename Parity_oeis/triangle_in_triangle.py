from supporting.A338031_list import *
import svg
import random
import math
from supporting.get_oeis import *

class ParityTriangleDrawer():
  def __init__(self, sequence_data, rows=None):
    self.sequence_data = sequence_data
    n = len(sequence_data)
    if rows is None:
      self.rows = int(((1+8*n)**0.5-1)/2) # A003056: inverse of triangular numbers
    else:
      self.rows = min(rows, int(((1+8*n)**0.5-1)/2))

  def hexagons(self, x, y, width, show_boundary=True):
    column_count = self.rows
    radius = width/(column_count+1)/2
    radius0 = radius*2/math.sqrt(3)
    h = math.sqrt(3)/2*width
    s = 0.9 # scale
    (xc,yc) = (x + width/2, y + h*2/3) # triangle center
    (x1,y1) = (x+width/2,y)
    (x2,y2) = (x,y+width*math.sqrt(3)/2)
    (x3,y3) = (x+width,y+width*math.sqrt(3)/2)
    (x4,y4) = (x,y+width*math.sqrt(3)/2+width/3)
    (x5,y5) = (x+width,y+width*math.sqrt(3)/2+width/3)
    def inter(z1, z2): return (1+s)/2*z1 + (1-s)/2*z2
    if show_boundary:
      elements = [
        svg.Path(
          stroke="red",
          stroke_width=2,
          fill="none",
          d=[
            svg.M(inter(x4,x5),inter(y4,y5)),
            svg.L(inter(x5,x4),inter(y5,y4)),
            svg.Q(x1=x5, y1=y5, x=inter(x5,x3), y=inter(y5,y3-width)),
            svg.L(inter(x3,x5),inter(y3,y5)),
            svg.Q(x1=x3, y1=y3, x=inter(x3,x1), y=inter(y3,y1)),
            svg.L(inter(x1,x3),inter(y1,y3)),
            svg.Q(x1=x1, y1=y1, x=inter(x1,x2), y=inter(y1,y2)),
            svg.L(inter(x2,x1),inter(y2,y1)),
            svg.Q(x1=x2, y1=y2, x=inter(x2,x4), y=inter(y2,y4)),
            svg.L(inter(x4,x2),inter(y4,y2-width)),
            svg.Q(x1=x4, y1=y4, x=inter(x4,x5), y=inter(y4,y5)),
            svg.Z()
          ]
        )
      ]
    else:
      elements = []
    for i in range(column_count):
      for j in range(i+1):
        r = column_count - j - 1
        c = i - j
        is_even = self.sequence_data[r*(r+1)//2 + c] % 2 == 0
        x0 = (x + radius*(2*i+2 - j))*s + (1-s)*xc
        y0 = (y + h - radius0*(3*j+2)/2)*s + (1-s)*yc
        if is_even:
          elements += [
            ParityTriangleDrawer.polygon_element(s*radius0*1/2, x0, y0),
            ParityTriangleDrawer.polygon_element(s*radius0*2/2, x0, y0),
            # ParityTriangleDrawer.polygon_element(s*radius0*3/3, x0, y0)
          ]
        else:
          elements += [
            ParityTriangleDrawer.polygon_element(s*radius0, x0, y0)
          ]
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

elements = []

sequences = sorted([
  (303513, 16),
  (73266, 16),
  (132393, 16),
  (26807, 16),
  (298187, 16),
  (222946, 16),
  (65600, 16),
  (326410, 16)
])

HEIGHT = 816
a_numbers = []
for index, (a_num, rows) in enumerate(sequences):
  seq = OEISBFile(a_num)
  row_index = index//4
  column_index = index % 4
  del_x = 260*column_index
  del_y = 350*row_index
  elements.append(ParityTriangleDrawer(seq.lookup_sequence(),rows).hexagons(x=18+del_x, y=50+del_y, width=240, show_boundary=True))
  elements.append(svg.Text(x=18+120+del_x, y=50 + 240*math.sqrt(3)/2 + 240/6 + del_y, font_size=56, text=seq.a_number_string, font_family="SquareFont", dominant_baseline="middle", text_anchor="middle"))
  a_numbers.append(seq.a_number_string)

canvas = svg.SVG(
  width=1056,
  height=HEIGHT,
  style="fill:none;stroke:#000000;",
  elements=elements
)

file_name = "_".join(a_numbers)
with open("/Users/peter/Programming/MathArt/AxiDrawV3/G4G/assets/" + file_name + ".svg", "w") as f:
  f.write(canvas.as_str())

# svg.Circle(
      #   stroke_dasharray=1,
      #   stroke="red",
      #   fill="none",
      #   cx=x,
      #   cy=y,
      #   r=5
      # ),
      # svg.Rect(
      #   stroke_dasharray=1,
      #   stroke="green",
      #   fill="none",
      #   x=x,
      #   y=y,
      #   width=width,
      #   height=width*math.sqrt(3)/2
      # ),
      # svg.Rect(
      #   stroke_dasharray=1,
      #   stroke="magenta",
      #   fill="none",
      #   x=x,
      #   y=y+width*math.sqrt(3)/2,
      #   width=width,
      #   height=width/3
      # ),
      # svg.Polygon(
      #   stroke_dasharray=1,
      #   stroke="blue",
      #   fill="none",
      #   points=[(x3,y3),(x2,y2),(x1,y1)]
      # ),
