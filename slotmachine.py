"""
-------------------------------
NAME: Jordan Brown
PROJECT: Slot Machine Game
-------------------------------
This program will simulate a simple slot machine. The user is the player of
the game. The game will begin with a default balance and prompt the player
to enter an amount of money to bet. Then, the player will click on the wheel
of the slot machine, and the game will begin. The program works in the
following steps:

    1. The game starts with the player the balance at $100
    2. The player types a number into the bet amount display
    3. The player clicks on the spin button
    4. The wheel display updates to show an independently selected shape
       randomly on each wheel
    5. The player balance updates according to:

                  If all three wheels show the same shape,
                          balance = balance + bet
                          
                  If two of the wheels show the same shape,
                          balance = balance + bet/2
                          
                  If none of the wheels are the same shape,
                          balance = balance - bet
                          
    6. The above steps should repeat until the player balance reaches zero,
       at which point a "You lose" message will display to the player
    
"""

from graphics import *

import math

import random

import time

import winsound


def centerOfWheels(win, w1, w2, w3):
    """ Gets the center of each rectangular wheel of the slot machine.
        Returns the center of all three wheels.
    """
    #gets the center of each wheel
    w1Center = w1.getCenter()
    w2Center = w2.getCenter()
    w3Center = w3.getCenter()

    return w1Center, w2Center, w3Center

    

def isClickInSpin(p):
    """ Determines whether the player's click is inside or outside
        the spin button. Returns true if inside, false otherwise. 
    """
    spinCenter = Point(100,200) #center of the spin button

    #finds the distance of the circle
    dist = math.sqrt( abs((p.getX()- spinCenter.getX())**2 - \
                      (p.getY() - spinCenter.getY())**2 ))
    
    if dist > 55: #distance is outside the radius of the circle
        return False
    else:
        return True #distance is within the radius of the circle
   
      
def spinButton(p,win):
    """ Detects whether player has clicked on spin button. If spin button is
        clicked on, return true. If spin button is not clicked on,
        it returns false and the player is able to click again. 
    """
    while (not(isClickInSpin(p))): #user clicked outside of spin button
        p = win.getMouse()
        return False
    if isClickInSpin(p): #user clicked inside the spin button
        return True
        

def checkBet(bet, win, balance):
    """ Checks to see if the bet amount is valid. If bet is invalid,
        two text box messages, betError1 and betError2, are displayed
        for 5 seconds, then disappear.
        Returns false is bet is invalid, and true otherwise.
    """
    if bet > balance: #bet entered is larger than balance amount
        betError1 = Text(Point(300, 430), "Insufficient funds!") 
        betError1.draw(win)
        betError2 = Text(Point(300, 410), "Please enter a smaller bet")
        betError2.draw(win)
        time.sleep(2.3) #Leaves error text on screen for 5 seconds
        betError1.undraw() 
        betError2.undraw()
        return False
    else:
        return True
    

def drawBackground(win):
    """ Draws the static and changeable background, including the spin button,
       the three wheels of the slot machine, and the text boxes for the
       balance and the bet amounts. Returns the bet entry, the balance box,
       and all three wheels.
    """
    #draws the spin button
    spin = Circle(Point(100,200), 55)
    spin.draw(win)
    spinText = Text(Point(100,200), "Spin")
    spinText.draw(win)
    spin.setFill('yellow')
    
    #draws the 3 wheels of the slot machine. w1, w2, and w3, the first, second
    #and third wheel, respectively
    w1 = Rectangle(Point(205, 340), Point(348, 50))
    w1.draw(win)
    w2 = Rectangle(Point(348, 340), Point(490, 50))
    w2.draw(win)
    w3 = Rectangle(Point(490,340), Point(630,50))
    w3.draw(win)


    #draws the static text box for balance amount
    balanceBox = Text(Point(70,430), "BALANCE: $")
    balanceBox.draw(win)
    
    #draws the text box to display current balance amount
    balance = 100
    balance = str(balance)
    balanceBox = Text(Point(135,430),"") 
    balanceBox.setText(balance)
    balanceBox.draw(win)

    #draws the static text box for bet amount
    betBox = Text(Point(50,405), "BET: $")
    betBox.draw(win)

    #draws the entry box for the current bet amount
    betEntry = Entry(Point(100,405),5) 
    betEntry.draw(win)
    

    return betEntry, balanceBox, w1, w2, w3

