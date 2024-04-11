import cv2
import datetime

cap = cv2.VideoCapture("image/Video.mp4")
while (cap.isOpened()):
    check, frame = cap.read() #รับภาพจากกล้อง Frame ต่อ Frame

    if check == True:
        currentDate = str(datetime.datetime.now())
        cv2.putText(frame,currentDate,(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),cv2.LINE_4)
        cv2.imshow("OUTPUT",frame)
        if cv2.waitKey(1)& 0xFF==ord("e"):
            break
    else :
        break
cap.release()
cv2.destroyAllWindows()