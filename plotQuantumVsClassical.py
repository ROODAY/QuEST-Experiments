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
import matplotlib.pyplot as plt
import statistics


N = 500
popSize = 10
theta = 0.2
mutateRate = 0.01
targets = ["101", "1001", "10101", "101101", "1010101"]
cAvgs = []
qAvgs = []
rAvgs = []

cSTD = []
qSTD = []
rSTD = []

for tar in targets:
    rT = []
    print("\nRunning random guessing trials for target = " + str(tar) + "...")
    printProgressBar(0, N, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i in range(N):
        rT.append(runRandomTrial(tar, popSize))
        printProgressBar(i + 1, N, prefix = 'Progress:', suffix = 'Complete', length = 50)

    rAvg = sum(rT) / float(len(rT))
    print("Average generations for random guessing (target = " + str(tar) + "): " + str(rAvg))
    rAvgs.append(rAvg)
    rSTD.append(statistics.stdev(rT))
    print(rT[:99])
    

    cT = []
    print("\nRunning classical trials for target = " + str(tar) + "...")
    printProgressBar(0, N, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i in range(N):
        cT.append(runClassicalTrial(tar, popSize, mutateRate))
        printProgressBar(i + 1, N, prefix = 'Progress:', suffix = 'Complete', length = 50)

    cAvg = sum(cT) / float(len(cT))
    print("Average generations for classical (target = " + str(tar) + "): " + str(cAvg))
    cAvgs.append(cAvg)
    cSTD.append(statistics.stdev(cT))
    print(cT[:99])

    qT = []
    print("\nRunning quantum trials for target = " + str(tar) + "...")
    printProgressBar(0, N, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i in range(N):
        qT.append(runQuantumTrial(tar, popSize, theta))
        printProgressBar(i + 1, N, prefix = 'Progress:', suffix = 'Complete', length = 50)

    qAvg = sum(qT) / float(len(qT))
    print("Average generations for quantum (target = " + str(tar) + "): " + str(qAvg))
    qAvgs.append(qAvg)
    qSTD.append(statistics.stdev(qT))
    print(qT[:99])

import csv




with open('data.csv', mode='w') as datafile:
    filewriter = csv.writer(datafile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Target', 'Random Guess Avg', 'Random Guess Stddev', 'EA (M = 0.01) Avg', 'EA Stddev', 'QEA (T = 0.2) Avg', 'QEA Stddev'])

    for i in range(len(targets)):
        filewriter.writerow([targets[i], rAvgs[i], rSTD[i], cAvgs[i], cSTD[i], qAvgs[i], qSTD[i]])



lens = [len(tar) for tar in targets]
plt.figure(1)
plt.plot(lens, rAvgs)
plt.plot(lens, cAvgs)
plt.plot(lens, qAvgs)
plt.legend(['Random Guessing', 'Classical EA', 'Quantum EA'], loc='upper left')
plt.xticks(lens)
plt.xlabel('Target Length')
plt.ylabel('Generations to Converge')
plt.title('Comparing Generations till Convergence for EA vs. QEA')
plt.savefig('qeaVSeaByTarget.png')