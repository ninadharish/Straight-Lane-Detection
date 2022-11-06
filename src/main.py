import math
import cv2
import numpy as np


def highlight_lanes(image):

    img = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)

    height, length = img.shape

    temp = np.zeros_like(img[:, :])
    cv2.fillConvexPoly(temp, np.array([[0, height], [337, 330], [587, 330], [length, height]]), 255)

    img = cv2.bitwise_and(img, img, mask=temp)
    _, img = cv2.threshold(img,200,255,cv2.THRESH_BINARY)

    lines = cv2.HoughLinesP(img, 1, (np.pi/180), 8, None, 5, 20)

    cleans = np.empty(shape=[0,4], dtype=np.int32)
    for l in lines:
        alfa = math.degrees(math.atan2(l[0][2]-l[0][0], l[0][3]-l[0][1]))
        if len(cleans) == 0:
            cleans = np.append(cleans, [l[0]], axis=0)
            continue
        similar = False
        for c in cleans:
            beta = math.degrees(math.atan2(c[2]-c[0], c[3]-c[1]))
            if abs(alfa-beta) < 15:
                similar = True
                break
        if not similar:
            cleans = np.append(cleans, [l[0]], axis=0)
    if cleans is not None:
        for i in range(0, len(cleans)):
            line_length = math.sqrt((cleans[i, 0]-cleans[i, 2])**2 + (cleans[i, 1]-cleans[i, 3])**2)
            if 5 < line_length < 200:
                cv2.line(image, (cleans[i, 0], cleans[i, 1]), (cleans[i, 2], cleans[i, 3]), (0,0,255), 5, cv2.LINE_AA)
            elif line_length > 200:
                cv2.line(image, (cleans[i, 0], cleans[i, 1]), (cleans[i, 2], cleans[i, 3]), (0,255,0), 5, cv2.LINE_AA)
    
    return image


def laneDetect(video):

    cap = cv2.VideoCapture(video)
    # out = cv2.VideoWriter('../output/problem2.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 10, (960,540))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        
        image = highlight_lanes(frame)

        # out.write(image)

        cv2.imshow('Problem2 Output', image)
        cv2.waitKey(25)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    
    laneDetect('../data/whiteline.mp4')

        
