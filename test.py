def hello():
	print('hello')

hello()

def pack(one, two, three):
	return [one, two, three]

print(pack('python', 'is', 'cool'))

def eat_lunch(food_list):
	for food in food_list:
		if food == food_list[0]:
			print(f'I eat {food}')
		else:
			print(f'Then I eat {food}')

eat_lunch(['Apple', 'Burger', 'Sandwich'])
