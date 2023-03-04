import math
import random

def box_muller(count):
	list_z1 = []
	list_z2 = []
	for i in range(0, count):
		u1 = random.uniform(0, 1)
		u2 = random.uniform(0, 1)
		z1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
		z2 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
		list_z1.append(z1)
		list_z2.append(z2)
	return list(zip(list_z1, list_z2))

def main():
	random_numbers = box_muller(200000)
	print(random_numbers)

if __name__ == "__main__":
	main()
