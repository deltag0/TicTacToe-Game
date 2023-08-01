import random
import time
def main():
	def sample(ls):
		i = len(ls)-1
		place = random.randint(0,i)
		return ls[place]
	os = []
	xs = []
	end = False
	almost_won = False
	close2 = 0
	num = 2
	dix = {
		1:"   |",
		2:"  |",
		3:"  \n",
		"line1":"----------\n",
		4:"   |",
		5:"  |",
		6:"  \n",
		"line2":"----------\n",
		7:"   |",
		8:"  |",
		9:"  ",
	}

	nexts = {
		
		1: [2,4,5],
		2: [1,3,4,5,6],
		3: [2,5,6],
		4: [1,2,5,7,8],
		5: [1,2,3,4,6,7,8,9],
		6: [2,3,5,8,9],
		7: [4,5,8],
		8: [4,5,6,7,9],
		9: [5,6,8],
	}

	diagonals = {
		1:9,
		3:7,
		7:3,
		9:1,


	}

	corners = [1,3,7,9]
	close = 0
	moves = [1,2,3,4,5,6,7,8,9]
	wins = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], [3,5,7], [3,6,9], [2,5,8], [1,4,7]] 

	com = False
	print("Greetings challenger of the computer...")
	r = random.randint(1, 2)

	ans = int(input("Choose your preffered number, 1 or 2?"))
	if ans == r:
		print("I'll let you start, little one")
	else:
		print("Fool, that was the wrong choice, I start\n")
		com = True
	for x in dix.values():
		print(x, end="")
	print("\n")
	time.sleep(1)
	print("We're playing tic tac toe")
	time.sleep(0.5)
	print("\n\n")
	def hard():
		close = 0
		os = []
		xs = []
		end = False
		almost_won = False
		close2 = 0
		num = 2
		l = [1,3,7,9]
		move1 = sample(l)
		dix[move1] = dix[move1][:1] + 'x' + dix[move1][1:]
		xs.append(move1)
		l.remove(move1)
		moves.remove(move1)
		print("I moved\n")
		time.sleep(0.5)
		for x in dix.values():
			print(x, end="")
		print("\n")

		while True:
			if len(moves) == 0:
				break
			for x in wins:
				s = x.copy()
				s2 = x.copy()
				for y in os:
					if y in x:
						s.remove(y)
						close += 1
				for p in xs:
					if p in x:
						s2.remove(p)
						close2 += 1

				if close2 == 2 and num%2 != 0 and s2[0] not in os:
					end = True
					
					
					winning = s2[0]
					break

				if close == 2 and s[0] not in xs:
					
					urgent = s[0]
					
					almost_won = True
				close = 0
				close2 = 0

			

			if num%2 != 0:
				if end == True:
					
					move = winning
				if almost_won == True and end == False:
					move =  urgent
					
				if num == 3:
					
					if "o" not in dix[5]:
						if move in nexts[move1]:
							
							for x in nexts[move]:
								if x in l:
									l.remove(x)
						l.remove(diagonals[move1])
						move = sample(l)
					else:
						move = diagonals[xs[0]]
				if almost_won == False and end == False and num != 3:
					for x in xs:
						con = False
						for o in os:
							if o in nexts[diagonals[x]]:
								break
							else:
								move = diagonals[x]
								con = True
								break

						if con == True:
							break

				xs.append(move)
				dix[move] = dix[move][:1] + 'x' + dix[move][1:]
				moves.remove(move)
				num += 1
				almost_won = False
				for x in dix.values():
					print(x, end="")
				print("\n\n")
				if end == True:
					print("bye")
					break
				continue


			if num%2 == 0:
				move = int(input(f"Make your move, it can be either of these:{moves} \n"))
				os.append(move)
			

				dix[move] = dix[move][:1] + 'o' + dix[move][1:]
				num += 1

			print("\n\n")
			moves.remove(move)
			for x in dix.values():
				print(x, end="")
			print("\n\n")

	def easy():
		
		num = 2
		close = 0
		os = []
		xs = []
		end = False
		almost_won = False
		close2 = 0
		num = 2
		l = [1,3,7,9]
		bruh = False
		

		while True:

			if len(moves) == 0:
				break
			for x in wins:
				s = x.copy()
				s2 = x.copy()
				for y in os:
					if y in x:
						s.remove(y)
						close += 1
				for p in xs:
					if p in x:
						s2.remove(p)
						close2 += 1

				if close2 == 2 and num%2 != 0 and s2[0] not in os:
					end = True
					
					
					winning = s2[0]
					break

				if close == 2 and s[0] not in xs:
					
					urgent = s[0]
					
					almost_won = True
				close = 0
				close2 = 0

			if num%2 == 0:
				move = int(input(f"Make your move, it can be either of these:{moves} \n"))
				os.append(move)
				dix[move] = dix[move][:1] + 'o' + dix[move][1:]
				moves.remove(move)
				num += 1
				continue

			if num%2 != 0:
				if end == True:
					
					move = winning
				if num == 3 and move not in l:
					move = sample(moves)
					bruh = True
				if move in l and num == 3 and bruh == False:
					move = 5
				if almost_won == True and end == False:
					move =  urgent
				if almost_won == False and end == False and num != 3:
					move = sample(moves)

				
				xs.append(move)
				dix[move] = dix[move][:1] + 'x' + dix[move][1:]
				moves.remove(move)
				num += 1
				almost_won = False
				for x in dix.values():
					print(x, end="")
				print("\n\n")	



			print("\n\n")
			
			for x in dix.values():
				print(x, end="")
			print("\n\n")

			if end == True:
				print("bye")
				break



	if com == True:
		hard()
	else:
		easy()

main()
while True:
	again = input("Play again? y/n ")
	if again == "y":
		main()
	else:
		break

"""	
	moves.remove(move1)
	dix[move1] = dix[move1][:1] + 'x' + dix[move1][1:]
	print("I moved\n")
	time.sleep(0.5)
	for x in dix.values():
		print(x, end="")

	move2 = int(input(f"Make your move, it can be either of these:{moves} \n"))
	dix[move2] = dix[move2][:1] + 'o' + dix[move2][1:]
"""