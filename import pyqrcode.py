import pyqrcode


#tkaya copy link aw babata dabne kadatawet
link = "--------"

image = pyqrcode.create(link)

image.svg("mylink.svg", scale= 9)