from PIL import Image
import os

def resize_images(directory, size):
    # Get a list of all files in the directory
    file_list = os.listdir(directory)

    for filename in file_list:
        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Open the image file
            image_path = os.path.join(directory, filename)
            image = Image.open(image_path)

            # Resize the image
            resized_image = image.resize(size)

            # Save the resized image with the same filename
            resized_image.save(image_path)

    print("Image resizing complete.")

# Specify the directory where the images are located
directory = 'temp_fire'

# Specify the desired size for the images (width, height)
size = (200, 200)

# Call the function to resize the images
resize_images(directory, size)





def rename_files(directory):
    # Get a list of all files in the directory
    file_list = os.listdir(directory)

    # Define the starting number for the new filenames
    number = 5

    for filename in file_list:
        # Get the file extension
        file_extension = '.jpg'

        # Create the new filename using the current number and file extension
        new_filename = '{:04d}{}'.format(number, file_extension)

        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

        # Increment the number for the next filename
        number += 1

    print("Renaming complete.")

# Specify the directory where the files are located
directory = 'temp_fire'

# Call the function to rename the files
rename_files(directory)