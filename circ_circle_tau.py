#!/usr/bin/env python3
# Created By: Beni
# Date: March 3, 2025
# Calculates the circumference of a circle

import math
import constants

def main():
    # asks for a radius
    radius = float(input("What is the radius of the circle?"))

    # calculate the circumference
    print("The circumference is: {}" .format(radius * constants.TAU))

if __name__ = "__main__":
    main()