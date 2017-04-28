






from Tkinter import *
from random import shuffle

answers = ["blue", "white", "red", "yellow", "orange"]
responses = []
tip = []
points = 500

class Game(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)




    def setupGUI(self):

        self.pack(fill = BOTH, expand = 1)

        Game.player_input = Entry(self, bg = "white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()


        img = None
        Game.image = Label(self, width=800, image=img)
        Game.image.image = img
        Game.image.pack(fill=Y)
        Game.image.pack_propagate(False)


    def setImage(self):
        Game.img = PhotoImage(file="const.gif")
        Game.image.config(image = Game.img)
        Game.image.image = Game.img
        

    def play(self):  
        self.setupGUI()
        self.setImage()

    def process(self, event):
        color = Game.player_input.get()
        color = color.lower()

        if color == "white" or "blue" or "yellow" or "orange" or "red":
            responses.append(color)
            Game.player_input.delete(0, 'end')
            print responses

        if len(responses) == 5:
            for i in range(len(answers)):
                if answers[i] == responses[i]:
                    tip.append("correct")
                else:
                    tip.append("incorrect")

            print tip
            

window = Tk()
window.title("Game")

g = Game(window)
g.play()

window.mainloop()


    
