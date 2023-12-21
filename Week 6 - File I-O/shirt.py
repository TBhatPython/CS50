import sys
import os
from PIL import Image, ImageOps

#"./Other Files/shirt.png" 
def main():

    #Needs correct number of command line args
    if len(sys.argv) != 3:
        sys.exit("Input 2 command-line arguments only")

    #To find the extentions of input and output files
    ext1 = os.path.splitext(sys.argv[1])[1]
    ext2 = os.path.splitext(sys.argv[2])[1]
    accepted_ext = [".jpeg", ".jpg", ".png"]

    #Check if input/output files are of accepted formats
    if ext1 not in accepted_ext or ext2 not in accepted_ext:
        sys.exit("Not an accepted file format")

    #Calling the work function
    overlay(sys.argv[1], "./Other Files/shirt.png", sys.argv[2])

def overlay(input, shirt, output):
    try:
        #Open input image (background image) of possible
        first_image = Image.open(input)

    #To handle if file input file is not found
    except FileNotFoundError:
        sys.exit('Input does not exist')

    #Opening and sizing the shirt image (foreground image)
    shirt = Image.open(shirt)
    size = shirt.size

    #Pasting both the background (input, first fitted to same size as shirt image) and foreground (shirt) images 
    #On the output image file.
    secondimage = ImageOps.fit(first_image, size)
    secondimage.paste(shirt, shirt)
    secondimage.save(output)
    



if __name__ == "__main__":
    main()
    
    