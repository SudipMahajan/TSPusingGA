import random as rm
import numpy as np


graphofcities = [[0, 2, 2, 5, 7],
                 [2, 0, 4, 1, 2],
                 [2, 4, 0, 1, 3],
                 [5, 1, 1, 0, 2],
                 [7, 2, 3, 2, 0]]
                 # Optimum tour: 0-1-4-3-2-0 cost: 9

def initpopulation(population):
	n_cities = len(graphofcities[1])
	listofchromosomes = []

	for i in range(population):
		tour = rm.sample(range(0,n_cities),n_cities)

		listofchromosomes.append( { "tour":tour,"cost":calcTourCost(tour) })   # cost acts like fitness for every chromosome

	return listofchromosomes


def calcTourCost(toursequence):
	tourcost = 0

	for i in range(len(toursequence)-1):
		# print (graphofcities[ toursequence[i] ][ toursequence[i+1] ])
		tourcost = tourcost + graphofcities[ toursequence[i] ][ toursequence[i+1] ]

	tourcost = tourcost + graphofcities[ toursequence[-1] ][ toursequence[0] ]          # to complete the cycle
	return tourcost


def proportionalselection(listofchromosomes,mpsize):
	sortedlist = sorted(listofchromosomes, key = lambda x:x["cost"],reverse = False)
	
	return sortedlist[0:mpsize]


def crossover(parent1, parent2):
	#print ("Parents inside crossover function:", parent1, parent2)
	p1 = parent1["tour"]
	p2 = parent2["tour"]
	o=[]
	index1= rm.randint(1,len(p1)-2)
	index2= p2.index(p1[index1])
	o.append(p1[index1])
	#print ("first append",o)
	index1 += 1
	index2 -= 1

	while (len(o)!=len(p1) and index1<len(p1) and index2<len(p2)):
		if (p1[index1] not in o):							#'d','c','i','b','a','h','g','e','f','k','l','m','n','o','j'	
																	                            #   <-------- #
															#'g','f','l','o','m','k','n','e','d','j','i','c','b','h','a'		
			
			o.append(p1[index1])
			#print ("o:",o)
			index1 += 1

		else:
			break

		if (p2[index2] not in o) and (index2>=0):	
			o.insert(0, p2[index2])
			#print ("o:",o)

			index2 -= 1

		else:
			break

	o.extend(list(set(p1) - set(o)))
	o = {'tour':o,'cost':calcTourCost(o)}
	return o


def mutate(child):
	indices2swap = rm.sample( range(len(child)), 2 )
	child["tour"][ indices2swap[0] ], child["tour"][ indices2swap[1] ] = child["tour"][ indices2swap[1] ], child["tour"][ indices2swap[0] ]
	child["cost"] = calcTourCost(child["tour"])
	return child
