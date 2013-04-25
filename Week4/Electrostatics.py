import numpy as py

def pointPotential(x,y,q,posx,posy):
    """Computes the electric potential from charge q at posx,posy and returns the potential at x,y"""
    k = 8.9875518e9
    return (k*q)/py.sqrt((x-posx)**2 + (y-posy)**2)



def dipolePotential(x,y,q,d):
     return pointPotential(x,y,q,-d,0) + pointPotential(x,y,-q,d,0)

