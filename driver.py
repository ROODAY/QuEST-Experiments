def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    if iteration == total: 
        print()

from classical import runClassicalTrial
from quantum import runQuantumTrial
from randomGuess import runRandomTrial


N = 500
target = "101"
popSize = 10
theta = 0.2
mutateRate = 1
cT = []
qT = []
rT = []

print("Running random guessing trials...")
printProgressBar(0, N, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i in range(N):
    rT.append(runRandomTrial(target, popSize))
    printProgressBar(i + 1, N, prefix = 'Progress:', suffix = 'Complete', length = 50)

rAvg = sum(rT) / float(len(rT))
print("Average generations for random guessing:", rAvg)

print("\nRunning classical EA trials...")
printProgressBar(0, N, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i in range(N):
    cT.append(runClassicalTrial(target, popSize, mutateRate))
    printProgressBar(i + 1, N, prefix = 'Progress:', suffix = 'Complete', length = 50)

cAvg = sum(cT) / float(len(cT))
print("Average generations for classical EA:", cAvg)

print("\nRunning quantum EA trials...")
printProgressBar(0, N, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i in range(N):
    qT.append(runQuantumTrial(target, popSize, theta))
    printProgressBar(i + 1, N, prefix = 'Progress:', suffix = 'Complete', length = 50)

qAvg = sum(qT) / float(len(qT))
print("Average generations for quantum EA:", qAvg)