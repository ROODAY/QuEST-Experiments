# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

from classical import runClassicalTrial



N = 1000
target = "10101"
popSize = 10
cT = []
qT = []

print("Running classical trials...")
printProgressBar(0, N, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i in range(N):
    cT.append(runClassicalTrial(target, popSize))
    printProgressBar(i + 1, N, prefix = 'Progress:', suffix = 'Complete', length = 50)

cAvg = sum(cT) / float(len(cT))
print("Average generations for classical:", cAvg)