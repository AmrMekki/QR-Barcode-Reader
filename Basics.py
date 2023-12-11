import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('1.jpg')
barcodes = decode(img)

if barcodes:
    barcode = barcodes[0]
    myData = barcode.data.decode('utf-8')
    print(myData)

    # Create a copy of the original image
    img_with_lines = img.copy()

    # Draw lines and text on the original image
    pts = np.array([barcode.polygon], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img_with_lines, [pts], True, (255, 0, 255), 5)
    pts2 = barcode.rect
    cv2.putText(img_with_lines, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

    # Save the result with lines
    cv2.imwrite('result.jpg', img_with_lines)

    # Extract and save the detected barcode as a separate image without lines
    x, y, w, h = pts2
    barcode_img = img[y:y+h, x:x+w]
    cv2.imwrite('barcode.jpg', barcode_img)

    # Display the result with lines
    cv2.imshow('Result', img_with_lines)
    cv2.waitKey(0)

cv2.destroyAllWindows()
