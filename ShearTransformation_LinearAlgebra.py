
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Hi guys , I'm Mohammad Javad Rajabi, so let's dive in 

address = input("Address please : ")
print("Please wait , It may take a few seconds")

# this part gets the orginal picture (line 12) and convert color-space from BGR to RGB (line 13) 
myimage = cv2.imread(address)
myimage = cv2.cvtColor(myimage, cv2.COLOR_BGR2RGB)


rows, cols, dim = myimage.shape
M2 = np.float32([[1, 0, 0],
             	[0, 1  , 0],
            	[0, 0  , 1]])

# this part makes the orginal picture biger in new size (rows*1 , cols*1.2) with white background
white_image = np.zeros((int(rows*1),int(cols*1.2),3), np.uint8)
white_image[:,:,:] = 255
myimage = cv2.warpPerspective(myimage,M2,(int(cols*1.2),int(rows*1)), white_image, borderMode=cv2.BORDER_TRANSPARENT)

# this part is similar to line 12 but it is for the shadow picture
myimagesh = cv2.imread(address)
myimagesh = cv2.cvtColor(myimagesh, cv2.COLOR_BGR2RGB)

rows, cols, dim = myimagesh.shape
# M is shear transformation matrix
M = np.float32([[1, 0.08, 0],
             	[0, 1  , 0],
            	[0, 0  , 1]])

# this part makes the shadow picture biger in new size (rows*1 , cols*1.2) with white background
white_image = np.zeros((int(rows*1),int(cols*1.2),3), np.uint8)
white_image[:,:,:] = 255
myimagesh = cv2.warpPerspective(myimagesh,M,(int(cols*1.2),int(rows*1)), white_image, borderMode=cv2.BORDER_TRANSPARENT)


# this part changes color of shadow picture to gray color 
for i in range(int(rows*1)):
    for ii in range(int(cols*1.2)):
        r , g , b = myimagesh[i][ii]
        if (r < 230 or g < 230 or b < 230) :
            myimagesh[i][ii] = [90,90,90]   

# mainimg is the ruseult of blending of orginal picture and shadow picture
mainimg = np.zeros((int(rows*1),int(cols*1.2),dim),dtype = 'uint8')

# this part blends orginal picture and shadow picture 
for i in range(int(rows*1)):
    for ii in range(int(cols*1.2)):
        ro , go , bo = myimage[i][ii] # RGB of every pixel in orginal picture
        rsh , gsh , bsh = myimagesh[i][ii] # RGB of every pixel in shadow picture
        # if the pixel of orginal picture is not white it will be in mainimg 
        # otherwise the pixel of shadow picture is be in mainimg
        if  (ro < 230 or go < 230 or bo < 230) : 
            mainimg[i][ii] = [ro,go,bo]
        else:
            mainimg[i][ii] = [rsh,gsh,bsh]


# this part shows the picture
plt.axis('on')
plt.imshow(mainimg)
plt.show()