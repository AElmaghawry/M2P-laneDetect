import cv2
from cv2 import line
from matplotlib import lines 
import numpy as np 

# lines= []
video = cv2.VideoCapture("outpy.mp4")
# cap = cv2.VideoCapture(0)

while True:
    ret , org_frame = video.read()
    # ret , org_frame = cap.read()
    if not ret: 
        video = cv2.VideoCapture("outpy.mp4") # read the video again 
        # cap = cv2.VideoCapture(0)
        continue 
    croppedimage = org_frame[ 350: org_frame.shape[0] ,0:org_frame.shape[1]]
    print(croppedimage.shape[1])
    print("_____")
    frame = cv2.GaussianBlur(croppedimage , (5,5),0)
    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    low_yellow = np.array([15 , 117 , 116])
    up_yellow = np.array([255 , 255 , 255])

 
    mask = cv2.inRange(hsv , low_yellow , up_yellow)
    edges = cv2.Canny(mask, 20 ,80)

    lines = cv2.HoughLinesP(edges , 1 , np.pi/180, 100 , maxLineGap = 50)
    try:
        # if lines is not None : 
        #     print(lines)
        #     for line in lines: 
        #         x1 , y1 , x2 , y2 = lines[0][0]
        #         print (line)
        #         cv2.line(frame , (x1,y1),(x2 , y2), (0,255 ,0 ) , 5)
        # print(len(lines))
        # if (len(lines) <= 4 ):
        # print(lines)
        # print("==================")
        min_x = 1000
        max_x = 0
        min_line = None
        max_line = None
        for line in lines:
            if line[0][0] < min_x:
                 min_x = line[0][0]
                 min_line = line
            if line[0][0] > max_x:
                max_x = line[0][0]
                max_line = line
        # print(max_line)
        # print("---------")
        # print(min_line)

        # axis = [lines[0][0][0], lines[1][0][0], lines[2][0][0], lines[3][0][0]]
        # print(axis)
        # max_index = axis.index(max (axis))
        # min_index = axis.index(min (axis))
        # min_line = lines[min_index]
        # max_line = lines[max_index]
        # x0, y0 = (min_line[2] + max_line[2])/2, max(min_line[3], max_line[3])
        x1, y1, x2, y2 = min_line[0]
        min_x1 = x1 
        min_x2 = x2 
        min_y2 = y2
        minl1 = min(min_x1 , min_x2)
        # avg_x11 = (x1+x2)/2 
        print("min point")
        print(min_line[0])
        print("*********")
        cv2.line(frame , (x1,y1),(x2 , y2), (0,255 ,0 ) , 5)
        x1, y1, x2, y2 = max_line[0]
        max_x1 = x1 
        max_x2 = x1 
        max_y2 = y1
        maxl1 = max(max_x1 , max_x2)
        # avg_x22 = (x1+x2)/2
        print("max point")
        print(max_line[0])
        print("*********")  
        cv2.line(frame , (x1,y1),(x2 , y2), (0,255 ,0 ) , 5)
        avglx = ((maxl1 + minl1)/2)
        minly = min(max_y2 , min_y2)
        print(int(avglx))
        print("-------")
        # print(minly)
        print(int(croppedimage.shape[1])/2)
        print("######")
        print(avglx)

        errorV = avglx - croppedimage.shape[1]/2 
        print("Error Value ")
        print(errorV)
        # if (int(avglx) < int(croppedimage.shape[1])/2):
        #     print("Go right!")
        #     errorV = (avglx) - (croppedimage.shape[1])/2
        #     print("Error Value")
        #     print(errorV)
        # if (int(avglx) > int(croppedimage.shape[1])/2):
        #     print("Go left")
        #     print("Error Value")
        #     print(errorV)
        #     errorV = avglx - croppedimage.shape[1]/2
        # if (int(avglx) == int(croppedimage.shape[1])/2):
        #     print("Go Forward")
        #     errorV = avglx - croppedimage.shape[1]/2
        #     print("Error Value")
        #     print(errorV)
        print("-*-*-*-*-*-*-*-*-*")
            # try:

            #     if lines is not None : 
            #         print(lines)

                
            #         for line in lines: 
            #             x1 , y1 , x2 , y2 = line[0]
            #             print (line)
            #             cv2.line(frame , (x1,y1),(x2 , y2), (0,255 ,0 ) , 5)
    except Exception as e:
        print(e)
        

    cv2.imshow("frame",frame)
    cv2.imshow("edges", edges)
    cv2.imshow("mask",mask)

    key = cv2.waitKey(1)
    if key == 27:
        break 
video.release()
# cap.release()
cv2.destroyAllWindows()


