# import library
import cv2

img = cv2.imread('lite.jpeg')  # read img

cv2.imshow('lite', img)  # display image
k = cv2.waitKey(0)

if k == 27:  # esc in keyboard
    cv2.destroyAllWindows()  # close the window

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert BGR image to grayscale

cv2.imshow('lite_gray', img_gray)  # display grayscale image
k = cv2.waitKey(0)

if k == 27:  # esc in keyboard
    cv2.destroyAllWindows()
elif k == ord('s'):  # if 's' key is pressed, save the image
    cv2.imwrite('lite_gray.png', img_gray)  # write image to your pc
    cv2.destroyWindow('lite_gray')  # close the grayscale window
