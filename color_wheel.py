import numpy as np
from math import sin,cos
import matplotlib.pyplot as plt

def make_colorwheel():
    RY = 15
    YG = 6
    GC = 4
    CB = 11
    BM = 13
    MR = 6

    ncols = RY + YG + GC + CB + BM + MR
    colorwheel = np.zeros((ncols, 3))
    col = 0

    # RY
    colorwheel[0:RY, 0] = 255
    colorwheel[0:RY, 1] = np.floor(255*np.arange(0,RY)/RY)
    col = col+RY
    # YG
    colorwheel[col:col+YG, 0] = 255 - np.floor(255*np.arange(0,YG)/YG)
    colorwheel[col:col+YG, 1] = 255
    col = col+YG
    # GC
    colorwheel[col:col+GC, 1] = 255
    colorwheel[col:col+GC, 2] = np.floor(255*np.arange(0,GC)/GC)
    col = col+GC
    # CB
    colorwheel[col:col+CB, 1] = 255 - np.floor(255*np.arange(CB)/CB)
    colorwheel[col:col+CB, 2] = 255
    col = col+CB
    # BM
    colorwheel[col:col+BM, 2] = 255
    colorwheel[col:col+BM, 0] = np.floor(255*np.arange(0,BM)/BM)
    col = col+BM
    # MR
    colorwheel[col:col+MR, 2] = 255 - np.floor(255*np.arange(MR)/MR)
    colorwheel[col:col+MR, 0] = 255
    return colorwheel/255.0
color_wheel=make_colorwheel()

def plot_colorwheel(colorwheel,steps):
    theta=(2*np.pi)/colorwheel.shape[0]
    x=np.linspace(0,1,steps)
    for i in range(colorwheel.shape[0]):
        angles=np.linspace(i*theta,(i+1)*theta,steps)
        colors=np.linspace(colorwheel[i],colorwheel[i+1],steps) if i<54 else np.linspace(colorwheel[0],colorwheel[1],steps)
        for j in range(steps):
            plt.plot(x*cos(angles[j]),-x*sin(angles[j]),color=colors[j])
            plt.axis('off')
    plt.show()


plot_colorwheel(color_wheel,15)
