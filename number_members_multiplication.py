#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard library import.
import sys

# Third-part library import.

# Project library import.

######################
# 277777788888899
# ==>
# 2*7*7*7*7*7*7*8*8*8*8*8*8*9*9 = ...
# Bases on "What's special about 277777788888899? - Numberphile"'s video
######################

def check_int(of_this):
    try:
        return True, int(of_this)
    except:
        return False, of_this

def decompose(these_digits):
    return "*".join([d for d in str(these_digits)])

def multiplication(these_digits):
    digits = [int(n) for n in str(these_digits)]
    if 0 in digits:
        return 0

    r = 1
    for x in digits:
        r = r * x

    return r

def main(arg):
    """
    Main function.
    @parameters : some arguments, in case of use.
    @return : 0 = all was good.
              ... = some problem occures.
    """
    print("")

    if not arg:
        print("Nothing to compute !\n")
        return 1

    int_ok, number = check_int(arg[0])
    if not int_ok:
        print("{} is NOT an integer !\n".format(number))
        return 2

    step = 0
    while number > 9:
        print("Result of {} = ".format(decompose(number)), end="")
        number = multiplication(number)
        print(number)
        step += 1

    print("Number of steps : {}\n".format(step))
    return 0

######################

if __name__ == "__main__":
    ret_code = main(sys.argv[1:])      # Keep only the argus after the script name.
    sys.exit(ret_code)
