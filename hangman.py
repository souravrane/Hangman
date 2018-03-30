import json as js
import random as rn
import sys 
import re

while True:
	print("\n HANGMAN \n")
	f = open("words.json",'r')
	a = js.loads(f.read())
	r=rn.randrange(len(a['words']))					#chooses a random word from the set of words

	hint=list(a['words'][r]["hint"])				#hint					
	hintstr=a['words'][r]["hint"]
	question=a['words'][r]["question"]				#corresponding question to guess the answer
	ans=list(a['words'][r]["answer"])				#the correct answer

	temp1=[m.start() for m in re.finditer('_',hintstr)]		#regex to find the locations of blank areas to fill in
	temp2=[]													
	for i in temp1:
		temp2.append(ans[i])					#stores the corresponding true value of the blank obtained from regex

	chance = 5							#trials
	
	while chance:
		print("No of Trys left : ",chance)
		print("\n QN : ",question)
		print("Guess : ",hint)
		ch=input("	Enter your Guess .... ")
		if ch in temp2:
			print("	A Good guess !..")
			for i in range(len(temp2)):
				if temp2[i]==ch:
					hint[temp1[i]]=ch 		#checking for the existence of the letter in the answer
			chance-=1					#and inserting it if true
		else:
			print("	Oops ! Wrong one ..")
			chance-=1
		if '_' not in hint:
			print("Guess : ",hint)				#break if all blanks are filled
			break

	if '_' not in hint:
		print("\n	WELL DONE ! YOU HAVE SAVED THE MAN !")
	else:
		print("\n	R.I.P -_- YOU LOSE!!!")

	choice=input("	New Game ? ... press 'Y' or 'N' :- ")
	if choice == 'y' or choice == 'Y':
		print("	Restart...\n")
		continue
	else:
		sys.exit()







	


