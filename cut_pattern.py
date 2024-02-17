import svg
import math

# 100 units is 1.39 inches

def upright_triangle(x_shift, y_shift):
  return [
    svg.M(x=x_shift + 0,   y=y_shift + 0),
    svg.L(x=x_shift + 100, y=y_shift + math.sqrt(3)*100),
    svg.L(x=x_shift + 200, y=y_shift + 0),
    svg.Z()
  ] + [
    svg.M(x=x_shift + 50,   y=y_shift + 300),
    svg.Arc(rx=25, ry=25, x = 25, y = math.sqrt(3)*25 + 300, angle = 60, large_arc = True, sweep = True)
  ]

# def parametetric_chain(f, t1, t2, steps=100):
#   (x1, y1) = f(t1)
#   pts = [svg.M(x1, y1)]
#   step_size = (t2-t1)/steps
#   for i in range(1,steps+1):
#     t = t1 + i * step_size
#     (x,y) = f(t)
#     pts.append(svg.L(x=x, y=y))
#   return pts
# a = 5
# b = 4
# def f(t):
#   return (528 + 200*math.cos(a*t), 408 + 200*math.sin(b*t))

elements = []
# for _ in range(1):
elements.append(
  svg.Path(
    stroke="#000000",
    stroke_width=2,
    stroke_linecap="round",
    fill="none",
    d=upright_triangle(0,0)
  )
)

elements = [svg.Rect(stroke="green", fill="none",x=0,y=0,width=1056,height=816)] + elements

canvas = svg.SVG(
  width=1056, # US Letter
  height=816, # US Letter
  style="fill:none;stroke:rgb(0%,0%,100%);",
  elements=elements
)

with open("/Users/peter/Programming/MathArt/AxiDrawV3/G4G/assets/triangles.svg", "w") as f:
  f.write(canvas.as_str())
