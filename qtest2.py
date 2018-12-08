from pyquil.quil import Program
from pyquil.api import QVMConnection
from collections import Counter
from pyquil.gates import *
import math

qvm = QVMConnection()
#p = Program(X(0), I(1), X(2), I(3), X(4))
p = Program()
p += H(0)
p += RY(-math.pi/4,0)
#p += RX(math.pi/2, 0)
#p += RZ(math.pi/4, 0)
p += H(0)
p += RY(-math.pi/4,0)
p += H(0)
measure = p.measure_all()
result = qvm.run(measure, trials=1000)
res = [x[0] for x in result]
print(Counter(res))