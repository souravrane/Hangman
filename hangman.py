import json as js
import random as rn
import sys 
import re

while True:
	print("\n HANGMAN \n")
	f = open("words.json",'r')
	a = js.loads(f.read())
	r=rn.randrange(len(a['words']))

	hint=list(a['words'][r]["hint"])
	hintstr=a['words'][r]["hint"]
	question=a['words'][r]["question"]
	ans=list(a['words'][r]["answer"])

	temp1=[m.start() for m in re.finditer('_',hintstr)]
	temp2=[]
	for i in temp1:
		temp2.append(ans[i])

	chance = 5
	
	while chance:
		print("No of Trys left : ",chance)
		print("\n QN : ",question)
		print("Guess : ",hint)
		ch=input("	Enter your Guess .... ")
		if ch in temp2:
			print("	A Good guess !..")
			for i in range(len(temp2)):
				if temp2[i]==ch:
					hint[temp1[i]]=ch
			chance-=1
		else:
			print("	Oops ! Wrong one ..")
			chance-=1
		if '_' not in hint:
			print("Guess : ",hint)
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







	


