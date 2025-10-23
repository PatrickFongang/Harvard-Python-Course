import os
import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    allowed = {".jpg", ".jpeg", ".png"}
    in_ext = os.path.splitext(input_path)[1].lower()
    out_ext = os.path.splitext(output_path)[1].lower()
    if in_ext not in allowed or out_ext not in allowed:
        sys.exit("Invalid input")
    if in_ext != out_ext:
        sys.exit("Input and output have different extensions")
    if not os.path.isfile(input_path):
        sys.exit("File does not exist")
    try:
        with Image.open(input_path) as photo, Image.open("shirt.png") as shirt:
            fitted = ImageOps.fit(photo, shirt.size)
            fitted.paste(shirt, mask=shirt)
            fitted.save(output_path)
    except FileNotFoundError:
        sys.exit("File does not exist")
    except OSError:
        sys.exit("Invalid input")


if __name__ == "__main__":
    main()
