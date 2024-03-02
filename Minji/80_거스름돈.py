def solution(amount):
	lists = [100, 50, 10, 1]
	changes = []
	
	for c in lists:
		while amount >= c:
			changes.append(c)
			amount -= c

	return changes

assert solution(123) == [100, 10, 10, 1, 1, 1]
assert solution(350) == [100, 100, 100, 50]