
def test(*args):

	res = 0
	for i in args:
		res += i
	print(res)

numbers = [1, 2, 3]
test(*numbers)
