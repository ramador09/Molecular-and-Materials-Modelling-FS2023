import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import physical_constants

#### this subroutine identifies all molecules connected to a given one
#### simple BUT NOT EFFICIENT
def allconnected(m,id,nx,ny):
    
    theconnected=[m[id]]
    n,l=neighbors(m,id,nx,ny)
    if n>0:
        remain=list(m) 
        remain.remove(m[id])
        for i in l:
            #theconnected.append(m[i])
            remain.remove(m[i])
        for i in l:
            remain.append(m[i])
            theconnected=theconnected+allconnected(remain,len(remain)-1,nx,ny)
            for j in theconnected:
                if j in remain:
                    remain.remove(j)

    return theconnected

def ene(mol,de,nx,ny):
    totene=0.0
    for m in range(len(mol)):
        n,l =neighbors(mol,m,nx,ny)
        totene=totene + n*de
    return totene/2

#### PERIODIC BOUNDARY CONTITIONS
def pbc(a,nx,ny):
    if a[0] <0: 
        a[0]=a[0]+nx
    elif a[0] > nx  -1 :
        a[0]=a[0]-nx
    if a[1] <0: 
        a[1]=a[1]+ny
    elif a[1] > ny  -1:
        a[1]=a[1]-ny
    return a

#### CONVERT the lattice coordinates in cartesian coordinates
#### used for plotting
def coordinates(m,dx,dy):
    x=[]
    y=[]
    for i in m:
       x.append(i[0]*dx+i[2]*dx/2)
       y.append(i[1]*dy-i[2]*dy/2)
    return x,y

#### find the 1st neighboring molecules to a given one
def neighbors(a,id,nx,ny):
    nneig=0
    allneig=[]
    thepoint=np.array(a[id])
    if a[id][2] == 0:
        for inc in [[0,0,1],[1,0,0],[0,1,1],[-1,1,1],[-1,0,0],[-1,0,1]]:
            theneig=(thepoint + np.array(inc)).tolist()
            theneig=pbc(theneig,nx,ny)
            if theneig in a:
                nneig=nneig+1
                allneig.append(a.index(theneig))
    else:
        for inc in [[1,-1,-1],[1,0,0],[1,0,-1],[0,0,-1],[-1,0,0],[0,-1,-1]]:
            theneig=(thepoint + np.array(inc)).tolist()
            theneig=pbc(theneig,nx,ny)
            if theneig in a:
                nneig=nneig+1
                allneig.append(a.index(theneig))
    return nneig,allneig