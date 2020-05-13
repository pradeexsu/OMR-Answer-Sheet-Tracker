					##########################################
					#   Developed by  : Pradeep Suthar       #
					#   User          : sutharp777           #
					#   e-mail id	  : sutharp777@gmail.com #
					##########################################

import csv
#from os import system

#system('color 9')

class OMRset:
	def __init__(self,answeredTuple,totalQuetion=20):
    	self.answeredQuetions = answeredTuple
    	self.numberOfQuetions =totalQuetion
    	self.numberOfCorrect = 0
    	self.numberOfWrong = 0
    	self.numberOfUnattempt = self.numberOfQuetions

	def checkAnswer(self,answer,mark,negetivemark):
    	self.negetiveMark = negetivemark
    	self.mark = mark
    	for i in range(self.numberOfQuetions):
      		if self.answeredQuetions[i] == answer[i]:
        		self.numberOfCorrect += 1
        		self.numberOfUnattempt -= 1
        	# print(self.answeredQuetions[i],end=' ')
      		elif self.answeredQuetions[i] == '':
        		pass
      		else:
        		self.numberOfWrong += 1
        		self.numberOfUnattempt -= 1

  	def getResult(self):
		attempt = self.numberOfCorrect + self.numberOfWrong
		print( 'Attempt   : ', str(attempt).ljust(10))
		nu = str( self.numberOfUnattempt ).ljust(10)
		nc = self.numberOfCorrect
		nw = self.numberOfWrong
		print( 'Unattempt : ', nu)
		print( 'Correct   :  {} x {} \t {}'.formate( nc, self.mark, nc * self.mark))
		print( 'Wrong     :  {} x {} \t {}'.formate( nw, self.negetiveMark, nw * self.negetiveMark))
		print( 'Tota      :  ', nc * self.mark - nw * self.negetiveMark)

class OMR_Sheet:
	def __init__( self, numberOfQuetion, OMRNumber, answeredTuple, ans, mark, negetivemark):
		self.OMRN = OMRNumber
		self.mark = mark
		self.negetiveMark = negetivemark
		self.answerset = OMRset(answeredTuple,numberOfQuetion)
		self.answerset.checkAnswer(ans,mark,negetivemark)

	def showResult( self):
		print('OMR Sheet NUMBER : '.ljust(20), self.OMRN)
		self.answerset.getResult()

	
if __name__ == '__main__':
	omrSerialNUMMBER = 34500
	global omrSerialNUMMBER
	csv_file = open('./ans.csv', 'r')
	csv_data = csv.reader(csv_file)

	# n = int(input('enter the number of student (n<20):'))
	omrSerialNUMMBERCount, n, i = omrSerialNUMMBER, 3, 0
	student, ans = dict(), next(csv_data)
	
	msg = """	Select following Option
	  1. insert name
	  2. exit
	  3. show all 
	  """
	
	while True: 		
		print(msg)
	  	option = input()
	  	# system('cls')
	
	  	if option == '2':
	    	break
	  	elif option == '1':
	    	answeredTuple = next( csv_data)
			name = input( 'enter student name :')
			omrSerialNUMMBERCount += 1
			student[ name ] = OMR_Sheet( 20, omrSerialNUMMBERCount, answeredTuple, ans, 1, .25)
			print( 'name : ', name)
			student[ name].showResult()
	  	elif option == '3':
	    	for k in student:
	      		print('name  : ', k)
	      		student[k].showResult()		
		i += 1
		if i == n:
			break
