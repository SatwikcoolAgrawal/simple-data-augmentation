# Import the necessary modules
import os
import random
import shutil

# Define the source folder where the given images are stored
source_folder = "C:/Users/casak/OneDrive/Desktop/dataimg"

# Define the destination folder where the dataset will be created
destination_folder = "dataset"

# Define the number of images to pick for the dataset
num_images = 1000

# Get the list of image files in the source folder
image_files = os.listdir(source_folder)


# Create the destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Pick num_images random images from the source folder and copy them to the destination folder
for i in range(num_images):
    # Choose a random image file
    image_file = random.choice(image_files)
    new_filename = f"votingslip{i}.png"
    new_image_path = os.path.join(destination_folder, new_filename)
    # Copy the image file to the destination folder
    shutil.copy(os.path.join(source_folder, image_file), new_image_path)

# Print a message to indicate the completion of the task
print("The dataset has been created successfully in the folder:", destination_folder,100)
