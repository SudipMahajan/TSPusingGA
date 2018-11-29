import smodule as GA
import random as rm
import numpy as np
from itertools import product

n_cities = len(GA.graphofcities[1])
population = 10
n_iter = 10

print ("TSP graph created with number of cities:",n_cities)

# STEP 1
listofchromosomes = GA.initpopulation(population)

print ("\nPopulation Initialized to:",listofchromosomes,"count:",len(listofchromosomes))

for i in range(n_iter):

	print ("\n\n**** Iteration:",i)

	# STEP 2 & 3  PROPORTIONAL SELECTION of half population
	print ("listofchromosomes",listofchromosomes)
	fitnesslist = [i["cost"] for i in listofchromosomes]
	#print ("Fitness List:",fitnesslist)
	matingpoolsize = int(np.round(population/2))
	matingpool = GA.proportionalselection(listofchromosomes, matingpoolsize)
	print ("mating pool:",matingpool)
	#print ("\nReproduction population chosen , count:",len(mpool))

	# STEP 4 # Select a parent couple for applying cross-over operator
	# add logic select unique couples ONLY!!!!!
	parentlist = []
	for i, j in product(matingpool,matingpool):
		if(i!=j):
			parentlist.append([i,j])

	childlist = []

	#print ("\nFrom mating pool, parentcouple pairs selected for reproduction",parentlist ,"... count:",len(parentlist))

	for parentcouple in parentlist:

		#print ("\nParent couple under consideration:",parentcouple)
		# STEP 4: CROSSOVER operator on parents to generate offsprings
		assert (parentcouple[0]["tour"]!=parentcouple[1]["tour"]),parentcouple

		child = GA.crossover( parentcouple[0], parentcouple[1] )
		#print ("\nCross Over applied, child returned:",child)

		# STEP 5: APPLY mutation operator for changes
		child = GA.mutate(child)
		#print ("\nMutated children:",child)

		childlist.append(child)

	# end of inner for loop
	listofchromosomes[:] = childlist[:]

# end of outer for loop
finaltour = min(listofchromosomes, key = lambda x: x["cost"])
print ("\n\n****  After",n_iter,"Iterations, minimum cost tour:",finaltour["tour"],"with cost:",finaltour["cost"])