def createShapes(win, w1Center, w2Center, w3Center):
    """ Draws each shape for each wheel. The shapes are squares, circles,
        and triangles and are not visible to the user. Returns all the
        shapes of each wheel. 
    """
    #first wheel's square, circle, and triangle
    w11 = Rectangle(Point(245, 224), Point(304, 166))
    w11.setFill("peachpuff")
    w12 = Circle(w1Center, 35)
    w12.setFill("red")
    w13 = Polygon(Point(271, 224), Point(245, 166), Point(304, 166))
    w13.setFill("cyan")

    #second wheel's square, circle, and triangle
    w21 = Rectangle(Point(388, 224), Point(445, 166))
    w21.setFill("peachpuff")
    w22 = Circle(w2Center, 35)
    w22.setFill("red")
    w23 = Polygon(Point(415, 224), Point(387, 166), Point(445, 166))
    w23.setFill("cyan")

    #third wheel's square, circle, and triangle
    w31 = Rectangle(Point(530, 224), Point(589, 166))
    w31.setFill("peachpuff")
    w32 = Circle(w3Center, 35)
    w32.setFill("red")
    w33 = Polygon(Point(556, 224), Point(530, 166), Point(589, 166))
    w33.setFill("cyan")
   
    return w11, w12, w13, w21, w22, w23, w31, w32, w33


def pickW1Shape(win, w11, w12, w13):
    """ Picks a random shape for the first wheel, w1. Picks randomly from 0,
        1, and 2 which represent a square, circle, and triangle, repectively.
        Returns the picked shape of the first wheel, w1shape.
    """
    #generates a random number for the shape, w1ShapeNum, from 0 to 2
    w1ShapeNum = random.randrange(3)
    if (w1ShapeNum == 0):
        w1shape = w11 #wheel is a square
    if (w1ShapeNum == 1):
        w1shape = w12 #wheel is a circle
    if (w1ShapeNum == 2):
        w1shape = w13 #wheel is a triangle
        
    return w1shape
    

def pickW2Shape(win, w21, w22, w23):
    """ Picks a random shape for the second wheel, w2. Picks randomly from 0,
        1, and 2 which represent a square, circle, and triangle, repectively.
        Returns the picked shape of the second wheel, w2shape.
    """
    #generates a random number for the shape, w2ShapeNum, from 0 to 2
    w2ShapeNum = random.randrange(3) 
    if (w2ShapeNum == 0): 
        w2shape = w21 #wheel is a square 
    if (w2ShapeNum == 1):
        w2shape = w22 #wheel is a circle
    if (w2ShapeNum == 2):
        w2shape = w23 #wheel is a triangle
        
    return w2shape

def pickW3Shape(win, w31, w32, w33):
    """ Picks a random shape for the third wheel, w3. Picks randomly from 0,
        1, and 2 which represent a square, circle, and triangle, repectively.
        Returns the picked shape of the third wheel, w3shape.
    """
    #generates a random number for the shape, w3ShapeNum, from 0 to 2
    w3ShapeNum = random.randrange(3)
    if (w3ShapeNum == 0):
        w3shape = w31 #wheel is a square
    if (w3ShapeNum == 1):
        w3shape = w32 #wheel is a circle
    if (w3ShapeNum == 2):
        w3shape = w33 #wheel is a triangle
        
    return w3shape



def undrawShapes(win, w1shape, w2shape, w3shape):
    """ Undraws the shapes that have previously been drawn. Returns the undrawn
        shape of each wheel. 
    """
    w1shape = w1shape.undraw()
    w2shape = w2shape.undraw()
    w3shape = w3shape.undraw()
    
    return w1shape, w2shape, w3shape



def drawShapes(win, w1shape, w2shape, w3shape):
    """ Draws the picked shapes for each wheel. Returns the drawn
        shape of each wheel. 
    """
    w1shape = w1shape.draw(win)
    w2shape = w2shape.draw(win)
    w3shape = w3shape.draw(win)
    
    return w1shape, w2shape, w3shape

    
    

