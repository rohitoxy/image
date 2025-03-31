import cv2
import numpy as np
import os

# Load the image
image_path = "apple_158989157.png"  # Change this to your image file
if not os.path.exists(image_path):
    print("Error: File not found!")
    exit()

image = cv2.imread(image_path)

# Functions for different image processing operations

def show_image_details():
    """Prints the size and shape of the image."""
    height, width, channels = image.shape
    print(f"\n📏 Image Dimensions: {width}x{height}")
    print(f"🎨 Number of Channels: {channels}\n")

def convert_to_grayscale():
    """Converts the image to grayscale and saves it."""
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gray_image.jpg", gray_image)
    print("✅ Grayscale image saved as 'gray_image.jpg'.")

def convert_to_binary():
    """Converts the image to binary (black & white) and saves it."""
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    cv2.imwrite("binary_image.jpg", binary_image)
    print("✅ Binary image saved as 'binary_image.jpg'.")

def scale_image():
    """Scales down the image by 50% and saves it."""
    scale_percent = 50  # Reduce size by 50%
    new_width = int(image.shape[1] * scale_percent / 100)
    new_height = int(image.shape[0] * scale_percent / 100)
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
    cv2.imwrite("resized_image.jpg", resized_image)
    print("✅ Resized image saved as 'resized_image.jpg'.")

def remove_noise():
    """Applies Gaussian Blur to remove noise and saves the image."""
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    denoised_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    cv2.imwrite("denoised_image.jpg", denoised_image)
    print("✅ Denoised image saved as 'denoised_image.jpg'.")

# Dictionary-based menu (acts as a switch-case)
operations = {
    "1": show_image_details,
    "2": convert_to_grayscale,
    "3": convert_to_binary,
    "4": scale_image,
    "5": remove_noise,
    "6": exit
}

# Menu loop
while True:
    print("\n📌 Choose an image processing operation:")
    print("1️⃣ Show Image Details")
    print("2️⃣ Convert to Grayscale")
    print("3️⃣ Convert to Binary")
    print("4️⃣ Scale Image")
    print("5️⃣ Remove Noise")
    print("6️⃣ Exit")

    choice = input("👉 Enter your choice (1-6): ")

    if choice in operations:
        operations[choice]()  # Calls the corresponding function
    else:
        print("❌ Invalid choice! Please enter a number between 1 and 6.")
