import numpy as np
import matplotlib.pyplot as plt
import progressbar

NOfP = int(input("How many points do you want? "))
Diff = input("Custom number of image? [y/n] ")
if Diff == "y":
  NOfI = int(input("Then, how many images? "))
else:
  NOfI = NOfP
path = input("Choose the path of the rendered elements ('.' of local directory): ")
extI = input("Choose the extension of each image ('png', 'svg', 'jpg', ...): ")
Ndpi = int(input("DPI (bigger, better, harder): "))

bar = progressbar.ProgressBar(widgets=[
    ' [', progressbar.Timer(), '] ',
    progressbar.Bar(),
    ' (', progressbar.ETA(), ') ',
])

def graph(n):
  c = NOfP
  m = n
  d = []
  l = np.linspace(0, c-1, c)

  for i in l:
    rad = 2*np.pi / c
    d.append(rad * i)

  X = np.cos(d)
  Y = np.sin(d)

  plt.close()
  plt.figure(figsize=(32, 32))
  plt.scatter(X, Y, color="k")

  for i in l:
    i = int(i)
    x1 = X.item(i)
    y1 = Y.item(i)
    r = (m*i) % c
    r = int(np.floor(r))
    x2 = X.item(r)
    y2 = Y.item(r)

    plt.plot([x1, x2], [y1, y2], color="k")

  plt.axis("off")
  plt.savefig(path + "/graph-" + str(m) + "." + extI, dpi=Ndpi)

for i in range(NOfI):
  graph(i)
  bar.update(i*100/NOfP)
