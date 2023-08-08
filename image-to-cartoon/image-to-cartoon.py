import cv2
import os
from pathlib import Path

def find_the_image(file_name, directory_name):
    for path, _, files in os.walk(directory_name):
        for name in files:
            if file_name == name:
                return os.path.join(path, name)
    return None

image_name = input("Image Name(example: kingfisher.jpg):")
image_directory = input("Image Location(example: ./ ):")

image_path = Path(find_the_image(image_name, image_directory))
if not image_path:
    print("Image file not found.")
    exit()

color_image = cv2.imread(str(image_path))

cartoon_style_selection = input("This script currently has 2 styles. Please type 1 or 2: ")

if cartoon_style_selection == "1":
    cartoon_image_style_1 = cv2.stylization(color_image, sigma_s=150, sigma_r=0.25)
    cv2.imshow('cartoon_1', cartoon_image_style_1)
elif cartoon_style_selection == "2":
    cartoon_image_style_2 = cv2.stylization(color_image, sigma_s=1000, sigma_r=1)
    cv2.imshow('cartoon_2', cartoon_image_style_2)
else:
    print("Invalid style selection.")

cv2.waitKey()
cv2.destroyAllWindows()
