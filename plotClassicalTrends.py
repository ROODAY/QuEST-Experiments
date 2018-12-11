def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    if iteration == total: 
        print()

from classical import runClassicalTrial
from quantum import runQuantumTrial
import matplotlib.pyplot as plt


N = 500
target = "10101"
popSize = 10
theta = 0.01
mutateRate = 0.01
mutateRates = [0.01, 0.05, 0.1, 0.2, 0.5, 1]
targets = ["101", "1001", "10101", "101101", "1010101"]
cAvgs = []

cT = []
qT = []


for rate in mutateRates:
    print("\nRunning classical trials for m = " + str(rate) + "...")
    printProgressBar(0, N, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i in range(N):
        cT.append(runClassicalTrial(target, popSize, rate))
        printProgressBar(i + 1, N, prefix = 'Progress:', suffix = 'Complete', length = 50)

    cAvg = sum(cT) / float(len(cT))
    print("Average generations for classical (m = " + str(rate) + "): " + str(cAvg))
    cAvgs.append(cAvg)

plt.figure(1)
plt.plot(mutateRates, cAvgs, '-o')
plt.xticks([0.01, 0.1, 0.2, 0.5, 1])
plt.xlabel('Mutation Rate')
plt.ylabel('Generations to Converge')
plt.title('Generations till convergence at  "10101" for Classical EA')
plt.savefig('classicalEAbyMR.png')

tAvgs = []
for tar in targets:
    print("\nRunning classical trials for target = " + str(tar) + "...")
    printProgressBar(0, N, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i in range(N):
        cT.append(runClassicalTrial(tar, popSize, mutateRate))
        printProgressBar(i + 1, N, prefix = 'Progress:', suffix = 'Complete', length = 50)

    cAvg = sum(cT) / float(len(cT))
    print("Average generations for classical (target = " + str(tar) + "): " + str(cAvg))
    tAvgs.append(cAvg)

print("Spread: " + str(tAvgs[-1] - tAvgs[0]))

plt.figure(2)
plt.plot([len(tar) for tar in targets], tAvgs, '-o')
plt.xticks([len(tar) for tar in targets])
plt.xlabel('Target Length')
plt.ylabel('Generations to Converge')
plt.title('Generations till convergence for Classical EA')
plt.savefig('classicalEAbyTarget.png')