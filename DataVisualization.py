# import the necessary packages
import imutils
import cv2

def main():
    # load the input image and show its dimensions, keeping in mind that
    # images are represented as a multi-dimensional NumPy array with
    # shape no. rows (height) x no. columns (width) x no. channels (depth)

    image = cv2.imread("metal7.jpg")
    if image is None:
        print("File not found")
        return

    (h, w, d) = image.shape
    print("width={}, height={}, depth={}".format(w, h, d))

    # display the image to our screen -- we will need to click the window
    # open by OpenCV and press a key on our keyboard to continue execution
    #cv2.imshow("Image", image)
    #cv2.waitKey(0)

    resize = cv2.resize(image, (600,600))
    gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 30, 150)
    thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)[1]
    count = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(count)
    output = resize.copy()

    #cv2.imshow("image", thresh)


    print(len(cnts))

    for c in cnts:
        cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
        cv2.imshow("Contours", output)

    cv2.waitKey(0)
    #cv2.imshow("edges", edges)
    #cv2.imshow("gray", thresh)
    #cv2.waitKey(0)

main()
