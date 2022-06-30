import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#LINEREG BASICS


#write the Cost functions

def cost_function(w,b,x,y):
    length=x.shape[0]
    cost=0
    for i in range(length):
        cost+=cost+w*x[i]+b-y[i]
    total_cost=cost/(2*length)
    return total_cost
