class Animal(object):
	def __init__(self,name,species,age,favorite_color):
		self.name = name
		self.name = species
		self.age= age
		self.favorite_color = favorite_color

class Cat(Animal):
	def meow(self, sound):
		print(sound +"!"+ " hello, my name is " + self.name)
	
tommy = Cat(name ="tommy", species = "Cat", age = "17", favorite_color="blue")
tommy.meow("meow")


##################


class Animal(object):
	def __init__(self,name,species,age,favorite_color):
		self.name = name
		self.name = species
		self.age= age
		self.favorite_color = favorite_color

class bird(Animal):
	def fly(self, sound):
		print(sound +"!"+ " hello i can fly")
	
Balbo = bird(name ="Balbo", species= "bird", age = "3", favorite_color="white")
Balbo.fly("queek")


#################


class Animal(object):
	def __init__(self,name,species,age,favorite_color):
		self.name = name
		self.name = species
		self.age= age
		self.favorite_color = favorite_color

class chicken(Animal):
	def fly(self, sound):
		print(sound +"!"+ " hello i can't fly")
	
fatima = chicken(name ="fatima", species= "chicken", age = "3", favorite_color="white")
fatima.fly("kook")

####################

class Animal(object):
	def __init__(self,name,species,age,favorite_color):
		self.name = name
		self.name = species
		self.age= age
		self.favorite_color = favorite_color

class dove(Animal):
	def hefhef(self, sound):
		print(sound +"!"+ " hello i have limbs")
	
zaher = dove(name ="zaher", species= "dove", age = "8", favorite_color="green")
zaher.hefhef("hefhef")

#####################

class Animal(object):
	def __init__(self,name,species,age,favorite_color):
		self.name = name
		self.name = species
		self.age= age
		self.favorite_color = favorite_color

class fish(Animal):
	def blubblub(self, sound):
		print(sound +"!"+ " hello I'm rasmeye, I boil water because I'm hot")
	
rasmeye = fish (name ="rasmeye", species= "fish", age = "10", favorite_color="black")
rasmeye.blubblub("blubblub")