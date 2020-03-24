import cv2
from matplotlib import pyplot as plt
import numpy as np

pic = cv2.imread('../hall_box_battery_atividade3.png')
pic = cv2.cvtColor(pic, cv2.COLOR_RGB2GRAY)

pic_copy = pic.copy()

for row_index, row in enumerate(pic):
  for column_index, pixel in enumerate(row):
    try:
      pic_copy[row_index][column_index] = abs(int(pic[row_index][column_index + 1]) - int(pic[row_index][column_index - 1]))
    except:
      print('')

plt.imshow(pic_copy, cmap="Greys_r", vmin=0, vmax=256)
plt.show()