import random

class RockPaperScissors:
    '''
    Main class for the game.
    '''
    
    def __init__(self):
        self.choices: list[str] =  ['rock','paper','scissors']

    def get_user_choice(self) -> str :
        
        user_choice: str = input(f'Welcome to your game!\nplease enter your choice from {self.choices}: ')
        
        if user_choice.lower() not in self.choices:
            print('Invalid input! try again. ')
            return self.get_user_choice()
        
        return user_choice.lower()
    
    def get_computer_choice(self) -> str :
        """
        Return a random choice for the computer.
        """
        
        return random.choice(self.choices)
    
    def decide_winner(self,user_choice:str,computer_choice:str) -> str:
        
        if user_choice == computer_choice:
            return("It's a tie! ")
        elif (user_choice,computer_choice) in( 
            ('rock','paper') ,
            ('scissors','rock'),
            ('paper','scissors') 
        ):
            return 'You Lost!'
        else :
            return 'You Won'
        
    def play(self) -> str:
        """Main method to play Rock, Paper, Scissors"""
        
        user_choice:str = self.get_user_choice() 
        computer_choice:str = self.get_computer_choice()
        print(f'Computer choice : {computer_choice}')
        print(self.decide_winner(user_choice,computer_choice))
        
        
if __name__  == '__main__':
    gamer=RockPaperScissors()
    
    while True:
        gamer.play()
        continue_game =input('Do you want play again?\nEnter any key to continue or "n" to quit: ')
        if continue_game.lower() == 'n':
            break
        