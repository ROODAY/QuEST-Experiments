from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import H
from functools import reduce

qvm = QVMConnection()
dice = Program(H(0), H(1), H(2))
roll_dice = dice.measure_all()
result = qvm.run(roll_dice)

dice_value = reduce(lambda x, y: 2*x + y, result[0], 0) + 1
print("Your quantum dice roll returned:", dice_value)