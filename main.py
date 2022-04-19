import sys
import argparse
from PIL import Image
import numpy as np


def main():
    args_parser = argparse.ArgumentParser(description='Parskaya Masha HW4')
    args_parser.add_argument('input', type=str, help='Input file name.')
    args_parser.add_argument('output', type=str, help='Output file name.')
    args = args_parser.parse_args()
    try:
        with Image.open(args.input) as input_file:
            #input_file.convert("L").show() <- it does exactly what we want, so we will not use it
            input_image_arr = np.asarray(input_file)
            #ITU-R 601-2 luma transform
            output_image_arr = (input_image_arr * np.array([0.299, 0.587, 0.114])).sum(axis=2)
            output_image = Image.fromarray(output_image_arr).convert("RGB")
            if len(args.output.split(".")) > 1:
                output_image.save(args.output, args.output.split(".")[-1])
            else:
                output_image.save(args.output, format="png")

    except FileNotFoundError:
        print("File not found")
        return 1


if __name__ == "__main__":
    main()
