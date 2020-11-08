import random 


while 1 < 2:	
	zero_inrow_record = 0
	one_inrow_record = 0

	zero_highscore = 0
	one_highscore = 0

	highscore = 0

	flips = input ('how many flips? :')

	flip = int(flips)
	print(flip)

	for times in range(flip):

		binary_choise = (random.choice([0,1]))
		#print("random number : ",binary_choise) 

		if binary_choise == 0:
			zero_inrow_record = zero_inrow_record + 1
			one_inrow_record = 0
			#print("zero inrow_record :",zero_inrow_record)

			if zero_inrow_record > zero_highscore:
				zero_highscore = zero_inrow_record
				#print('zero high',zero_highscore)

		elif binary_choise == 1:
			one_inrow_record = one_inrow_record + 1
			zero_inrow_record = 0
			#print("one inrow_record :",one_inrow_record)

			if one_inrow_record > one_highscore:
				one_highscore = one_inrow_record
				#`print('one high',one_highscore)


	if zero_highscore > one_highscore:
		highscore = zero_highscore
		print('the highscore is a tails highscore and is', highscore)
		

	elif one_highscore > zero_highscore:
		highscore = one_highscore
		print('the highscore is a heads highscore and is', highscore)
		
	else:
		print('the highscore is a tie between tails and heads and is ',one_highscore)	
