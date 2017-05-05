






from Tkinter import *
from random import sample
import RPi.GPIO as GPIO
from time import sleep
from sys import exit



home = "const3.gif"
hint = "const4.gif"
thirtyPoints = "score30.gif"
twentyFivePoints = "score25.gif"
twentyPoints = "score20.gif"
fifteenPoints = "score15.gif"
tenPoints = "score10.gif"
fivePoints = "score5.gif"
zeroPoints = "score0.gif"

#GPIO pins for red and green LED's
red = 18
green = 23

#GPIO pins for anode RGB LED
redRGB = 12
blueRGB = 21
greenRGB = 16

#Resets RGB LED so that there is no output
def resetRGB():
    GPIO.output(redRGB, GPIO.HIGH)
    GPIO.output(blueRGB, GPIO.HIGH)
    GPIO.output(greenRGB, GPIO.HIGH)

#sets up GPIO pins
def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    colors = [red, green, redRGB, blueRGB, greenRGB]
    for i in colors:
        GPIO.setup(i, GPIO.OUT)
    resetRGB()

    return colors
    
#makes LED blink
def blink(pin):
    GPIO.output(pin, GPIO.HIGH)
    sleep(.1)
    GPIO.output(pin, GPIO.LOW)
    sleep(.2)

#the following functions control the color of the RGB LED
def blinkRed():
    GPIO.output(redRGB, GPIO.LOW)
    GPIO.output(blueRGB, GPIO.HIGH)
    GPIO.output(greenRGB, GPIO.HIGH)
    sleep(.5)
    resetRGB()

def blinkBlue():
    GPIO.output(blueRGB, GPIO.LOW)
    GPIO.output(redRGB, GPIO.HIGH)
    GPIO.output(greenRGB, GPIO.HIGH)
    sleep(.5)
    resetRGB()

def blinkWhite():
    GPIO.output(redRGB, GPIO.LOW)
    GPIO.output(blueRGB, GPIO.LOW)
    GPIO.output(greenRGB, GPIO.LOW)
    sleep(.5)
    resetRGB()    

def blinkYellow():
    GPIO.output(redRGB, GPIO.LOW)
    GPIO.output(blueRGB, GPIO.HIGH)
    GPIO.output(greenRGB, GPIO.LOW)
    sleep(.5)
    resetRGB()

#will control the RGB LED color based on player's input
def lightColor(color):
    if color == "white":
        blinkWhite()
    elif color == "red":
        blinkRed()
    elif color == "yellow":
        blinkYellow()
    elif color == "blue":
        blinkBlue()
    elif color == "orange":
        blinkYellow()


#initializes Game class as a subclass of Frame
class Game(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)



    #sets up GUI 
    def setGUI(self):
        
        #initializes GUI
        self.pack(fill = BOTH, expand = 1)
        
        #sets up entry box 
        Game.player_input = Entry(self, bg = "white")
        
        #whenever enter is pressed, the text contained in the entry box
        #is run through the process function
        Game.player_input.bind("<Return>", self.process)

        #puts entry box at bottom of GUI and stretches is to fit the width
        Game.player_input.pack(side=BOTTOM, fill=X)

        #makes the entry box automatically highlighted when program is run so
        #player does not have to click in it before typing
        Game.player_input.focus()

        #creates Label in GUI where image will be displayed
        img = None
        Game.image = Label(self, width=800, image=img)
        Game.image.image = img
        Game.image.pack(fill=Y)
        Game.image.pack_propagate(False)

    #will set image depending on how many wrong entries have been put in
    def setImage(self, screen):
        Game.img = PhotoImage(file="{}".format(screen))
        Game.image.config(image = Game.img)
        Game.image.image = Game.img
        
    #main function that runs the puzzle
    def play(self):
        self.setGUI()
        self.setImage(home)
        

    #process players input and adds to list
    def process(self, event):

        
        #tip list will show order of each response as correct or incorrect
        tip = []
        global responses
        global points
        global wrongAns
        
        
        color = Game.player_input.get()
        color = color.lower()


        #gives hint if 3 answers are input that arent valid
        if wrongAns  == 2:
            self.setImage(hint)

        if wrongAns == 5:
            pass
        
            


        #if answer is acceptable color it is added to the response list
        if color not in responses:
            if (color == "white" or color == "yellow" or color == "red" or color == "blue" or\
                color == "orange"):
                #sets image back to original after player sees hint image
                self.setImage(home)
                Game.player_input.delete(0, 'end')
                lightColor(color)
                responses.append(color)
                print responses

            #increments wrongAns variable if player input is not valid
            else:
                Game.player_input.delete(0, 'end')
                wrongAns += 1

        else:
            Game.player_input.delete(0, 'end')
            wrongAns += 1


        

        if len(responses) == 5:
            for i in range(len(answers)):
                if answers[i] == responses[i]:
                    tip.append("correct")
                else:
                    tip.append("incorrect")

            print tip
            if tip == ["correct", "correct", "correct", "correct", "correct"]:
                #something will happen if player wins (You can make a function out of the following if wanted)
                #dislays gif for amount of points recieved.
                if (points == 30):
                    self.setImage(thirtyPoints)
                elif (points == 25):
                    self.setImage(twentyFivePoints)
                elif (points == 20):
                    self.setImage(twentyPoints)
                elif (points == 15):
                    self.setImage(fifteenPoints)
                elif (points == 10):
                    self.setImage(tenPoints)
                elif (points == 5):
                    self.setImage(fivePoints)
                else:
                    self.setImage(zeroPoints)

                    
            #if all answers are not right then points will be deducted and responses list is emptied
            else:
                points -= 5
                print "current points = {}\n\n".format(points)
                for i in range(len(tip)):
                    if tip[i] == "correct":
                        blink(green)
                        
                    elif tip[i] == "incorrect":
                        blink(red)
                        
                del responses
                del tip
                responses = []
            
        

            
window = Tk()
window.title("Game")

g = Game(window)

wrongAns = 0

answers = ["blue", "white", "yellow", "red", "orange"]
#creates new list with order shuffled around
answers = sample(answers, len(answers))
responses = []


#starting points
points = 30

setupGPIO()

g.play()

window.mainloop()


    
