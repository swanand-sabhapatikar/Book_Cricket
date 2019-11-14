#There is no separete exception script made for the program. exceptions are handled in this script itself
#The program will terminate itself afte a successful / interupted execution. To execute it again, run the file again

#import --START--

import time
import random
import subprocess as sub
from sys import exit

#import --END--

#Global variables --START--

Team=[] #will hold names of team

typeOfMatch=["2 overs, 1 Players in each team" ,[2,1],
             "4 overs, 3 Players in each team" ,[4,3],
             "6 overs, 5 Players in each team" ,[5,6],
	     "8 overs, 7 Players in each team" ,[8,7]]
totalRun={} #will hold runs of each team

#Global variables --START--

#Following fuction depicts rules for the game
#(gameRule.__doc__) or DocString is used to print rules
def gameRule():
	
	"""Hi Folks Following are Rules for this Game.
	1. ONLY 2 players can play at a time Team 1 and Team 2, One will bat* and other will bowl*
	NOTE: if it is your 1st time go for 1st choice
	2. bat* : The batting team will be the active one, 
	4. Bowl*: The bowling team will have just 1 job, to watch batting team and pray that oppnent will be all out soon

	"""

#
def selectType():
	strt="""We have 4 types from which you can choose.
		0: 2 overs, 1 Players in each team
		2: 4 overs, 3 Players in each team
		4: 6 overs, 5 Players in each team
		6: 8 overs, 7 Players in each team, select any one.
	"""
	#print(strt)
	ch=str(input(">>"))
	while True:
		type(ch)
		if ch.isdigit()==True:
			if ch not in ["0","2","6","4"]:
				#raise
				print("invalid input select again")
				print(strt)
				ch=str(input(">>"))
			else:
				return int(ch)
				break
		else:
			#Raise
			print("only inter values accepted ")
			selectType()	


# Following functions does following things:
# 1.takes names of  two team
# 2.decides which team will take the toss and also who wins the toss
# 3.returns the team name who won the toss
def getInput():
	global Team
	#getting first team name 
	print("enter 1st team Name")
	Team1=str(input(">>"))
	
	#getting second team name
	print("enter 2nd  team Name")
	Team2=str(input(">>"))
	
	#List contain team names 
	Team=[Team1,Team2]
	
	#print names 
	print("so Team1:{} and Team2:{}, Lets toss".format(Team1,Team2))
	time.sleep(1)

	# Toss mechanism
	# Here random module is used to generate real time random feature of toss
	# The team who wins the toss, will bat first		
	#--selecting team who will call the toss
	print("lets see who will take the call")
	time.sleep(1)
	
	no=random.randint(0,1) # 0: Team 1 and 1: team 2
	Team_That_takes_call=Team[no]
	print("and the call goes to:{}".format(Team_That_takes_call))
	
	#code for Head or Tails 
	print("select h:Head or t: Tails ")
	H_or_t=str(input(">>")).upper()

	while True:
		
		if H_or_t not in ["H","T"]:
			#raise
			print("invalid ip")
			print("select h:Head or t: Tails ")
			H_or_t=str(input(">>")).upper()
		else:
			#ramdom module used to select between H and T
			TossValue=random.choice(["H","T"])
			print(TossValue)
			if H_or_t==TossValue:
				print("Bravooooooooooo Team {}, you win the toss ".format(Team[no]))
				print("you will bat first")

			if H_or_t!=TossValue:
				print("Oh shit!!! Team {}, you lost".format(Team[no]))
				if no==0:
					no=1
				else:
					no=0
				print("team {} won the toss awesomeeeee".format(Team[no]))
				print("you will bat first")
			
			return no		
			break	

#Following funciton will stimulate the game play according to the type of match selected.
#Radom module is used to deliver hits:0,1,2,3,4,6,8,9
#when the player hits enter, the random.choice method will will ramdomly select any value with random co-incidence.
#no extra ball are added for NO Ball(8) or Wide ball(9) but extra 1 run is added to the score
def playMatch(matchType,teamName):
	
	print(matchType)
	overs,playerPerTeam=matchType
	overs=int(overs)
	playerPerTeam=int(playerPerTeam)
	totalBalls=int(overs)*6
	noOfPlayer=int(playerPerTeam)
	print("batting team Name:",Team[teamName])
	Runs=0
	#code for counting overs 
	while totalBalls>=0 or noOfPlayer!=0:
		if totalBalls==(-1):
			break

		#to check overs
		if (totalBalls%6)==0:
			overs-=1

		print("Runs       :",Runs)
		print("balls left :",totalBalls)
		print("no of Player left:",noOfPlayer)
		print("hit enter when ready")
		enttr=input(">>")
		if enttr !='':
				#raise
				print ("invalid input")
				enttr=input(">>")
		run=random.choice([0,1,2,3,4,6,8,9])
		
		#code for out 
		if run==0:
			print("ohh shit Player {} is out".format(noOfPlayer))
			noOfPlayer-=1
			if noOfPlayer==0:
				break
		#code for NO Ball / WIDE Ball
		elif run in [8,9]:
			print("oooo wide ball \ No ball, Run scored on this ball :",1)
			Runs+=1
		#code for runs 
		else: 
			print("good run(s) scored on this ball",run)
			Runs+=run

		#decrease the ball count
		totalBalls-=1

	print("end of 1st half ")

	totalRun[Runs]=Team[teamName]	

#Following function delivers instructios as given below in the funciton
def instructions1():
	print(""""So now the team that will bat has to press enter[enter will be considered as you hit the ball with bat]\n 
    for every hit,You will be given run(s):(1,2,3,4,6,8,9,0)
    description:
    0        : you are out
    8        : NO ball
    9        : wide ball
    1,2,3,4,6: Runs """)
	print("so here your batting begins, ")
	print()


#To Clear Screen 
def ClrScr(n=10):
	for i in range(n,0,-1):
		print("The screen will be cleared in :",end="")
		print(n,"\r",end="")
		time.sleep(1)
		#print("\t",end="")
		n-=1
	sub.call("cls",shell=True)



#the main program
def main():
    #This script only run ONCE(Till each team gets to bat and bowl).
    print(gameRule.__doc__)
	
    typeOfGame=selectType()

    noo=getInput()
    print("lets clear the mess on the screen and start the match in 10 sec")
    ClrScr(10)


#Round1 Team A will bat and Team B will bowl
    print("we will start the match now")

    time.sleep(1)
    print("As per toss team {} is going to bat 1st ".format(Team[noo]))

    time.sleep(1)
    print("also type of game selected is: {}".format(typeOfMatch[typeOfGame]))

    time.sleep(1)

    instructions1()
    playMatch(typeOfMatch[typeOfGame+1],noo)
    print("well thats good batting")
    if noo==0:
	    noo=1
    else:
	    noo=0

#Round2 Team B will bat and Team A will bowl
    print("lets clear the mess on the screen and start the match in 10 sec")
    #time.sleep(1)
    print("score till now")
    print(totalRun)
    ClrScr()
    print("Now its turn of 2nd team: {}".format(Team[noo]))
    instructions1()
    playMatch(typeOfMatch[typeOfGame+1],noo)
    print("Bravooooooooooo")
    print("Now we have score of both team")
    print(totalRun)
    print("And The winner is :",end="")
    print(totalRun[max(totalRun)])
    print("Congratulations to winner team")
    time.sleep(1)
    print("Thank you for playing ")
    time.sleep(1)
    print("This terminal will close in 10 sec. To play again click cricket file again")
    time.sleep(10)
    exit()


#the starting pt.
main()
