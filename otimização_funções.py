#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 20:33:38 2019

@author: enricotorriero
"""

import numpy as np
from scipy.optimize import minimize 

# setting up main function (the one that will be optimized) = (x1 * x4 * (x1 + x2 + x3) + x3)
def target(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    return (x1 * x4 * (x1 + x2 + x3) + x3)

# passing constraints
#   first = x1 * x2 * x3 * x4 >= 25
#   second = squared sum of all variables = 40 
#   thid = 1 <= x1, x2, x3, x4 <= 5
def st1(x):
    return x[0] * x[1] * x[2] * x[3] - 25
def st2(x):
    sum_sq = 40
    for i in range(4):
        sum_sq -= x[i]**2
    return sum_sq

# setting up the starting point (first guess)
x0 = [1, 5, 5, 1]

# creating solver 
st3 = (1.0, 5.0)
st3_ = (st3, st3, st3, st3)
con1 = {'type' : 'ineq', 'fun' : st1}
con2 = {'type' : 'eq', 'fun' : st2}
cons = [con1, con2]

solver = minimize(target, x0, method = 'SLSQP', bounds = st3_, constraints = cons)
x = solver.x
print('Objetivo final: ' + str(target(x)))
print('x1 = ' + str(x[0]))
print('x2 = ' + str(x[1]))
print('x3 = ' + str(x[2]))
print('x4 = ' + str(x[3]))