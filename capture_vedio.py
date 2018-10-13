import cv2

capture = cv2.VideoCapture(0)  # 打开摄像头(默认第一个摄像头)
# capture = cv2.VideoCapture(r"F:\vv\123\111.avi")  # 打开视频
# w = capture.get(3)  # 视频的长
# h = capture.get(4)  # 视频的宽
#
# # 重设长宽
# capture.set(3, w * 2)
# capture.set(4, h * 2)

# 注意这里，不知为何，重设了宽高以后，视频保存失败(不报错，只是视频没有内容)


frcc = cv2.VideoWriter_fourcc(*"DIVX")
# frcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")  # FourCC编码方式，用来指定视频编码方式的四字节码
cap_writer = cv2.VideoWriter(r"C:\Users\Administrator\Desktop\pic\test.avi", frcc, 20.0,
                             (640, 480))  # 25是帧率FPS，(640,480)是分辨率

while capture.isOpened():
    ret, img = capture.read()
    if ret == True:

        img = cv2.rectangle(img, (0, 0), (100, 100), (255, 0, 0), 2)  # 在某个位置上画个方形
        img = cv2.putText(img, "This is my test text!!!", org=(100, 100), fontFace=cv2.FONT_HERSHEY_COMPLEX,
                          fontScale=1,
                          color=(0, 255, 0), thickness=2, lineType=cv2.LINE_8)  # 从某个点开始添加文字

        cap_writer.write(img)  # 保存video文件
        cv2.imshow("gray_img", img)  # 显示
        k = cv2.waitKey(1)
        if k & 0xFF == ord("q"):  # q键退出
            break
    else:
        break

capture.release()
cap_writer.release()
cv2.destroyAllWindows()
