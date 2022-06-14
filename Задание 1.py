#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-
import math
import sys

def test():
  number = int(input('Введите число: '))
  if number > 0:
    positive()
  elif number < 0:
    negative()
  else:
    print('Я вас не совсем понял. ;)')
    test()
 
def positive():
  print('Положительное')
 
def negative():
  print('Отрицательное')
 
test()
