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


def test4():
    with Image.open("cat_test.png") as input_file:
        ans = input_file.convert("L")
        input_image_arr = np.asarray(input_file)
        output_image_arr = (input_image_arr * np.array([0.299, 0.587, 0.114])).sum(axis=2)
        if np.max(np.abs(ans - output_image_arr)) < 1:
            print("TEST 4: Correct")
            return 1
        else:
            print("TEST 4: WRONG")
            return 0


def Autotest():
    print("Testing in progreess")
    test1()
    test2()
    test3()
    test4()
    print("Testing completed")
