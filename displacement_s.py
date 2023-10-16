# Program to calculate relative displacement for s-value curves

# Libraries needed, not sure all of them will made use of
import pandas as pd
import random
import numpy as np
from numpy import std, mean, sqrt
from meta_simulations import *   #This is needed but not all of them


def displacement_calc (pop_num, test_num, mean1, mean2, sd1, sd2, samp_size):

    df = pd.DataFrame({'Cumulation':[], 'Sample Numerosity': []})
    cum = []
    cum_0 = []
    std_dev = []
    std_dev_0 = []
    
    for i in range(samp_size):
        res = simulation_slim(pop_num, test_num, mean1, mean2, sd1, sd2, i, i)
        res = sorted(list(s_value(res)))
        cum.append(sum(res))
        std_dev.append(std(res))
        
        standard = simulation_slim(pop_num, test_num, mean1, mean1, sd1, sd1, i, i)
        standard = sorted(list(s_value(standard)))
        cum_0.append(sum(standard))
        std_dev_0.append(std(standard))

    cum = np.array(cum)
    cum[np.isnan(cum)] = 0
    cum_0 = np.array(cum_0)
    cum_0[np.isnan(cum_0)] = 0
    
    

    degrees_f = []

    for i, j in zip(cum[:-1], cum[1:]):
        degrees_f.append(abs(j-i))

    return (degrees_f, std_dev_0, std_dev)


if __name__ == "__main__":

    dummy, dev_0, dev = displacement_calc(1000,1000,0,0.5,1,1,30)
    df = pd.DataFrame ({'Difference between neighbors' : dummy, 'True effect standard deviation': dev, 'No effect standard deviation': dev_0})
    df.to_csv('output')
