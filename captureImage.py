import cv2
import dropbox 
def take_snapshot():
    #initializing cv2
    videoCaptureObject  = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        #read the frames while the camera is on.

        print(ret)
        #cv2.imwrite() method is used to save an image to any storage device

        cv2.imwrite("newImage.jpg",frame)
        result = False

    #releases the camera 
    videoCaptureObject.release()
    #closes all the windows that might be opened while this process

    cv2.destroyAllWindows()

take_snapshot()





