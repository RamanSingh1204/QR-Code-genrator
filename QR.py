import qrcode

img = qrcode.make("https://instagram.com/srm.auv?igshid=NDc0ODY0MjQ=")
img.save("auv.jpg")
