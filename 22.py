import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

flat_chess = cv2.imread('flat_chessboard.png')
plt.imshow(flat_chess)

found,corners = cv2.findChessboardCorners(flat_chess,(7,7))
found,corners

cv2.drawChessboardCorners(flat_chess,(7,7),corners,found)
plt.imshow(flat_chess)

dots = cv2.imread('dot_grid.png')
plt.imshow(dots)

found , corners = cv2.findCirclesGrid(dots,(10,10),cv2.CALIB_CB_SYMMETRIC_GRID)
cv2.drawChessboardCorners(dots,(10,10),corners,found)
plt.imshow(dots)

