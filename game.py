from random import randint

class Game():

    def __init__(self, lower, upper, attemptLimit=-1):
        self.lower = lower
        self.upper = upper
        self.target = randint(lower, upper)
        self.attemptLimit = None if attemptLimit < 0 else attemptLimit

    def play(self):
        print('Pick a number between {} and {}'
            .format(self.lower, self.upper)
        )

        while True:
            guess = self._takeGuess()

            if guess == self.target:
                print("Winner!")
                return True
            
            if self.attemptLimit is not None:
                self.attemptLimit -= 1

            if not self._keepGoing():
                print("Loser!")
                return False
            
            hint = "Lower!" if guess > self.target else "Higher!"
            attempts = f" ({self.attemptLimit} guesses left)" if self.attemptLimit else ""
            print(f"{hint}{attempts}")
            

    def _takeGuess(self):
        while True:
            try:
                guess = int(input("> "))
                return guess
            except:
                print("That's not a number!")
                continue

    def _keepGoing(self):
        return self.attemptLimit is None or self.attemptLimit > 0