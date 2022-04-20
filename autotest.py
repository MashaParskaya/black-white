import sys
import argparse
from PIL import Image
import numpy as np


def test1():
    with Image.open("red_test.png") as input_file:
        input_image_arr = np.asarray(input_file)
        for i in range(input_image_arr.shape[0]):
            for j in range(input_image_arr.shape[1]):
                if not (input_image_arr[i, j, 0] == 255 and
                        input_image_arr[i, j, 1] == 0 and
                        input_image_arr[i, j, 2] == 0):
                    print("TEST 1: WRONG")
                    return 0
    print("TEST 1: Correct")
    return 1


def test2():
    with Image.open("green_test.png") as input_file:
        input_image_arr = np.asarray(input_file)
        for i in range(input_image_arr.shape[0]):
            for j in range(input_image_arr.shape[1]):
                if not (input_image_arr[i, j, 0] == 0 and
                        input_image_arr[i, j, 1] == 255 and
                        input_image_arr[i, j, 2] == 0):
                    print("TEST 1: WRONG")
                    return 0
    print("TEST 2: Correct")
    return 1


def test3():
    with Image.open("blue_test.png") as input_file:
        input_image_arr = np.asarray(input_file)
        for i in range(input_image_arr.shape[0]):
            for j in range(input_image_arr.shape[1]):
                if not (input_image_arr[i, j, 0] == 0 and
                        input_image_arr[i, j, 1] == 0 and
                        input_image_arr[i, j, 2] == 255):
                    print("TEST 1: WRONG")
                    return 0
    print("TEST 3: Correct")
    return 1


def Autotest():
    print("Testing in progreess")
    test1()
    test2()
    test3()
    print("Testing completed")
