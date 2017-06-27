import numpy as np
import matplotlib.pyplot as plt

def graph(n):
  c = 500
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
  plt.scatter(X, Y, color='k')

  for i in l:
    i = int(i)
    x1 = X.item(i)
    y1 = Y.item(i)
    r = (m*i) % c
    r = int(np.floor(r))
    x2 = X.item(r)
    y2 = Y.item(r)

    plt.plot([x1, x2], [y1, y2], color='k')

  plt.axis('off')
  plt.savefig('MMOCs/png/graph-'+str(m)+'.png', dpi=128)
  print('Graph generated, x'+str(m))



for i in np.arange(101, 201, 1):
  graph(i)
