from PIL import Image

# open the image file and store it as an object
img = Image.open('flower.jpg')
px = img.load()

# get width and height of image
w = img.size[0]
h = img.size[1]

#Sample functions
# turn one pixel purple
def drawPurplePixel():
    px[50,50] = (153, 0, 255)

# turn a horizontal line of pixels red
def drawRedLine():
    for x in range(w):
        px[x,30] = (255, 0 ,0)

# turn all pixels red
def makeRed():
    for x in range(w):
        for y in range(h):
            px[x,y] = (255, 0, 0)
        
 

# Uncomment the function you want to test
#drawPurplePixel()
#drawRedLine()
#makeRed()


# display image
img.show()