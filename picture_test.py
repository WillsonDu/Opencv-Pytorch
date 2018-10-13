import cv2
import os
import matplotlib.pyplot as plt

root = r"C:\Users\Administrator\Desktop\pic"
name = r"\444.jpg"
path = root + name

img = cv2.imread(path, cv2.IMREAD_COLOR)  # 读取图片

# cv2.namedWindow("window1", cv2.WINDOW_AUTOSIZE)
# cv2.imshow("444.jpg", img)

# cv2.imshow("111.jpg", cv2.imread(root + r"\333.jpg"))

# print(ord("F"))  # ord函数可以返回键盘按键对应的数字
# k = cv2.waitKey(0)  # 接受键盘输入
# print(k)

plt.figure()
plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.xticks([123, 456, 777])
plt.yticks([])
# plt.show()

plt.figure()
plt.imshow(img)
plt.show()
