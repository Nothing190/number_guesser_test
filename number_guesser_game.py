import random

class GuessNumber:
    def __init__(self, number, mn=0, mx=100): # mn and mx have default values if there are no values from the user
        self.number = number
        self.guesses = 0
        self.min = mn
        self.max = mx

    def get_guess(self):
        guess = input(f"Please guess a number ({self.min} - {self.max}): ")

        if self.valid_number(guess):
            return int(guess)
        else:
            print("Please enter a valid number.")
            return self.get_guess()

    def valid_number(self, str_number):
        try:
            number = int(str_number)
        except:
            return False
        
        return self.min <= number <= self.max

    def play(self):
            while True:
                self.guesses += 1
                
                guess = self.get_guess()

                if guess < self.number:
                    print("Your guess was under.")
                elif guess > self.number:
                    print("Your guess was over.")
                else: # guess was right
                    break
            
            print(f"You guessed it in {self.guesses} guesses.")

print("This is a game which will guess a radom number. Please use integers only.")
mn = int(input("Please enter the minimum number: "))
mx = int(input("Please enter the maximum number: "))

number = random.randint(mn, mx)

game = GuessNumber(number, mn , mx)
game.play()
                