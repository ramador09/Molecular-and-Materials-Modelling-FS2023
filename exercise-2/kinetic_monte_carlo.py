import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import physical_constants
import time

def unique(l):
    newk = []
    for i in l:
        if i not in newk:
            newk.append(i)
    return newk

### periodic boundary conditions
def pbc(v,nx,ny):
    b=np.array(v)
    dim=len(b.shape)
    if dim==2:
        for a in v:
            if a[0] <0: 
                a[0]=a[0]+nx
            elif a[0] > nx  -1 :
                a[0]=a[0]-nx
            if a[1] <0: 
                a[1]=a[1]+ny
            elif a[1] > ny  -1:
                a[1]=a[1]-ny
    else:
        if v[0] <0: 
            v[0]=v[0]+nx
        elif v[0] > nx  -1 :
            v[0]=v[0]-nx
        if v[1] <0: 
            v[1]=v[1]+ny
        elif v[1] > ny  -1:
            v[1]=v[1]-ny
    return v

### map lattice system coordinate  to cartesian coordinates
def coordinates(m,dx,dy):
    x=[]
    y=[]
    c=[]
    for i in m:
        x.append(i[0]*dx+i[2]*dx/2)
        y.append(i[1]*dy-i[2]*dy/2)
        if i[3]==0:
            c.append('blue')
        else:
            c.append('red')
    return x,y,c

### list of possible events with reference to the lattice coordinate convention
### the forth index means unbound (0) or bound (1) molecule
def events(m,selection,nx,ny):
    allevents=[]
    set=[]
    #### list of first neighbors (relative position)
    # e.g.
    #    set[0] == (6)neigh. at site 0 (ids==0)
    #    set[1] == (6)neigh. at site 1 (ids==1)
    set.append([[0,0,1,0],[1,0,0,0],[0,1,1,0],[-1,1,1,0],[-1,0,0,0],[-1,0,1,0]])
    set.append([[1,-1,-1,0],[1,0,0,0],[1,0,-1,0],[0,0,-1,0],[-1,0,0,0],[0,-1,-1,0]])
    

    for i in selection:
        #### le is the list of possible events
        le=[] 
        #### consider only molecules that are not binded
        if m[i][3] == 0:

            #### the funcion neighbors returns "n" the number of occupied
            #### 1st nb sites and "l"  implicit and explicit list of
            ####  the 1st nb sites occupied e.g. (2,[[0,[3,3,0,0]],[5,[2,3,1,0]]])
            n,l=neighbors(m,i,nx,ny)
            ids=m[i][2]

            #### if there are no first neigh then 6 diffusions possible
            #### add all possible displacements (tobeadded) for molecule i (involved)
            thepoint=np.array(m[i])
            if n==0: 
                tobeadded=pbc((thepoint + np.array(set[int(ids)])).tolist(),nx,ny)
                involved=[i]
                for d in tobeadded:
                    le.append([[d],'d',involved]) 
                   #le=le+pbc(tobeadded,nx,ny)
                   #le=[c+['d']+involved for c in le]
            else:
                # n = ... 1 |2 |3 |4 |5 ,where |=='or'
                away=[0,1,2,3,4,5]
                dr=[]
                dstring='d'+str(n)
                if n==2:
                    ndist=np.abs(l[0][0]-l[1][0])
                    if ndist==1 or ndist==5:
                        drstring='drl'+str(n) # 2 neighbooring nb 
                    else:
                        drstring='dr'+str(n)  # 2 non-neighbooring nb
                else:
                    drstring='dr'+str(n)
                # n = ... 1 |3 |4 |5 ,where |=='or'
                for nn in l:
                    ni=nn[0]
                    ns=nn[1]
                    away.remove(ni)

                    #### binding
                    involved=[i,m.index(ns)]
                    new1=list(m[i])
                    new1[3]=1
                    new2=list(ns)
                    new2[3]=1
                    le.append([[new1,new2],'b',involved])

                    #### diffusion around the neighbor
                    for aw in [1,5]:
                        nsite=np.mod(ni+aw,6)
                        if nsite not in dr:
                            dr.append(nsite)
                for nn in l:
                    ni=nn[0]
                    #dr = list(filter((ni).__ne__, dr))
                    if ni in dr:
                        dr.remove(ni)
                #### for all possible mooves (dr) ![remaining around at least one neighbor]  append event.
                #### The event is coded as 'dri' where 'i' is the position relative to m[i]
                for nsite in dr:
                    if nsite in away:
                        away.remove(nsite)
                    aux=(thepoint + np.array(set[int(ids)][nsite])).tolist()
                    aux=pbc(aux,nx,ny)
                    le.append([[aux],drstring,[i]])
                #### away contains the possible moves to sites non-neighbooring to any nb
                #### diffusion away
                for nsite in away:
                    dstring='d'+str(n)
                    aux=(thepoint + np.array(set[int(ids)][nsite])).tolist()
                    aux=pbc(aux,nx,ny)
                    le.append([[aux],dstring,[i]])
        allevents=allevents+le
    return allevents



