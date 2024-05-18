import cv2
import numpy as np

img=cv2.imread("E:/Python-Projects/OpenCV/AI.jpeg")
c=cv2.Canny(img,200,170)
cv2.imshow("Edged Image:",c)
cv2.imshow("Original Image:",img)


'''s=cv2.pyrDown(img)
l=cv2.pyrUp(img)
cv2.imshow("Original Image:",img)
cv2.imshow("Larger Image:",l)
cv2.imshow("OSmaller Image:",s)'''


'''k=np.ones((7,7),np.float32)/49
blur=cv2.filter2D(img,-1,k)
cv2.imshow("Blurred Image:",blur)
cv2.imshow("Original Image",img)'''



'''height=img.shape[0]
width=img.shape[1]
start_row,start_col=int(height*.15),int(width*.15)
end_row,end_col=int(height*.65),int(width*.65)
cropped=img[start_row:end_row,start_col:end_col]
cv2.imshow("Cropped Image:",cropped)
cv2.imshow("Original Image",img)'''


'''video=cv2.VideoCapture(0)
while True:
    check,frame=video.read()
    cv2.imshow("frame",frame)
    cv2.waitKey(0)'''


'''rotateimg=cv2.transpose(img)
cv2.imshow("Rotated Image:",rotateimg)
cv2.imshow("Original Image:",img)'''



'''print(img.shape)
height=img.shape[0]
width=img.shape[1]
rotateimg=cv2.getRotationMatrix2D((width/2,height/2),70,.5)
finalimg=cv2.warpAffine(img,rotateimg,(width,height))
cv2.imshow("Rotated Image:",finalimg)
cv2.imshow("Original Image:",img)'''




#cv2.imshow("Output Image", img)
#cv2.imwrite("output.jpeg",img)

cv2.waitKey(0)