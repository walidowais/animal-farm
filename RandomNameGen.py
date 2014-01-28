import random

with open('adjectives.txt') as f:
	adjectives = f.readlines()
	# f.close()
with open('animals.txt') as b:
	animals = b.readlines()
	# f.close()

	s1 = random.choice(adjectives).title()
	s2 = random.choice(animals)


	strpre = s1 + s2 
	strfinal = strpre.replace("\n", " ")
	print strfinal