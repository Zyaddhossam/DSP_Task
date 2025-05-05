import cv2
import os

cap = cv2.VideoCapture("TEST.mp4")

try: #creating a folder
    X = 'D:\\DSP_Test'
    if not os.path.exists(X):
        os.makedirs(X)


except OSError: #if folder not created raise error
    print("Error: Creating directory of data")


currentframe= 0
while(True):
    ret, frame = cap.read()
    if ret:
        #if a frame still exists --> create image
        name = f"{X}\\frame"+str(currentframe)+".jpg"
        print("Creating :" + name)

        #writing extracted frame
        cv2.imwrite(name, frame)

        currentframe += 1

    else:
        break

cap.release()

cap = cv2.VideoCapture("TEST.mp4")
while(True):
    ret, frame = cap.read()
    if ret:
        font = cv2.FONT_ITALIC
        cv2.putText(frame,
                    "SOS",
                    (300,300),
                    font,
                    2,
                    (0,0,0),
                    3,
                    cv2.LINE_4)


        cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xff==ord("q"):
        break

pos_msec = int(cap.get(cv2.CAP_PROP_POS_MSEC))
pos_frames = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_hieght = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
FPS = cap.get(cv2.CAP_PROP_FPS)
print(f" Total frames: {frame_count}, \n FPS: {FPS}, \n H: {frame_hieght},\n W: {frame_width},"
      f"\n Pos in milliseconds: {pos_msec}, \n Frame Index:{pos_frames}")


cap.release()
cv2.destroyAllWindows()
