import math, random, string

class PasswordGenerator():
	def __init__(self, minLength, maxLength, digitCount = -1, specialCount = -1):
		self.ascii = string.ascii_uppercase + string.ascii_lowercase
		self.digits = string.digits
		self.special = '!@#$%^&*-_'
		self.minLength = minLength
		self.maxLength = maxLength
		self.digitCount = digitCount
		self.specialCount = specialCount
		self.asciiCount = None
		self.__setup()

	def __setup(self):
		if self.minLength < 8:
			print('Minimum Password Length is low, setting to 8 characters')
			self.minLength = 8

		if self.maxLength > 40:
			print('Maximum Password Length is too high, setting to 40 characters')
			self.maxLength = 40

		if (self.digitCount == -1 and self.specialCount == -1):
			partCount = math.floor(0.25 * self.maxLength)
			self.digitCount, self.specialCount = partCount, partCount
		
		self.asciiCount = self.maxLength - (self.digitCount + self.specialCount)

	def generate(self):
		randomAscii = random.sample(self.ascii, self.asciiCount)
		randomDigits = random.sample(self.digits, self.digitCount)
		randomSpecial = random.sample(self.special, self.specialCount)

		combined = randomAscii + randomDigits + randomSpecial
		random.shuffle(combined)
		mixPassword = ''.join(combined)

		return mixPassword

def main():
	pwdGen = PasswordGenerator(8, 25) # (minimumLength, maximumLength)

	count = 0
	while count < 5:
		print(pwdGen.generate())
		count += 1
  
if __name__== "__main__":
	main()
	
