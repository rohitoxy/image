import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(image_path):
    """Loads an image from a file."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image at path '{image_path}' not found.")
    return image

def invert_image(image):
    """Performs inverse transformation on the image."""
    return cv2.bitwise_not(image)

def contrast_stretching(image):
    """Enhances contrast using min-max normalization."""
    min_val, max_val = np.min(image), np.max(image)
    stretched = ((image - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    return stretched

def histogram_equalization(image):
    """Applies histogram equalization to improve contrast."""
    return cv2.equalizeHist(image)

def edge_detection(image):
    """Detects edges using the Canny edge detection algorithm."""
    return cv2.Canny(image, 100, 200)

def process_image(image_path):
    """Processes the image and displays results."""
    image = load_image(image_path)
    
    # Apply transformations
    inverted = invert_image(image)
    contrast_stretched = contrast_stretching(image)
    hist_equalized = histogram_equalization(image)
    edges = edge_detection(image)

    # Display results
    titles = ["Original", "Inverted", "Contrast Stretched", "Histogram Equalized", "Edge Detected"]
    images = [image, inverted, contrast_stretched, hist_equalized, edges]

    plt.figure(figsize=(12, 6))
    for i in range(5):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], cmap="gray")
        plt.title(titles[i])
        plt.axis("off")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    image_path = "input.jpg"  # Change this to your image file path
    process_image(image_path)
