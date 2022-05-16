'''
The function takes 3 arguments: a string and two symbols. 
It searches a greatest index of every symbol. 
Returns -1 if there are not those symbols in the string.
'''

def max_ind(line: str, sx: str, sy: str) -> int:
	l = []
	for z in sx, sy:
		l += [a for a in range(len(line)) if line[a] == z]
	try:
		return sorted(l)[-1]
	except IndexError:
		return -1

print(max_ind('Python code to demonstrate', 'o', 't'))
print(max_ind('Python code to demonstrate', 'ж', 'ы'))
print(max_ind('Python code to demonstrate', 'h', 'ы'))
print(max_ind('Python code to demonstrate', 'ж', 's'))

# Output:
# 24
# -1
# 3
# 20
