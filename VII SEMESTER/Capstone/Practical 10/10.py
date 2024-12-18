import cv2
import numpy as np

def forensic_image_analysis(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image.")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 100, 200)

    noise = cv2.Laplacian(gray, cv2.CV_64F).var()
    print(f"Noise Level (Laplacian Variance): {noise}")

    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 
    high_pass = cv2.filter2D(gray, -1, kernel)

    combined = cv2.bitwise_and(edges, high_pass)
    combined_colored = cv2.cvtColor(combined, cv2.COLOR_GRAY2BGR)
    result = cv2.addWeighted(image, 0.7, combined_colored, 0.3, 0)

    cv2.imshow("Original Image", image)
    cv2.imshow("Edge Detection", edges)
    cv2.imshow("High-Pass Filtered (Possible Tampered Regions)", high_pass)
    cv2.imshow("Forensic Analysis Result", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

forensic_image_analysis("D:\College Work\VII SEMESTER\Capstone\ALL PRACTICALS\hello.jpeg")
