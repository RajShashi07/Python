#Importing Libraries
import tkinter
import random


#list of possible colors
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black',
          'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
# Game time left , for 30
timeleft = 30

# startGame function will start the game
def startGame(event):
    if timeleft == 30:
        # Start the countdown
        countdown()
    # nextcolor function to display the next color
    nextcolor()

def nextcolor():
    # Using the globally  declared 'score' and 'play' variables above
    global score
    global timeleft

    # If a game is currently in play
    if timeleft > 0:
        e.focus_set()   # To make the entry box active

        # If the color type is equal to the color of the text
        if e.get().lower() == colors[1].lower():
            score += 1
        # Clear the text entry box.
        e.delete(0,tkinter.END)

        random.shuffle(colors)

        #Change the color to type, by changing the text_and_the
        # color to random color value
        label.config(fg =str(colors[1]),text=str(colors[0]))
        #Updating the score
        scoreLabel.config(text="Score:" + str(score))

def countdown():
    global timeleft

    # Idf a game is in play
    if timeleft > 0:
        # Decrement the timer
        timeleft -= 1
        #Update the time left label
        timeLabel.config(text = "Timeleft:" + str(timeleft))
        # Run the function again after 1 Second
        timeLabel.after(1000,countdown)

# Create GUI window
root = tkinter.Tk()

#set the title
root.title("WELCOME TO COLOR GAME")
#set the size
root.geometry("360x260")

#add the instruction label
instructions = tkinter.Label(root, text="Type in  the color of words and not the word ", font = ('Helvetica',12))
instructions.pack()

#Add the score label
scoreLabel = tkinter.Label(root, text = "Press Enter to Start", font = ('Helvetica',12))
scoreLabel.pack()

#Add the time left label
timeLabel = tkinter.Label(root, text = "Timeleft:" + str(timeleft), font = ('Helvetica',12))
timeLabel.pack()

# Add a label for displaying the color
label = tkinter.Label(root, font = ('Helvetica',12))
label.pack()

#add the text box for typing in color
e = tkinter.Entry(root)
root.bind('<Return>',startGame)
e.pack()

# Set focus on the entry box
e.focus_set()
# Start GUI
root.mainloop()
