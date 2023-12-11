# QR-Barcode-Reader

## Overview

### This project is done using the pyzbar library
We can use pyzbar to detect QR Codes or Barcodes in images or live videos

I have edited the code to be able to:
1. Save a picture of the result with the bounding box
2. Save a picture of the barcode/QRcode by itself without a bounding box

To use live videos you should attach to the project:
```
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
```
before the `while(true)`
And in the beginning of the loop
```
success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        .
        .
        .

```

To start project
`pip install opencv-python` or any version of OpenCV that is available at the time
`pip install numpy`
finally `pip install pyzbar`

