import cv2
import numpy as np

img = cv2.imread('../Material/lena.jpg',0)

rows, cols = img.shape

M = np.float32([[1, 0, 25], [0, 1, 25]])

dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', dst)
print("Pulsa 0 para cerrar programa...")
cv2.waitKey(0);
cv2.destroyAllWindows();