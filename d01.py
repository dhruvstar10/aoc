# solution to Day 1 of December in Advent of Code
input = "L5, R1, R4, L5, L4, R3, R1, L1, R4, R5, L1, L3, R4, L2, L4, R2, L4, L1, R3, R1, R1, L1, R1, L5, R5, R2, L5, R2, R1, L2, L4, L4, R191, R2, R5, R1, L1, L2, R5, L2, L3, R4, L1, L1, R1, R50, L1, R1, R76, R5, R4, R2, L5, L3, L5, R2, R1, L1, R2, L3, R4, R2, L1, L1, R4, L1, L1, R185, R1, L5, L4, L5, L3, R2, R3, R1, L5, R1, L3, L2, L2, R5, L1, L1, L3, R1, R4, L2, L1, L1, L3, L4, R5, L2, R3, R5, R1, L4, R5, L3, R3, R3, R1, R1, R5, R2, L2, R5, L5, L4, R4, R3, R5, R1, L3, R1, L2, L2, R3, R4, L1, R4, L1, R4, R3, L1, L4, L1, L5, L2, R2, L1, R1, L5, L3, R4, L1, R5, L5, L5, L1, L3, R1, R5, L2, L4, L5, L1, L1, L2, R5, R5, L4, R3, L2, L1, L3, L4, L5, L5, L2, R4, R3, L5, R4, R2, R1, L5"

# convert input string into a list
input = input.split(", ")
# starting direction is north
starting_dir = "N"

# mapping how right or left would change starting direction to new direction
turn_map = 	{
			"N":{"R":"E", "L":"W"},
			"E":{"R":"S", "L":"N"},
			"S":{"R":"W", "L":"E"},
			"W":{"R":"N", "L":"S"},
		}

# track steps in each direction
steps_tracker = {"N":0, "E":0, "S":0, "W":0}
# current direction tracker
curr_dir = starting_dir

# going through instructions
for instruction in input:
	# separate the instruction pieces
	turn = instruction[0]
	steps = int(instruction[1:])
	# find the new current direction
	curr_dir = turn_map[curr_dir][turn]
	# add steps to sum in correct direction
	steps_tracker[curr_dir] += steps

x_steps = steps_tracker["E"] - steps_tracker["W"]
y_steps = steps_tracker["N"] - steps_tracker["S"]
distance = abs(x_steps) + abs(y_steps)

print distance


# Note: more elegant way of doing it: realizing that every other instruction is along the same axis. i.e. instructions 0, 2, 4 etc. are along X-axis and instructions 1, 3, 5 etc. are along Y-axis. Then you just keep track of steps in either direction and add them up later. Would have been less readable, more confusing to code, and would be same O(n) in input size.