import random
import operator
from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import *
from functools import reduce
import copy

qvm = QVMConnection()
currentBest = []

def generateInitialPopulation(sizePopulation, nBits):
  population = []
  for i in range(sizePopulation):
    p = Program()
    for i in range(nBits):
      p += H(i)
    population.append(p)
  return population

def fitness(password, testWord):
  if len(password) == len(testWord):
    score = 0
    i = 0
    while i < len(password):
      if password[i] == testWord[i]:
        score += 1
      i += 1
    return score / len(password) * 100

def gradePopulation(qPop, password):
  population = copy.deepcopy(qPop)
  measuredPopulation = []
  for individual in population:
    runMeasurement = individual.measure_all()
    measurement = qvm.run(runMeasurement)
    measuredPopulation.append(''.join(map(str,measurement[0])))

  populationGrades = []
  for individual in measuredPopulation:
    populationGrades.append((individual, fitness(password, individual)))

  return sorted(populationGrades, key=lambda tup: tup[1], reverse=True)

def evolve(qPop, currentBest, theta):
  gates = []
  for i, bit in enumerate(currentBest):
    if bit == "0":
      gates.append(RY(-1 * theta, i))
    elif bit == "1":
      gates.append(RY(theta, i))

  for individual in qPop:
    for gate in gates:
      individual += gate

  return qPop

def mutatePopulation(population):
  return population

def runQuantumTrial(target, popSize, theta):
  qPop = generateInitialPopulation(popSize, len(target))
  p = gradePopulation(qPop, target)
  count = 0
  while p[0][0] != target:
    currentBest = p[0][0]
    qPop = evolve(qPop, currentBest, theta)
    #p = mutatePopulation(p)
    p = gradePopulation(qPop, target)
    count += 1
    if p[0][0] == target:
      break
  return count