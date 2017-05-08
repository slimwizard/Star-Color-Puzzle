






from Tkinter import *
from random import sample
import RPi.GPIO as GPIO
from time import sleep
from sys import exit



#dictionary containing the different images that will be displayed
screens = {"home": "const3.gif", "hint": "const4.gif", "fiftyPoints": "score50.gif",\
           "fortyFivePoints": "score45.gif", "fortyPoints": "score40.gif",\
           "thirtyFivePoints": "score35.gif", "thirtyPoints": "score30.gif",\
           "twentyFivePoints": "score25.gif", "twentyPoints": "score20.gif",\
           "fifteenPoints": "score15.gif", "tenPoints": "score10.gif",\
           "fivePoints": "score5.gif", "zeroPoints": "score0.gif"}


#GPIO output pins for red and green LED's
red = 18
green = 23


#any RGB object created will be added to this set 
rgbSet = []

#class to create and control common anode RGB LED's
class RGB(object):
    def __init__(self, redPin, greenPin, bluePin):
        self.red = redPin
        self.green = greenPin
        self.blue = bluePin
        self.off()
        rgbSet.append(self)

    def makeRed(self):
        GPIO.output(self.red, GPIO.LOW)
        GPIO.output(self.green, GPIO.HIGH)
        GPIO.output(self.blue, GPIO.HIGH)

    def makeGreen(self):
        GPIO.output(self.red, GPIO.HIGH)
        GPIO.output(self.green, GPIO.LOW)
        GPIO.output(self.blue, GPIO.HIGH)

    def makeBlue(self):
        GPIO.output(self.red, GPIO.HIGH)
        GPIO.output(self.green, GPIO.HIGH)
        GPIO.output(self.blue, GPIO.LOW)    

    def makeWhite(self):
        GPIO.output(self.red, GPIO.LOW)
        GPIO.output(self.green, GPIO.LOW)
        GPIO.output(self.blue, GPIO.LOW)

    def makePurple(self):
        GPIO.output(self.red, GPIO.LOW)
        GPIO.output(self.green, GPIO.HIGH)
        GPIO.output(self.blue, GPIO.LOW)

    def makeYellow(self):
        GPIO.output(self.red, GPIO.LOW)
        GPIO.output(self.green, GPIO.LOW)
        GPIO.output(self.blue, GPIO.HIGH)

    def off(self):
        GPIO.output(self.red, GPIO.HIGH)
        GPIO.output(self.green, GPIO.HIGH)
        GPIO.output(self.blue, GPIO.HIGH)

#turns all RGB LED's off
def allOff():
    for i in rgbSet:
        i.off()

#turns all RGB's red
def allRed():
    for i in rgbSet:
        i.makeRed()
        
#turns all RGB's green
def allGreen():
    for i in rgbSet:
        i.makeGreen()
        
#turns all RGB's blue
def allBlue():
    for i in rgbSet:
        i.makeBlue()

#turns all RGB's yellow
def allYellow():
    for i in rgbSet:
        i.makeYellow()

#turns all RGB's purple
def allPurple():
    for i in rgbSet:
        i.makePurple()

#turns all RGB's white
def allWhite():
    for i in rgbSet:
        i.makeWhite()
#light display when puzzle is solved       
def gameOver():
    for i in range(8):
        allPurple()
        sleep(.05)
        allWhite()
        sleep(.05)
        allBlue()
        sleep(.05)
        allYellow()
        sleep(.05)
        allRed()
        sleep(.05)
        allGreen()
        sleep(.05)
        
        


#sets up the GPIO
def setupRgbGPIO():
    pins = [13, 22, 4, 16, 24, 19, 5, 17, 20, 25, 26, 6, 27, 21, 12]
    GPIO.setmode(GPIO.BCM)
    for i in pins:
        GPIO.setup(i, GPIO.OUT)


#sets up GPIO pins
def setupLedGPIO():
    GPIO.setmode(GPIO.BCM)
    colors = [red, green]
    for i in colors:
        GPIO.setup(i, GPIO.OUT)

    return colors
    
#makes LED blink
def blink(pin):
    GPIO.output(pin, GPIO.HIGH)
    sleep(.1)
    GPIO.output(pin, GPIO.LOW)
    sleep(.2)


#will control the RGB LED color based on player's input
def lightColor(color):
    if color == "white":
        rgbSet[response].makeWhite()
    elif color == "red":
        rgbSet[response].makeRed()
    elif color == "yellow":
        rgbSet[response].makeYellow()
    elif color == "blue":
        rgbSet[response].makeBlue()
    elif color == "orange":
        rgbSet[response].makeYellow()

        
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
        Game.image = Label(self, width=WIDTH, height=HEIGHT, image=img)
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
        self.setImage(screens["home"])
        

    #process players input and adds to list
    def process(self, event):

        
        #tip list will show order of each response as correct or incorrect
        tip = []
        global response
        global responses
        global points
        global wrongAns
        
        
        color = Game.player_input.get()
        color = color.lower()


        #gives hint if 3 answers are input that arent valid
        if wrongAns  == 2:
            self.setImage(screens["hint"])

        if wrongAns == 5:
            pass
        
            


        #if answer is acceptable color it is added to the response list
        if color not in responses:
            if (color == "white" or color == "yellow" or color == "red" or color == "blue" or\
                color == "orange"):
                #sets image back to original after player sees hint image
                self.setImage(screens["home"])
                Game.player_input.delete(0, 'end')
                lightColor(color)
                response += 1
                responses.append(color)
                sleep(.5)
                allOff()
                print responses
                

            #increments wrongAns variable if player input is not valid
            else:
                Game.player_input.delete(0, 'end')
                allRed()
                sleep(.1)
                allOff()
                sleep(.1)
                allRed()
                sleep(.1)
                allOff()
                sleep(.1)
                allRed()
                sleep(.1)
                allOff()
                sleep(.1)
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
                if (points == 50):
                    self.setImage(screens["fiftyPoints"])
                    gameOver()
                elif (points == 45):
                    self.setImage(screens["fortyFivePoints"])
                    gameOver()
                elif (points == 40):
                    self.setImage(screens["fortyPoints"])
                    gameOver()
                elif (points == 35):
                    self.setImage(screens["thirtyFivePoints"])
                    gameOver()
                elif (points == 30):
                    self.setImage(screens["thirtyPoints"])
                    gameOver()
                elif (points == 25):
                    self.setImage(screens["twentyFivePoints"])
                    gameOver()
                elif (points == 20):
                    self.setImage(screens["twentyPoints"])
                    gameOver()
                elif (points == 15):
                    self.setImage(screens["fifteenPoints"])
                    gameOver()
                elif (points == 10):
                    self.setImage(screens["tenPoints"])
                    gameOver()
                elif (points == 5):
                    self.setImage(screens["fivePoints"])
                    gameOver()
                else:
                    self.setImage(screens["zeroPoints"])
                    gameOver()
                
                    
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
                del response

                response = 0
                responses = []
            
        

WIDTH = 800
HEIGHT = 490

           
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
response = 0

#sets up pins for LED's and RGB's
GPIO.setwarnings(False)
setupLedGPIO()
setupRgbGPIO()

#creates RGB objects
rgb0 = RGB(13, 19, 26)
rgb1 = RGB(22, 5, 6)
rgb2 = RGB(4, 17, 27)
rgb3 = RGB(16, 20, 21)
rgb4 = RGB(24, 25, 12)




g.play()

window.mainloop()


    