### compute the total rate of events
def total_rate(events,rates):
    R=np.sum([rates[i[1]] for i in events])
    
    return R

### select randomly an event from the list of possible events
def find_event(R,rates,events):
    sum__l=0
    rho1=np.random.random()
    target=rho1*R
    sum_l=rates[events[0][1]]
    if target<sum_l:
        the_event=events[0]
    else:
        for i in events[1:]:
            #sum_U=sum_l+rates[i[1]]
            sum_l+=rates[i[1]]
            if target<sum_l:
                the_event=i
                break
            #sum_l=sum_U
    return the_event


### neighbors of a molecule according to the lattice coordinate convention
def neighbors(a,id,nx,ny):
    nneig=0
    allneig=[]
    f=[]
    f.append([[0,0,1,0],[1,0,0,0],[0,1,1,0],[-1,1,1,0],[-1,0,0,0],[-1,0,1,0]])
    f.append([[1,-1,-1,0],[1,0,0,0],[1,0,-1,0],[0,0,-1,0],[-1,0,0,0],[0,-1,-1,0]])
    thepoint=np.array(a[id])
    ids=a[id][2]
    for n in range(6):
        theneig=(thepoint + np.array(f[int(ids)][n])).tolist()
        theneig=pbc(theneig,nx,ny)
        alt1=list(theneig) 
        alt2=list(theneig) 
        alt1[3]=1 
        alt2[3]=0
        if alt1 in a:
            nneig=nneig+1
            allneig.append([n,alt1])
        if alt2 in a:
            nneig=nneig+1
            allneig.append([n,alt2])
    return nneig,allneig


### function to execute an event
def apply_event(molecules,selected_event,possible_events,nx,ny):
    new_positions=selected_event[0]
    tobeupdated=[]
    theinvolved=0
    id_involved=selected_event[2]
    for involved in id_involved:
        tobeupdated.append(involved)
        nu,lu=neighbors(molecules,involved,nx,ny)
        for ii in lu:
            theindex=molecules.index(ii[1])
            if theindex not in tobeupdated:
                tobeupdated.append(theindex)

    for involved in id_involved:
        molecules[involved]=new_positions[theinvolved]
        theinvolved=theinvolved+1

    theinvolved=0
    for involved in id_involved:
        nu,lu=neighbors(molecules,involved,nx,ny)
        for ii in lu:
            theindex=molecules.index(ii[1])
            if theindex not in tobeupdated:
                tobeupdated.append(theindex)
        theinvolved=theinvolved+1

    i_shift = 0
    oldevents=list(possible_events)
    for i_oe, oe in enumerate(possible_events):
        for tu in tobeupdated:
            if tu in oe[2]:
                del oldevents[i_oe+i_shift]   
                i_shift -= 1
                break
    possible_events=list(oldevents)

#    oldevents=list(possible_events)
#    for oe in possible_events:
#        for tu in tobeupdated:
#            if tu in oe[2]:
#                oldevents.remove(oe)
#                break
#    possible_events=list(oldevents)

    return possible_events,tobeupdated