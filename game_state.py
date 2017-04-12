class GameState(object):
	"""Game State object"""
	def __init__(self):
		self.border = "="*80
		self.name = "default state"

	def __str__(self):
		return self.border + "\n" + self.name + "\n"

	def tick(self):
		input(self)
		return self

class BattleScreen(GameState):
	"""docstring for BattleScreen."""
	def __init__(self, chars=["Ron"], enemies=["Goblin"], location="default"):
		super(BattleScreen, self).__init__()
		self.name = "BATTLE"
		self.chars = chars
		self.enemies = enemies
		self.location = location

	def __str__(self):
		output = super(BattleScreen, self).__str__()
		output += "Location: {}\nENEMIES:\n".format(self.location)
		for i in self.enemies:
			output += "{}\t".format(i)
		output += "\nPARTY:\n"
		for i in self.chars:
			output += "{}\t".format(i)
		output += "\n"
		return(output)

class StartScreen(GameState):
	"""Object for start start screen"""

	def __init__(self):
		super(StartScreen, self).__init__()
		self.name = "Main Menu"
		self.startMenu = ("1 - New Game\n"
						  "2 - Load Game\n"
						  "3 - Options\n"
						  "4 - Exit\n")

	def __str__(self):
		output = super(StartScreen, self).__str__()
		output += self.startMenu
		return output

	def tick(self):
		#try:
			answer = int(input(self))
			if answer == 1:
				return BattleScreen()
			elif answer == 2:
				return BattleScreen(chars=["Ron", "Jeremy"])
			elif answer == 3:
				return OptionScreen()
			elif answer == 4:
				return None
			else:
				return self
		#except:
			return self
