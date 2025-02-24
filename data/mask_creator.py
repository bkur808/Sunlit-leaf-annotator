import os
import cv2
import numpy as np

# Define directories
train_dir = "train"
train_labels_dir = "train_labels"
output_dir = "overlay_masks_review"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get list of images in train directory
train_images = [f for f in os.listdir(train_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Track missing overlay images
missing_overlays = []


# Process each image
for img_name in train_images:
    train_img_path = os.path.join(train_dir, img_name)
    label_img_path = os.path.join(train_labels_dir, img_name)

    # Check if corresponding label image exists
    if os.path.exists(label_img_path):
        # Read the images
        train_img = cv2.imread(train_img_path, cv2.IMREAD_COLOR)
        label_img = cv2.imread(label_img_path, cv2.IMREAD_COLOR)

        # Resize label image to match train image if necessary
        if train_img.shape[:2] != label_img.shape[:2]:
            label_img = cv2.resize(label_img, (train_img.shape[1], train_img.shape[0]), interpolation=cv2.INTER_LINEAR)

        # Blend images with 40% opacity for label
        overlay = cv2.addWeighted(label_img, 0.4, train_img, 0.6, 0)

        # Save the overlaid image
        output_path = os.path.join(output_dir, img_name)
        cv2.imwrite(output_path, overlay)
        print(f"Saved: {output_path}")
    else:
        missing_overlays.append(img_name)

# Print missing overlay images
if missing_overlays:
    print("\nImages without a corresponding mask in train_labels:")
    for missing in missing_overlays:
        print(missing)
    print()
    print(f"\nMissing {len(missing_overlays)} images.")


print("Overlay process completed.")
