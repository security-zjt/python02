class Student:
	def __init__(self, std):
		self.count = std
		print(std)

	def print_std(self):
		for i in range(self.count):
			print(i)
		return

if __name__ == '__main__':
	Student(6).print_std()

