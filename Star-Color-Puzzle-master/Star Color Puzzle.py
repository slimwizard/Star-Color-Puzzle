






from Tkinter import *
from random import sample




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
    def setImage(self):
        Game.img = PhotoImage(file="const3.gif")
        Game.image.config(image = Game.img)
        Game.image.image = Game.img
        
    #main function that runs the puzzle
    def play(self):
        self.setGUI()
        self.setImage()
        

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
            Game.img = PhotoImage(file="const4.gif")
            Game.image.config(image = Game.img)
            Game.image.image = Game.img

        if wrongAns == 5:
            pass
        
            


        #if answer is acceptable color it is added to the response list
        if color not in responses:
            if (color == "white" or color == "yellow" or color == "red" or color == "blue" or\
                color == "orange"):
                #sets image back to original after player sees hint image
                Game.img = PhotoImage(file="const3.gif")
                Game.image.config(image = Game.img)
                Game.image.image = Game.img
                responses.append(color)
                Game.player_input.delete(0, 'end')
                print responses

            #increments wrongAns variable if player input is not valid
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
                    Game.img = PhotoImage(file="score30.gif")  
                    Game.image.config(image = Game.img)
                    Game.image.image = Game.img
                elif (points == 25):
                    Game.img = PhotoImage(file="score25.gif")
                    Game.image.config(image = Game.img)
                    Game.image.image = Game.img
                elif (points == 20):
                    Game.img = PhotoImage(file="score20.gif")
                    Game.image.config(image = Game.img)
                    Game.image.image = Game.img
                elif (points == 15):
                    Game.img = PhotoImage(file="score15.gif")
                    Game.image.config(image = Game.img)
                    Game.image.image = Game.img
                elif (points == 10):
                    Game.img = PhotoImage(file="score10.gif")
                    Game.image.config(image = Game.img)
                    Game.image.image = Game.img
                elif (points == 5):
                    Game.img = PhotoImage(file="score5.gif")
                    Game.image.config(image = Game.img)
                    Game.image.image = Game.img
                else:
                    Game.img = PhotoImage(file="score0.gif")
                    Game.image.config(image = Game.img)
                    Game.image.image = Game.img
                
            #if all answers are not right then points will be deducted and responses list is emptied
            else:
                points -= 5
                print "current points = {}\n\n".format(points)
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


g.play()

window.mainloop()


    
