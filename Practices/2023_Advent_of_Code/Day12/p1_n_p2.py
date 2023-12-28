# First time to look up codes :p
# but learnt alot about DP
import re

def combinator(line:str, nums:tuple, part1=True):
	if part1 == False:
		line = "?".join([line]*5)
		nums *= 5

	DP:dict = {}

	def f(i:int, n:int, b:int) -> int: # return how many solutions there are from this position
		# i - index in line
		# n - index in nums
		# b - size of current block
		if (i,n,b) in DP:return DP[(i,n,b)] # Caching already solved it
		
		if i == len(line):	# at the end of the line, return 1 if this is a posible configuration or 0 otherwise
			return int(
				n == len(nums) and b == 0 or 			# no current block, and finished all numbers
				n == len(nums)-1 and b == nums[-1]		# one last block, and currently in a block of that size
			)

		ans = 0
		if line[i] in ".?":	# treat it like a .
			if(b == 0):
				ans += f(i+1, n, 0) # just keep moving forward
			else:			# we have a current block
				if n == len(nums): return 0	# more springs than input asks for, so not a solution
				if b == nums[n]: 			# If we currently have a continguous spring of the required size
					ans += f(i+1, n+1, 0)	# Move forward and count this block

		if line[i] in "#?": # treat it like a #
			ans += f(i+1, n, b+1) 	# no choice but to continue current block
		DP[(i,n,b)] = ans # cache it
		return ans
	
	return f(0,0,0)


if __name__ == "__main__":
	puzzle_input: list[str]
	with open("input.txt", "r") as file:
		puzzle_input = file.read().split("\n")
	
	res1:int = 0
	res2:int = 0
	for line in puzzle_input:
		springs, goal = line.split(" ")
		springs = re.sub(r"\.+", ".", springs)
		goal = eval(goal) # returns the string as a tuple
		
		res1 += combinator(springs, goal)
		res2 += combinator(springs, goal, False)
	print(res1, res2)