# import libarary
import cv2

img = cv2.imread(r"D:\coding\python\cv\read-and-write-an-image-in-openCV\lite.jpeg") #read img

cv2.imshow('lite',img)#display image
k=cv2.waitKey(0)

if k == 27: #esc in kaybourdconvert  RGB image to GRAY image-in-openCV
    cv2.destroyAllWindows() # close the window 

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert img RGB to gray

cv2.imshow('lite',img_gray)#display image
k=cv2.waitKey(0)

if k == 27: #esc in kaybourd
    cv2.destroyAllWindows()
elif k == ord('s'):#if order is s save the image
    cv2.imwrite('lite_gray.png',img_gray)#write image in your pc  
    cv2.destroyAllWindows() # close the window 