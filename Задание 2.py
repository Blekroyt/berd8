#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-
import math
import sys

def cylinder(r, h):
from math import pi
def circle(r): return pi*r**2
s = 2*pi*r*h
if input('Full area? [y/n]: ') == 'y': \
s += 2*circle(r)
return s

r, h = 1, 1
print('s =', cylinder(r, h))
