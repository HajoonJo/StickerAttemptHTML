import cv2         

if __name__ == "__main__":
    img_path = "./BORIS.png"

    img = cv2.imread(img_path)
    print(img)

    cv2.imshow("Boris", img)
    cv2.waitKey(0)
