import numpy as np
from math import sin,cos
import matplotlib.pyplot as plt
from tqdm import tqdm
from pylab import rcParams
rcParams['figure.figsize'] = 7,7

def radial_gradient(color,radii):
    colors=[]
    for r in radii:
        colorr=r*color+(1-r)*np.array([1,1,1])
        colors.append(colorr)
    return colors

def make_colorwheel():
    RY,YG,GC,CB,BM,MR=15,6,4,11,13,6
    ncols=RY+YG+GC+CB+BM+MR
    colorwheel=np.zeros((ncols,3))
    col=0

    colorwheel[0:RY,0]=255
    colorwheel[0:RY,1]=np.floor(255*np.arange(0,RY)/RY)
    col=col+RY

    colorwheel[col:col+YG,0]=255-np.floor(255*np.arange(0,YG)/YG)
    colorwheel[col:col+YG,1]=255
    col=col+YG

    colorwheel[col:col+GC,1]=255
    colorwheel[col:col+GC,2]=np.floor(255*np.arange(0,GC)/GC)
    col=col+GC

    colorwheel[col:col+CB,1]=255-np.floor(255*np.arange(CB)/CB)
    colorwheel[col:col+CB,2]=255
    col=col+CB

    colorwheel[col:col+BM,2]=255
    colorwheel[col:col+BM,0]=np.floor(255*np.arange(0,BM)/BM)
    col=col+BM

    colorwheel[col:col+MR,2]=255-np.floor(255*np.arange(MR)/MR)
    colorwheel[col:col+MR,0]=255
    return colorwheel/255.0
color_wheel=make_colorwheel()

def plot_colorwheel(colorwheel,steps):
    theta=(2*np.pi)/colorwheel.shape[0]
    x=np.linspace(0,1,100)
    for i in tqdm(range(colorwheel.shape[0])):
        angles=np.linspace(i*theta,(i+1)*theta,steps)
        colors=np.linspace(colorwheel[i],colorwheel[i+1],steps) if i<(colorwheel.shape[0]-1) else np.linspace(colorwheel[0],colorwheel[1],steps)
        for j in range(steps):
            color=colors[j]
            line=radial_gradient(color,x)
            for k in range(len(x)):
                plt.scatter(x[k]*cos(angles[j]),-x[k]*sin(angles[j]),color=line[k])
                plt.axis('off')
    plt.xlim(-0.6,0.6)
    plt.ylim(-0.6,0.6)
    plt.show()
plot_colorwheel(color_wheel,20)
