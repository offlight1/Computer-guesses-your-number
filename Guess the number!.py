import random
import time
print('Welcome to my game! You will have to think of a number 1-10 and the computer will try to guess it. Numbers may be repeated due to my random number generation.!')
play_option = input('Do you want to play? ').lower()
if play_option == 'yes':
  print('Ok, lets play!')
  comp_number_guess = random.randint(0,10) 
  comp_number_guess_two = random.randint(0,10)
  comp_number_guess_tree = random.randint(0,10)
  number_think = input('Think of a number. Once you have thought of a number, answer "yes": ').lower()
  if number_think == 'yes':
   print(comp_number_guess)
   user_guess_reply = input('Is this your number?  ' )
   if user_guess_reply == 'yes':
     print("yay! I won!")
     play_again = input('Do you want to play again? ').lower()
     if play_again == 'yes':
       while True:
        print('Ok, lets play!')
        comp_number_guess = random.randint(0,10)
        number_think = input('Think of a number. Once you have thought of a number, answer "yes": ').lower()
        if number_think == 'yes':
         print(comp_number_guess)
         user_guess_reply = input('Is this your number ').lower()
         if user_guess_reply == 'yes':
           print("yay! I won!")
           play_again == input('Do you want to play again? ').lower() 
           if play_again == 'no':
              quit()
     if play_again == 'no':
       quit()
   while True:
      if user_guess_reply == 'no':
       print('darn! let me try again!')
       print(comp_number_guess_two)
       retry_guess =  input('Is this your number?').lower()
       if retry_guess == 'yes':
           print('yay! I won!')
           time.sleep(3)
           quit()
       if retry_guess == 'no':
         while True:
           if user_guess_reply == 'no':
              print('darn! let me try again!')
              print(comp_number_guess_tree)
              retry_guess =  input('Is this your number?').lower()
              if retry_guess == 'yes':
               print('yay! I won!')
               time.sleep(3)
               quit()
              else:
               if retry_guess == 'no':
                print('I quit! Good job at winning me over, maybe I am not the best number guesser')
                time.sleep(4)
                quit()
else:
  quit()
