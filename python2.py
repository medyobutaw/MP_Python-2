import numpy as np
import math as mt
    
x1 = float(input('Enter the first point in the x-axis: '))
y1 = float(input('Enter the first point in the y-axis: '))
x2 = float(input('Enter the second point in the x-axis: '))
y2 = float(input('Enter the second point in the y-axis: '))
x3 = float(input('Enter the third point in the x-axis: '))
y3 = float(input('Enter the third point in the y-axis: '))

def python2(x1,y1,x2,y2,x3,y3):
    
    X1 = (x1**2) + (y1**2)
    X2 = (x2**2) + (y2**2)
    X3 = (x3**2) + (y3**2)

    c = np.array([(x1,y1,1),(x2,y2,1),(x3,y3,1)])
    C = np.linalg.det(c)

    d = -np.array([(X1,y1,1),(X2,y2,1),(X3,y3,1)])
    D = np.linalg.det(d)

    e = np.array([(X1,x1,1),(X2,x2,1),(X3,x3,1)])
    E = np.linalg.det(e)

    f = -np.array([(X1,x1,y1),(X2,x2,y2),(X3,x3,y3)])
    F = np.linalg.det(f)

    h = -(D/(C*2))
    k = -(E/(C*2))
    r = mt.sqrt(((x1-h)**2)+((y1-k)**2))

    Dc = D/C
    Ec = E/C
    Fc = F/C
    
    print('Center(h,k): (',round(h),',',round(k),')')
    print('Radius(r): ',round(r),'')
    print('Vector[D,E,F]:[',round(Dc),',',round(Ec),',',round(Fc),']')

python2(x1,y1,x2,y2,x3,y3)