class Remote(): # Encapsulation -> as we are encapsulating remote's function inside a class
    pass

class Player:  # Encapsulation -> as we are encapsulating player's function inside a class
    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveTop(self):
        pass

remote1 = Remote()
player1 = Player()

if(remote1.isLeftPressed()):  #Abstraction -> user dont have to think about what is happening behind the scenes
    player1.moveLeft()