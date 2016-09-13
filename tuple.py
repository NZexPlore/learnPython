class GameLexicon(object):
	def __init__(self):
		pass
	def include_words(self, words_list):
		self.words_list = words_list
	def words_count(self):
		try:
			self.words_count = len(self.words_list)
			return self.words_count
		except ValueError:
			pass
	def word_check(self, input_word):
		try:
			for word_temp in self.words_list:
				if input_word == word_temp:
					check_flag = True
					return check_flag
				else:
					check_flag = False
			return False
		except ValueError:
			print "Please put a word as snytax."

class InputSentence(object):
	def __init__(self):
		self.valid_direction = False
		self.valid_verb = False
		self.valid_stop = False
		self.valid_noun = False
		self.valid_number = False
	def get_words(self, sentence):
		self.words = sentence.split(' ')
	def words_match(self):
		for word_temp in self.words:
			if instDirectionWords.word_check(word_temp) == True:
				self.directionword = word_temp
				self.valid_direction = not self.valid_direction
			elif instVerb.word_check(word_temp) == True:
				self.verb = word_temp
				self.valid_verb = not self.valid_verb
			elif instStopWords.word_check(word_temp) == True:
				self.stopword = word_temp
				self.valid_stop = not self.valid_stop
			elif instNouns.word_check(word_temp) == True:
				self.noun = word_temp
				self.valid_noun = not self.valid_noun
			elif instNumbers.word_check(word_temp) == True:
				self.number = word_temp
				self.valid_number = not self.valid_number
			else:
				pass
		if self.valid_direction:
			return self.directionword
		elif self.valid_verb:
			return self.verb
		elif self.valid_stop:
			return self.stopword
		elif self.valid_noun:
			return self.noun
		elif self.valid_number:
			return self.number
		else:
			print "Invalid Instruction."
			new_commander = Commander()
			new_commander.play()
			return new_commander.instruction
			
class Commander(object):
	def __init__(self):
		print "Welcome aboard, Sir."
	def play(self):
		print 'Please make your order'
		self.new_order = raw_input('=> ')
		instInputsentence = InputSentence()
		instInputsentence.get_words(self.new_order)
		self.instruction = instInputsentence.words_match()
			
DirectionWords = ['north', 'south', 'east', 'west',
				  'down', 'up', 'left', 'right', 'back'
				 ]
Verbs = ['go', 'stop', 'kill', 'eat']
StopWords = ['the', 'in', 'of', 'from', 'at', 'it']
Nouns = ['door', 'bear', 'princess', 'cabinet']
Numbers = "0 1 2 3 4 5 6 7 8 9"
Numbers = Numbers.split()

instDirectionWords = GameLexicon()
instDirectionWords.include_words(DirectionWords)
instVerb = GameLexicon()
instVerb.include_words(Verbs)
instStopWords = GameLexicon()
instStopWords.include_words(StopWords)
instNouns = GameLexicon()
instNouns.include_words(Nouns)
instNumbers = GameLexicon()
instNumbers.include_words(Numbers)

instPlayer = Commander()
instPlayer.play()
print instPlayer.instruction