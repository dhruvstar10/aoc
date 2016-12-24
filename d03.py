# solution to d03 of aoc

# parse file in to list of triangles
triangleList = []
with open('d03_input') as f:
	triangleList.append([int(x) for x in next(f).split()]) # read first line
	for line in f:
		triangleList.append([int(x) for x in line.split()])

# procedure to return true if valid triangle, false otherwise
def checkTriangle(lengthList):
	l1 = lengthList[0]
	l2 = lengthList[1]
	l3 = lengthList[2]

	if l1 >= l2 + l3 or l2 >= l1 + l3 or l3 >= l1 + l2:
		return False
	else:
		return True

newTriangleList = []

## special procedure for part 2 to transform triangleList columnwise
for i in range(len(triangleList)):
	column = i%3	# column to pick lengths from
	row = i - column
	newTriangleList.append([triangleList[row][column], triangleList[row+1][column], triangleList[row+2][column]])

triangleList = newTriangleList

countTriangle = 0
for triangle in triangleList:
	if checkTriangle(triangle):
		countTriangle += 1

print countTriangle