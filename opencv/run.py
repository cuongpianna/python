import cv2
import numpy as np
from matplotlib import pyplot as plt

#show img basic
def showImg():
    #read img
    img = cv2.imread('went.jpg', cv2.IMREAD_GRAYSCALE)

    #show img
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    # draw line
    plt.plot([200, 300, 400], [100, 200, 300], 'c', linewidth=5)
    plt.show()

#show vide
def showVideo():
    cap = cv2.VideoCaptured(0)
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

#draw img
def drawingImg():
    img = cv2.imread('went.jpg', cv2.IMREAD_GRAYSCALE)
    #line with arg: where, start, end,color, width
    cv2.line(img,(0,0),(150,150),(255,255,255),15)
    #ve hinh chu nhat
    #cv2.rectangle(img,(15,15),(200,150),(0,0,250),15)

    #draw circle
    #cv2.circle(img, (100, 63), 55, (0, 255, 0), -1)

    #free
    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    #pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (0, 255, 255), 3)

    #viet len anh
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'Hello world',(0,130),font,1,(200,255,155), 2, cv2.LINE_AA)


    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#thao tac vs anh
def imgOpetaion():
    img = cv2.imread('went.jpg',cv2.IMREAD_COLOR)
    px = img[69,69]
    img[55, 55] = [255, 255, 255]
    px = img[55, 55]
    print(px)
    print(img.shape)
    print(img.size)
    print(img.dtype)

    watch_face = img[37:111, 107:194]
    img[0:74, 0:87] = watch_face
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def imgarithmetics():
    img1 = cv2.imread('went.jpg')
    img2 = cv2.imread('img2.jpg')
    #add = cv2.add(img1,img2)
    add = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
    cv2.imshow('add',add)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def knear():
    trainData = np.random.randint(0,100, size=(25,2)).astype(np.float32)
    ketqua = np.random.randint(0,2, size=(25,1)).astype(np.float32)
    newMember = np.random.randint(0, 100, size=(1, 2)).astype(np.float32)
    # print(ketqua)
    # print(trainData)

    red = trainData[ketqua.ravel()==1]
    blue = trainData[ketqua.ravel() == 0]
    plt.scatter(red[:,0],red[:,1],100,'r','s')
    plt.scatter(blue[:, 0], blue[:, 1], 100, 'b', '^')
    plt.scatter(newMember[:, 0], newMember[:, 1], 100, 'g', 'o')

    #knear
    knn = cv2.ml.KNearest_create()
    knn.train(trainData,0,ketqua)
    result = knn.findNearest(newMember, 3)
    plt.show()
    print(result)

if __name__ == '__main__':
    knear()