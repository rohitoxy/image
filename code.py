import cv2
import numpy as np

def process_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image. Please check the file path.")
        return
    
    # Print the size and shape of the image
    height, width, channels = image.shape
    print(f"Image Size: {height}x{width}, Channels: {channels}")
    
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray_image.jpg', gray_image)
    print("Grayscale image saved as 'gray_image.jpg'.")
    
    # Convert image to binary (thresholding)
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite('binary_image.jpg', binary_image)
    print("Binary image saved as 'binary_image.jpg'.")
    
    # Scale the image (reduce size by half)
    scaled_image = cv2.resize(image, (width // 2, height // 2))
    cv2.imwrite('scaled_image.jpg', scaled_image)
    print("Scaled image saved as 'scaled_image.jpg'.")
    
    # Remove noise using GaussianBlur
    denoised_image = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imwrite('denoised_image.jpg', denoised_image)
    print("Denoised image saved as 'denoised_image.jpg'.")

# Example usage
if __name__ == "__main__":
    image_path = "input.jpg"  # Change this to the path of your image
    process_image(image_path)
