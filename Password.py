password = 'a123456'
chance = 3

while True:
        guess = input('Please enter your password')

        if guess == 'a123456':
                print('Login successfully')

        else:
                chance = chance-1
                print('Wrong Password! You still have', chance, 'Chances:')                

        if chance == 0:
                print('Your account is locked! Please call me asap!!!')
                break
	
