import os
import cv2

class GrayscaleConverter:
    '''
    A class to convert images to grayscale.
    '''
    def convert(self, path):
        for image in os.listdir(path):
            image_path = os.path.join(path, image)
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            cv2.imwrite(image_path, img)

revised_dataset_path = os.path.join("data", "RevisedPolesY11")

# New train/val
new_train = os.path.join(revised_dataset_path, "train")
new_val = os.path.join(revised_dataset_path, "valid")
new_test = os.path.join(revised_dataset_path, "test")

new_train_images = os.path.join(new_train, "images")
new_val_images = os.path.join(new_val, "images")
new_test_images = os.path.join(new_test, "images")

# Convert to grayscale
print("Converting to grayscale...")
grayscale_converter = GrayscaleConverter()
grayscale_converter.convert(new_train_images)
grayscale_converter.convert(new_val_images)
grayscale_converter.convert(new_test_images)

