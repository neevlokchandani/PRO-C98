print('file word counter')
def counter():
	file_name = input('file name:- ')
	file = open(f'{file_name}.txt')
	line = 0
	lenght = 0
	no_of_line = file.readlines()
	for line in no_of_line:
		words = line.split(' ')
		lenght += len(words)
	print(f'lenght:- {lenght}')

counter()