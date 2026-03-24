import numpy as np
import matplotlib.pyplot as plt

def process_image(path):
    # 1. Load the image and convert to float (0.0 to 1.0) 
    # This prevents the "overflow" issues common with uint8 (0-255)
    img = plt.imread(path).astype(float) / 255.0

    # --- BRIGHTEN ---
    # We use a simple scalar addition. NumPy broadcasts 0.2 to every pixel.
    # We then use np.clip to ensure no value exceeds 1.0
    brightened = np.clip(img + 0.2, 0, 1)

    # --- GRAYSCALE ---
    # Weights based on human perception: R: 29.9%, G: 58.7%, B: 11.4%
    weights = np.array([0.2989, 0.5870, 0.1140])
    
    # The dot product multiplies each RGB pixel by the weights and sums them
    # Resulting shape goes from (H, W, 3) to (H, W)
    grayscale = np.dot(img[..., :3], weights)

    # --- TINT (Broadcasting a Vector) ---
    # Adding a 1D vector [R, G, B] to a 3D matrix (H, W, 3)
    # This adds 0.3 to Red and 0 to Blue/Green
    red_tint = np.clip(img + np.array([0.3, 0, 0]), 0, 1)

    # Display results
    fig, axes = plt.subplots(1, 4, figsize=(15, 5))
    axes[0].imshow(img); axes[0].set_title("Original")
    axes[1].imshow(brightened); axes[1].set_title("Brightened (+0.2)")
    axes[2].imshow(grayscale, cmap='gray'); axes[2].set_title("Grayscale (Weighted)")
    axes[3].imshow(red_tint); axes[3].set_title("Red Tint (Vector Add)")
    
    for ax in axes: ax.axis('off')
    plt.show()

# Add this at the bottom of your file
if __name__ == "__main__":
    process_image("cat_image.jpg")  # Make sure this filename is correct!

