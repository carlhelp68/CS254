def dfa(M, w):
	current_position = M[3]
	transition_function = M[2]
	for char in w:
		# Check to see if char is in alphabet, if not reject string
		if char in M[1]:
			current_position = transition_function[current_position, char]
		else:
			return False
	# If q0 there were an even number of 1's so return False
	if current_position == "q0":
		return False
	return True

def main():
	delta = {("q0", "0"):"q0", ("q0", "1"):"q1", ("q1", "0"):"q1", ("q1", "1"):"q0"}
	m = (("q0", "q1"), ("0", "1"), delta, "q0", ("q1",))
	print(dfa(m, "010"))

if __name__ == '__main__':
    main()

