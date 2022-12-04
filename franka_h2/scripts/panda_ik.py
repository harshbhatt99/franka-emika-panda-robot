import math
from spatialmath.base import *
from spatialmath import SE3
import spatialmath.base.symbolic as sym
import numpy as np

import roboticstoolbox as rtb


panda = rtb.models.URDF.Panda()
print(panda)

T = panda.fkine(panda.qz, end='panda_hand')
print(T)

point = SE3(0.6,-0.5,0.0)
point_sol = panda.ikine_LM(point)
print("IK Solution: ",point_sol)

