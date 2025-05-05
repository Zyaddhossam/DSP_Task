import cv2

cap = cv2.VideoCapture("TEST.mp4")  #read the video
#cap = cv2.VideoCapture(0)  #Capture video by default camera

if not cap.isOpened(): #check if the camera/video file is opened
    print("Error, Couldn't open")
    exit()


################## To Write and save the video#
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('D:\\OUT.mp4',fourcc,30.0,(738, 402))



##################To show the whole video that captured/uploaded
while True:
    ret,frame = cap.read()
    # cap.read() returns 2 values -->
    # 1.the first is boolean that checks if the reading is successful
    # 2.the frame that is read, frame-by-frame

    if not ret :# or(cv2.waitKey(25) & 0xff ==ord('q'))
        break
    # 25 is the wait period between each 2 frames
    #break if user entered q

    out.write(frame)
    cv2.imshow('Video',frame)
    #winname refers to the window name that will display the video
    if cv2.waitKey(25) & 0xff == ord('q'): break


####################### To show only the first frame
# ret,frame = cap.read()
# if ret:
#     cv2.imshow('Video',frame)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("Error")



######Get Video Properties(frame count, frame width,,,,,)
pos_msec = int(cap.get(cv2.CAP_PROP_POS_MSEC))
pos_frames = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_hieght = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
FPS = cap.get(cv2.CAP_PROP_FPS)
print(f" Total frames: {frame_count}, \n FPS: {FPS}, \n H: {frame_hieght},\n W: {frame_width},"
      f"\n Pos in milliseconds: {pos_msec}, \n Frame Index:{pos_frames}")





cap.release() #close the resources after the operation
out.release()
cv2.destroyAllWindows()

