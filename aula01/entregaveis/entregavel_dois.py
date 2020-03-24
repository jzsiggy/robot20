import cv2
from matplotlib import pyplot as plt
import numpy as np

caixote = cv2.imread('../cena_canto_sala.jpg')
caixote = cv2.cvtColor(caixote, cv2.COLOR_BGR2RGB)

caixote_copy = caixote.copy()

for column_index, column in enumerate(caixote):
  for row_index, pixel in enumerate(column):
    if pixel[0] > 150 and pixel[2] < 10:
      caixote_copy[column_index][row_index] = 255
    

plt.imshow(caixote_copy)
plt.show()