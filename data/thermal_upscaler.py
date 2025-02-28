import cv2
import os
import numpy as np

# Define paths
original_dir = "thermals/original"
upscaled_dir = "thermals/upscaled"

# Ensure output directory exists
os.makedirs(upscaled_dir, exist_ok=True)

def upscale_thermal(thermal_img, target_size=(480, 640), method=cv2.INTER_CUBIC):
    """
    Upscale a thermal image progressively by a factor of 2 three times.

    Parameters:
        thermal_img (numpy array): Original thermal image.
        target_size (tuple): Final resolution (H, W) after 8x scaling.
        method (cv2 interpolation): Interpolation method (default: bicubic).

    Returns:
        upscaled_img (numpy array): Upscaled thermal image.
    """
    upscaled_img = thermal_img.copy()

    # Upscale 3 times by 2x
    for _ in range(3):
        upscaled_img = cv2.resize(upscaled_img, None, fx=2, fy=2, interpolation=method)

    # Final resize to ensure exact target dimensions
    upscaled_img = cv2.resize(upscaled_img, target_size, interpolation=method)

    return upscaled_img

# Process all images in the thermal/original folder
for filename in os.listdir(original_dir):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".tiff")):
        original_path = os.path.join(original_dir, filename)
        upscaled_path = os.path.join(upscaled_dir, filename)

        # Load thermal image as grayscale
        thermal_img = cv2.imread(original_path, cv2.IMREAD_GRAYSCALE)
        if thermal_img is None:
            print(f"Error loading {filename}, skipping...")
            continue

        # Upscale
        upscaled_img = upscale_thermal(thermal_img)

        # Save the upscaled image
        cv2.imwrite(upscaled_path, upscaled_img)
        print(f"Upscaled {filename} → {upscaled_path}")

print("All thermal images have been upscaled and saved.")
