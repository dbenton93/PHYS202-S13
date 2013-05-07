import numpy as py
import math

def pointPotential(x,y,q,posx,posy):
    """Computes the electric potential from charge q at posx,posy and returns the potential at x,y"""
    k = 8.9875518e9
    return (k*q)/py.sqrt((x-posx)**2 + (y-posy)**2)



def dipolePotential(x,y,q,d):
     return pointPotential(x,y,q,-d,0) + pointPotential(x,y,-q,d,0)

def pointField(x,y,q,Xq,Yq):
    """Takes arrays, x and y, charge q, position Xq, Yq and returns components of electric field in the form (Ex,Ey)
    Ex = (k*q*(x-Xq))/(sqrt((x-Xq)**2+(y-Yq)**2))
    Ey = (k*q*(y-Yq))/(sqrt((x-Xq)**2+(y-Yq)**2))
    return (Ex,Ey)
