import random
import operator

def generateBitString(length):
  result = ""
  while len(result) < length:
    letter = str(round(random.random()))
    result += letter
  return result

def generateInitialPopulation(sizePopulation, password):
  population = []
  i = 0
  while i < sizePopulation:
    population.append(generateBitString(len(password)))
    i += 1
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

def gradePopulation(population, password):
  populationGrades = []
  for individual in population:
    populationGrades.append((individual, fitness(password, individual)))
  return sorted(populationGrades, key=lambda tup: tup[1], reverse=True)

def evolve(sortedPopulation):
  retain_length = int(len(sortedPopulation)*.2)
  nextGeneration = sortedPopulation[:retain_length]

  for individual in sortedPopulation[retain_length:]:
    if 0.05 > random.random():
      nextGeneration.append(individual)
  random.shuffle(nextGeneration)
  return nextGeneration

def createChild(individual1, individual2):
  child = ""
  for i in range(len(individual1)):
    if (int(100 * random.random()) < 50):
      child += individual1[i]
    else:
      child += individual2[i]
  return child

def createChildren(parents, numChildren):
  nextPopulation = []
  while len(nextPopulation) < numChildren:
    parent1 = random.randint(0, len(parents)-1)
    parent2 = random.randint(0, len(parents)-1)
    if parent1 != parent2:
      nextPopulation.append(createChild(parents[parent1][0], parents[parent2][0]))
  return nextPopulation

def mutateWord(word):
  index = int(random.random() * len(word))
  if index == 0:
    word = str(round(random.random())) + word[1:]
  else:
    word = word[:index] + str(round(random.random())) + word[index+1:]
  return word

def mutatePopulation(population):
  for i in range(len(population)):
    if random.random() < 0.01:
      population[i] = mutateWord(population[i])
  return population


def runClassicalTrial(target, popSize):
  p = gradePopulation(generateInitialPopulation(popSize, target), target)
  count = 0
  while p[0][0] != target:
    p = evolve(p)
    p = createChildren(p, popSize)
    p = mutatePopulation(p)
    p = gradePopulation(p, target)
    count += 1
    if p[0][0] == target:
      break
  return count