import math
import numpy as np  
from numpy import * 
import matplotlib.pyplot as plt
import time


E = 1
S = 10
ES = 0
P = 0

def funcEt(ES,E,S):
    return 600*ES+150*ES-100*E*S
def funcSt(ES,E,S):
    return 600*ES-100*E*S
def funcESt(ES,E,S):
    return 100*E*S-600*ES-150*ES
def funcPt(ES):
    return 150*ES

