"""
Plot.py
Created 21/12/2021
"""
import sys
sys.path.append("..")

import numpy as np
from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt
from typing import List

class Plot:
    """
    Class Plot:
    Uses the matplotlib to plot various graphs

    Parameters: None

    Funtions:
        plotControlSurface
    """

    def __init__(self) -> None:
        pass

    def plotControlSurface(self,x,y,z,xLabel,yLabel,zLabel) -> None:
        """Plot a 3D surface showcasing the relationship between input (x,y) and output z"""
        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
        x,y = np.meshgrid(x,y)
        ax.plot_surface(np.asarray(x), np.asarray(y),np.asarray(z))
        ax.set_xlabel(xLabel)
        ax.set_ylabel(yLabel)
        ax.set_zlabel(zLabel)
        plt.title("Control Surface")
    
    def show(self):
        plt.show()
    
    def figure(self):
        plt.figure()
    
    def plotMF(self,name,sets,xDisc,xAxisRange,yAxisRange,addExtraEndPoints) -> None:
        x = self.discretize(sets.getSupport(),xDisc)
        y = [0] * xDisc
        for i in range(xDisc):
            y[i] = sets.getFS(x[i])
        
        if addExtraEndPoints:
            x2 = [0.0] * (len(x)+2)
            y2 = [0.0] * (len(y)+2)
            x2[0] = sets.getSupport().getLeft()
            x2[-1] = set.getSupport().getRight()
            for i in range(len(x)):
                x2[i+1] = x[i]
                y2[i+1] = y[i]
            x = x2
            y = y2
        plt.plot(x,y,label=name)

    def discretize(self,support,discLevel) -> List[float]:
        d = [0] * discLevel
        stepSize = (support.getSize())/(discLevel-1.0)
        d[0] = support.getLeft()
        d[-1] = support.getRight()
        for i in range(1,discLevel-1):
            d[i] = support.getLeft()+i*stepSize
        return d