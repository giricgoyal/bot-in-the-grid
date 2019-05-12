import queue

pairs = [(5, 5), (6, 6), (9, 7)]

def get_shortest_path(pointA, pointB):
	dx = abs(pointA[0] - pointB[0])
	dy = abs(pointA[1] - pointB[1])

	return max(dx, dy)

def main():
	stepCount = 0

	for i in range(len(pairs) - 1):
		stepCount += get_shortest_path(pairs[i], pairs[i + 1])

	print(stepCount)


if __name__ == "__main__":
	main()