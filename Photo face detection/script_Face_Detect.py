import cv2
  
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("group_Photo.jpg")

img=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(grey_img,
scaleFactor=1.05,
minNeighbors=10)

cv2.imshow("Original Photo",img)
for x, y, w, h in faces:
    img=cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),3)

print(faces)
#print(type(faces))



cv2.imshow("face Recgonized",img)
cv2.waitKey(0)
cv2.destroyAllWindows()