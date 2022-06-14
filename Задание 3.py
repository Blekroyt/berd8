#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-
import math
import 

def getInput():
    return input()
 
 
def testInput(a):
    if type(a) == int or type(a) == float:
        return True
    elif a.isnumeric():
        return True
    else:
        return False
 
 
def strToInt(a):
    return int(a)
 
 
def printInt(a):
    print(a)
 
 
b = getInput()
if testInput(b):
    printInt(strToInt(b))
