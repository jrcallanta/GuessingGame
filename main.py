import sys
from game import Game

if __name__ == "__main__":
    _, *args = sys.argv
    
    game = None
    try:
        args = [int(arg) for arg in args]
        match(len(args)):
            case 1 if args[0] != 0:
                game = Game(0, *args)
            case (2 | 3) if args[0] < args[1]:
                game = Game(*args)
            case _:
                raise Exception
        
        if game:
            game.play()
    except:
        print("Cannot play game without valid parameters")