def updateBalance(balance, bet, w1shape, w2shape, w3shape):
    """ Updates the balance, based on the outcome of the wheel spin.
        The possibilities are a win, a partial win, or a loss. 
        Returns the balance.
    """
    #A win, if all picked shapes are of the same shape
    if w1shape == w2shape and w2shape == w3shape and w3shape == w1shape:
        balance = balance + bet

    #A partial win, if at least two picked shapes are of the same shape
    elif w2shape == w1shape or w3shape == w2shape or w1shape == w3shape:
        balance = balance + (bet/2)

    #A loss, if no picked shapes are of the same shape
    else:
        balance = balance - bet
        
    return balance


def main():
    """ Draws the main display window. Prompts the player to enter a bet
        amount, then asks the player to click on the spin button.
        When clicked on, the spin button makes a sound! Then, each wheel
        displays a random shape. The game continues, updating the balance
        and bet based on the wheel shape outcome. Once the balance reaches
        zero a "You lose" message appears, and the user is instructed to
        click to quit. 
    """
    
    #draws the main display window
    win = GraphWin("Python Slot Machine!", 650, 450)
    win.setCoords(0,0,650,450)

    betEntry, balanceBox, w1, w2, w3 = drawBackground(win)
    w1Center, w2Center, w3Center = centerOfWheels(win, w1, w2, w3)
    w11, w12, w13, w21, w22, w23, w31, w32, w33 = createShapes(win, w1Center, \
                                                            w2Center, w3Center)
    
    #pick random shapes
    w1shape = pickW1Shape(win, w11, w12, w13)
    w2shape = pickW2Shape(win, w21, w22, w23)
    w3shape = pickW3Shape(win, w31, w32, w31)

    #draw picked shapes
    drawShapes(win, w1shape, w2shape, w3shape)

    #Instruct user to enter a bet amount and then click spin!
    startText = Text(Point(300, 430), "Enter a bet amount,")
    startText2 = Text(Point(300, 410),"Then click on spin button to begin!")
    startText.draw(win)
    startText2.draw(win)


    #simulates a spin of the slot machine
    balance = 100
    while balance != 0: #Continue to loop, as long as balance is not 0
        
        balance = int(balance)

        
        p = win.getMouse() #player's mouse click

        
        
        if spinButton(p, win): #checks whether the click is valid

        
            startText.undraw()
            startText2.undraw()

            #Plays chime sound 
            soundfile = "c:/Windows/Media/chimes.wav"
            winsound.PlaySound(soundfile, winsound.SND_FILENAME \
                               |winsound.SND_ASYNC)
        
            bet = eval(betEntry.getText()) #updates bet amount
            
            if checkBet(bet, win, balance): #checks to see if bet is valid
                
                #undraw previous selected shapes
                undrawShapes(win, w1shape, w2shape, w3shape)

                #pick random shapes for each wheel
                w1shape = pickW1Shape(win, w11, w12, w13)
                w2shape = pickW2Shape(win, w21, w22, w23)
                w3shape = pickW3Shape(win, w31, w32, w31)

                #draw the randomly picked shapes on the window
                drawShapes(win, w1shape, w2shape, w3shape)
                

                #updates the balance, based on outcome
                balance = updateBalance(balance, bet, w1shape, w2shape, w3shape)
                balance = str(balance)
                balanceBox.setText(balance) #updates balance box display
        


    if balance == 0: #check if the balance is 0
        loseMessage = Text(Point(300, 430), "You lose!")
        loseMessage.draw(win)
        quitMessage = Text(Point(300,410), "Click anywhere to quit.")
        quitMessage.draw(win)
        win.getMouse() #wait for user click
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS) #exit sound
        win.close()
       
    

  
main()

# Cited Sources used for sound
# windows exit sound found at https://docs.python.org/3.4/library/winsound.html
# chime sound for spin button found at https://www.daniweb.com/software-
# development/python/code/216438/play-those-cute-little-wave-files-python

