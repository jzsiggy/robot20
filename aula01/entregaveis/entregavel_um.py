import cv2
from matplotlib import pyplot as plt
import numpy as np

def distribute_color_hist(image):

  x_axis = ( image.flatten() - 8 ) * 50

  hist, bins = np.histogram(x_axis, 256, [0,256])

  cdf = hist.cumsum()
  cdf_normalized = cdf * hist.max()/ cdf.max()

  plt.plot(cdf_normalized, color = 'b')
  plt.hist(x_axis, 256, [0,256], color = 'r')
  plt.xlim([0,256])
  plt.legend(('cdf','histogram'), loc = 'upper left')
  plt.show()
  return x_axis


def list_to_img(image):
  nova_img = []
  for x in image:
    coluna = []
    for y in x:
      y = (y-8) * 5
      coluna.append(y)
    nova_img.append(coluna)
  nova_img = np.array(nova_img)
  plt.imshow(nova_img, cmap="Greys_r", vmin=0, vmax=256)
  plt.show()

rintin = cv2.imread('../RinTinTin.jpg')
rintin_gray = cv2.cvtColor(rintin, cv2.COLOR_RGB2GRAY)

print(rintin_gray.shape)

# distribute_color_hist(rintin_gray)

list_to_img(rintin_gray)

