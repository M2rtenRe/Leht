#!/usr/bin/python
from hashlib import sha512
from bitstring import BitArray
import numpy as np
import cv2,os,urllib.request,random,string
def captureCam(time):
    count = 0
    imageCount = "shot"+str(count)+".jpg"
    imgUrl = os.environ.get('RNGCAM_IP')
    while os.path.exists("/home/m2rtenreinaasoriginal/Pictures/"+str(imageCount)):
        count += 1
        imageCount = "shot"+str(count)+".jpg"
    imageDir = "/home/m2rtenreinaasoriginal/Pictures/"+str(imageCount)
    try:
        imgResp = urllib.request.urlopen(imgUrl)
    except:
        return "No connection"
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img = cv2.imdecode(imgNp,-1)
    cv2.imwrite(imageDir, img)
    with open(imageDir,"rb") as imageF:
        f = imageF.read()
        b = bytearray(f)
        bits = BitArray(b).bin
    if time == 0:
        os.remove(imageDir)
        random.seed(bits)
        returnable = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation) for n in range(256)).replace("-", "").replace(",","").replace(":","")
        return returnable
