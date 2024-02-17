import svg
import random

x_count = 8
y_count = 8
layers = 7
box_size = 10

elements = []
for x in range(x_count):
  for y in range(y_count):
    for layer in range(layers):
      if (x + y) % 2 == 0 and layer > 0:
        continue
      elements.append(
        svg.Rect(
          stroke="#000000",
          stroke_width=0.3,
          fill="none",
          x=box_size*(x + layer/(2*layers - 1)),
          y=box_size*(y + layer/(2*layers - 1)),
          width=box_size*(1 - 2*layer/(2*layers - 1)),
          height=box_size*(1 - 2*layer/(2*layers - 1)),
        )
      )

canvas = svg.SVG(
  width=x_count * box_size,
  height=y_count * box_size,
  elements=elements
)

file_name = "_".join(["parity", "rectangle"])
with open("/Users/peter/Programming/MathArt/AxiDrawV3/tmp/" + file_name + ".svg", "w") as f:
  f.write(canvas.as_str())
