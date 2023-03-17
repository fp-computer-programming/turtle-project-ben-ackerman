

#To Do: Make background black and make the black selection have a white circle. If they pick grey then keep the text black but otherwise text should be white, add a Simon says logo next to Simon says on title screen. Make shape select arrows
#imports modules turtle, and random so the program has access to their code
import turtle
import random
#P1 is set as a Turtle and is what the player will control
P1 = turtle.Turtle()
#Title1 is set to be a Turtle and will be what makes a lot of the title screens and selections
Title1 = turtle.Turtle()
#Title1 is set to have a speed of 8 so the title and selection runs smoothly
Title1.speed(8)
#for aesthetics, title1 is set to be an arrow and so the player can choose to be an arrow in the shape select screen 
Title1.shape("arrow")
#Second is the detector if the player has already played a round that way the program will show the high score
second = False
#P1 is set to red and a circle to differ it from the background and so the player won’t see it turn for aesthetic purposes 
P1.color("Red")
P1.shape("circle")
P1.hideturtle()
#DSi is the speed of P1 that is altered by the difficulty selection
DSi = 7
#the window is set to equal wind and is named Simon Says
wind = turtle.Screen()
wind.title("Simon Says")
#The initial value of the background color that can be changed in the background color screen is set to black to save lines from function Black and to define brcolor
brcolor = "Black"
#The initial value of the players shape that can be changed in the shape selector screen is set to arrow to save lines from function Arrow and to define shape
shape = "arrow"
#All this line is for is to define P which changes to y when we don’t want keys to do anything and has no effect on the code
P = "x"
#Score is defined and  set to be a list that way it can be appended to later on 
Score = []
#if the player decides to go back to the title screen after losing, tiback will play to restore the values to default
def tiback():

    global DSi
    global brcolor
    global shape
    P1.color("Red")
    P1.shape("circle")
    P1.hideturtle()
    DSi = 7
    brcolor = "Black"
    shape = "arrow"
    Title1.speed(8)
    Title1.shape("arrow")

#All Nono is for is to make keys do nothing
def nono():
    P == "y"
#decide is typically used after the player does an input and the program does not want them doing another input until prompted to do so or until the animation is over
#Sets all the keys to do nothing
def decide():
    wind.onkey(nono,"Up" )
    wind.onkey(nono, "Right")
    wind.onkey(nono, "Left")
    wind.onkey(nono, "Down")
#This is the function for the background selector
def bgs():
    #Function decide is used so they do not activate the function again
    decide()
    #The previous title screen is cleared 
    Title1.clear()
    #goes to the top left and prints “Pick a background color” and then goes up left so it looks better 
    Title1.goto(-200, 100)
    Title1.write("Pick a background color", font=("Verdana", 25, "normal"))
    #Title1 draws the two circles with Grey and Black as an option and then goes back to the text for aesthetics
    Title1.goto(-180, -200)
    Title1.color("Grey")
    Title1.fillcolor("Grey")
    Title1.begin_fill()
    Title1.circle(50)
    Title1.end_fill()
    Title1.penup()
    Title1.goto(180, -200)
    Title1.pendown()
    Title1.color("Black")
    Title1.fillcolor("Black")
    Title1.begin_fill()
    Title1.circle(50)
    Title1.end_fill()
    Title1.penup()
    
    Title1.goto(-220, 120)
    #Before P1 is revealed to the player, it draws two red arrows indicating that you need to use the left and right keys to pick the color
    P1.speed(10)
    P1.penup()
    P1.goto(45, -150)
    P1.pendown()
    P1.forward(75)
    P1.right(135)
    P1.forward(30)
    P1.back(30)
    P1.right(90)
    P1.forward(30)
    P1.penup()
    P1.goto(-45, -150)
    P1.left(45)
    P1.pendown()
    P1.forward(75)
    P1.right(135)
    P1.forward(30)
    P1.back(30)
    P1.right(90)
    P1.forward(30)
    P1.penup()
    P1.goto(0, -150)
    #P1 goes left 45 to reset its angle
    P1.left(45)
    #P1 is now revealed and has its speed restored to 5 
    P1.showturtle()
    P1.speed(5)
    P1.fillcolor("Black")
    #When the player presses the left key, it will do function Grey and if they press the Right key, then they do function Black
    wind.onkey(Grey, "Left")
    wind.onkey(Black, "Right")
#function Grey is what happens when the player chooses Grey in the background select screen
def Grey():
    #Sets it so the brcolor will change even outside the function and uses decide to make it so the player doesn’t change its mind and picks Black which would ruin the program
    global brcolor
    decide() 
    #P1 turns right 180 that way in the shape screen the circles will be the right orientation and so it faces Grey 
    P1.right(180)

    P1.forward(180)
    #When P1 goes forward into the Grey circle title1 will draw a bigger circle outside of it to indicate the players choice
    Title1.goto(-180, -220) 
    Title1.pendown()
    Title1.color("Grey")
    Title1.circle(70)
    #Title1 goes right 360 to make time between the next screen
    Title1.right(360)
    #This is set to Grey that way when brcolor is put into wind.bgcolor(brcolor) it will make the background Grey instead of Black
    brcolor = "Grey"
    #Title1 is set to Black that way it won’t be grey the rest of the program
    Title1.color("Black")
    #the selector screen is cleared and the shape screen is to be played
    Title1.clear()    
    shpscreen()
def Black():
    #function uses  decide to make it so the player doesn’t change its mind and picks Grey which would ruin the program
    decide() 
    #it goes right 180 and backward instead of just going forward that way in shape screen the circles are oriented correctly  
    P1.right(180)   
    P1.backward(180)
    #Title1 draws a black circle around the black filled circle to indicate the players selection
    Title1.goto(180, -220) 
    Title1.pendown()
    Title1.color("Black")
    Title1.circle(70)
    #no brcolor or switch to black is necessary because brcolor and title1 are already by default set to black which saves time. 
    #turns around 360 to give time between screens and then it clears the page and shape screen is played
    Title1.right(360)
    Title1.clear()
    shpscreen()
#the first function of the program and is the title screen at the beginning. This is also called if the player decides to go back to the title screen after losing
def tiscreen():
    #if the player has already played a match, second is set to True and the game screen is cleared to “reset” the program. The high score will not be reset though
    decide()
    if second == True:
        S1.clear()
        E1.clear()
        P1.clear()
        Title1.clear()
        wind.bgcolor("White")
        tiback()
    #Title1 is revealed and goes to the top left and makes a colorful writing that say “Simon Says!”
    Title1.showturtle()
    Title1.color("Black")
    Title1.penup()
    Title1.goto(-180, 100)
    Title1.color("Red")
    Title1.write("Simon Says!", font=("Comic Sans Ms", 50, "normal"))
    Title1.right(360)
    Title1.color("Blue")
    Title1.write("Simon Says!", font=("Comic Sans Ms", 50, "normal"))
    Title1.right(360)
    Title1.color("Green")
    Title1.write("Simon Says!", font=("Comic Sans Ms", 50, "normal"))
    Title1.right(360)
    Title1.color("Yellow")
    Title1.write("Simon Says!", font=("Comic Sans Ms", 50, "normal"))
    Title1.right(360)
    #is cleared so there aren’t extra ugly layers of text behind the black one
    Title1.clear()  
    Title1.color("Black")
    Title1.write("Simon Says!", font=("Comic Sans Ms", 50, "normal"))    
    Title1.goto(-180, 0)
    #Title1 goes lower and writes “Press any arrow key to start” to show the player that the screen is over and they can continue
    Title1.write("Press any arrow key to start", font=("Comic Sans Ms",25, "normal"))
    #goes here for aesthetics
    Title1.goto(-200, 24)
    #when any arrow key is pressed, the next screen will play
    wind.onkey(bgs, "Up")
    wind.onkey(bgs, "Right")
    wind.onkey(bgs, "Down")
    wind.onkey(bgs, "Left")
    #these two lines are prominent through the rest of the program
    wind.listen()   
    wind.mainloop()  
#this function plays the shape selector screen where the player will choose what shape P1 Will be 
def shpscreen():
    #Turtles Turt, Circ, and Squ are set to be global in the program
    global Turt
    global Circ
    global Squ
    #P1’s red arrows are cleared
    P1.clear()    
    P1.goto(0, 0)
    #Title1 goes to the top left and writes pick a shape
    Title1.penup()
    Title1.fillcolor("Black")
    Title1.goto(-180, 220)    
    Title1.write("Pick a shape", font=("Comic Sans Ms", 48, "normal"))
    #Turt, Circ, and Squ are defined, set to be their corresponding shapes, and they all go in different directions from P1 to make a four way selection
    Title1.goto(-200, 260)
    Turt = turtle.Turtle()
    Circ = turtle.Turtle()
    Squ = turtle.Turtle()
    Turt.shape("turtle") 
    Circ.shape("circle")
    Squ.shape("square")
    Turt.penup()
    Circ.penup()
    Squ.penup()
    P1.right(180)
    Circ.goto(150, 0)
    Turt.goto(0, 150)
    Squ.goto(0, -150)
    Title1.goto(-150, 0)
    #when the player presses a directional key, it will do the function that corresponds with the direction
    wind.onkey(trt, "Up")
    wind.onkey(crc, "Right")
    wind.onkey(sq, "Down")
    wind.onkey(arrow, "Left")
    #used to clear screens from shape select and beyond by hiding the turtles and clearing their writing
def hturt():
    Turt.hideturtle()
    Squ.hideturtle()
    Circ.hideturtle()
    Turt.clear()
    Squ.clear()
    Circ.clear()
    Title1.clear()
#called at the beginning of the difficulty select to reappear the turtles except turt and to make title1 yellow, squ orange, and circ red.
def sturt():
    Squ.showturtle()
    Circ.showturtle()
    Title1.showturtle()
    Title1.shape("circle")
    Circ.shape("circle")
    Squ.shape("circle")
    Title1.color("Yellow")
    Title1.fillcolor("Yellow")
    Squ.color("Orange")
    Squ.fillcolor("Orange")
    Circ.color("Red")
    Circ.fillcolor("Red")    
#used to draw the circles at the beginning of a Simon says gam
def sc():
    S1.pendown()
    S1.circle(80)
    S1.penup()
    S1.left(90)
    S1.forward(20)
    S1.right(90)
    S1.pendown()
    S1.circle(60)
    S1.penup() 
#used to generate the sequence that Simon will go in that the player must copy  
def gen_seq():
    #used decide to make sure that the player won’t try to control P1 while Simon is
    decide()
    #seq is set to be global
    global seq
    #appends a random choice of up, right, down, or left to seq for Simon to do. It appends that way it will only add one after every round instead of making a new sequence every round.
    seq.append(random.choice(list(["Up", "Right", "Down", "Left"])))
#Displays the sequence that has been created or changed for Simon to do
def disp_seq():
    #seq is set to be global and also pturn
    global seq
    global pturn
    #for every input in the sequence, the program will play them to show the player what the sequence is. 
    for i in seq:
        P1.penup()
        if i == "Up":
            up()
        elif i == "Down":
            down()
        elif i == "Right":
            right()
        elif i == "Left":
            left()
    #after the loop is over, pturn is set to true that way the player can control P1 again 
    pturn = True
    #plturn sets the inputs to be correspond to functions up, right, down up instead of Nono that way the player is in control again
    plturn()
#the function makes p1 go to the middle of the red circle and the basically invisible E1 fills the circle with its color and then unfills it to give the illusion of a button press.
#This function is used when the player or Simon uses Up
def up():
    #To make sure P1 doesn’t accidentally draw a line, the pen is put up
    P1.penup()
    #this function makes it so the user temporarily cannot control P1
    plpause()
    #E1 goes to the bottom of the inner circle and P1 goes the the middle of it. When it reaches the middle E1 fills the circle with the circles color and then fills it with the background color that way it makes it look like P1 pressed the button
    E1.goto(0, 140)
    E1.pendown()
    E1.fillcolor("Red")
    E1.color("Red")
    E1.begin_fill()
    P1.goto(0, 200)
    E1.circle(60)
    E1.end_fill()
    E1.right(1080)
    E1.fillcolor(brcolor)
    E1.begin_fill()
    E1.circle(60)
    E1.end_fill()
    E1.penup()
    E1.goto(0, 40)
    E1.color(brcolor)       
    #when the circle button “press” is over, E1 goes back to its original location and P1 goes back to the center
    P1.goto(0, 80)
    #plturn is used to set the controls back to the player if it is their turn and not simons
    plturn()
    #if it is the players turn, the value is added to pseq that way the game can check if the player sequence is the same as the simons sequence
    if pturn == True:
        pseq.append("Up")
        #gc is used to check if the game is over
        gc()
#the function makes p1 go to the middle of the blue circle and the basically invisible E1 fills the circle with its color and then unfills it to give the illusion of a button press.
#This function is used when the player or Simon uses “Right”
def right():
    #To make sure P1 doesn’t accidentally draw a line, the pen is put up
    P1.penup()
    #this function makes it so the user temporarily cannot control P1
    plpause()
    #E1 goes to the bottom of the inner circle and P1 goes the the middle of it. When it reaches the middle E1 fills the circle with the circles color and then fills it with the background color that way it makes it look like P1 pressed the button
    E1.goto(120, 20)
    E1.pendown()
    E1.fillcolor("Blue")
    E1.color("Blue")
    E1.begin_fill()
    P1.goto(120, 80)
    E1.circle(60)
    E1.end_fill()
    E1.right(1080)
    E1.fillcolor(brcolor)
    E1.begin_fill()
    E1.circle(60)
    E1.end_fill()
    E1.penup()
    E1.goto(0, 40)
    E1.color(brcolor)
    #when the  circle button “press” is over, E1 goes back to its original location and P1 goes back to the center  
    P1.goto(0, 80)
    #plturn is used to set the controls back to the player if it is their turn and not simons
    plturn()
    #if it is the players turn, the value is added to pseq that way the game can check if the player sequence is the same as the simons sequence
    if pturn == True:
        pseq.append("Right")
        #gc is used to check if the game is over
        gc()
#the function makes p1 go to the middle of the Green circle and the basically invisible E1 fills the circle with its color and then unfills it to give the illusion of a button press.
#This function is used when the player or Simon uses “Left”

def left():
    #To make sure P1 doesn’t accidentally draw a line, the pen is put up
    P1.penup()
    #this function makes it so the user temporarily cannot control P1
    plpause()
    #E1 goes to the bottom of the inner circle and P1 goes the the middle of it. When it reaches the middle E1 fills the circle with the circles color and then fills it with the background color that way it makes it look like P1 pressed the button
    E1.goto(-120, 20)
    E1.pendown()
    E1.fillcolor("Green")
    E1.color("Green")
    E1.begin_fill()
    P1.goto(-120, 80)
    E1.circle(60)
    E1.end_fill()
    E1.right(1080)
    E1.fillcolor(brcolor)
    E1.begin_fill()
    E1.circle(60)
    E1.end_fill()
    E1.penup()
    E1.goto(0, 40)
    E1.color(brcolor)
    #when the  circle button “press” is over, E1 goes back to its original location and P1 goes back to the center      
    P1.goto(0, 80)
    #plturn is used to set the controls back to the player if it is their turn and not simons
    plturn()
    #if it is the players turn, the value is added to pseq that way the game can check if the player sequence is the same as the simons sequence
    if pturn == True:
        pseq.append("Left")
        #gc is used to check if the game is over
        gc()  
#the function makes p1 go to the middle of the yellow circle and the basically invisible E1 fills the circle with its color and then unfills it to give the illusion of a button press.
#This function is used when the player or Simon uses “Down”
    
def down():
    #To make sure P1 doesn’t accidentally draw a line, the pen is put up
    plpause()
    #this function makes it so the user temporarily cannot control P1
    P1.penup()
    #E1 goes to the bottom of the inner circle and P1 goes the the middle of it. When it reaches the middle E1 fills the circle with the circles color and then fills it with the background color that way it makes it look like P1 pressed the button
    E1.goto(0, -100)
    E1.pendown()
    E1.fillcolor("Yellow")
    E1.color("Yellow")
    E1.begin_fill()
    P1.goto(0, -40)
    E1.circle(60)
    E1.end_fill()
    E1.right(1080)
    E1.fillcolor(brcolor)
    E1.begin_fill()
    E1.circle(60)
    E1.end_fill()
    E1.penup()
    E1.goto(0, 40)
    E1.color(brcolor)
    #when the  circle button “press” is over, E1 goes back to its original location and P1 goes back to the center    
    P1.goto(0, 80)
    #plturn is used to set the controls back to the player if it is their turn and not simons
    plturn()
    #if it is the players turn, the value is added to pseq that way the game can check if the player sequence is the same as the simons sequence
    if pturn == True:
        pseq.append("Down")
        #gc is used to check if the game is over
        gc()
#used to set the controls for P1 only if it is the players turn
def plturn():
    if pturn == True:
        wind.listen()
        wind.onkey(up, "Up")
        wind.onkey(right, "Right")
        wind.onkey(left, "Left")
        wind.onkey(down, "Down")
#Similar to decide(), except pturn has to be true that way it does not waste time when doing the display sequence 
def plpause():
    if pturn == True:
        wind.onkey(nono,"Up" )
        wind.onkey(nono, "Right")
        wind.onkey(nono, "Left")
        wind.onkey(nono, "Down")
#if the player chooses hard mode, this animation will be played
def hspiral():
    #P1 is hidden to make the screen completely black
    P1.hideturtle()
    #Circ is set to red and to be so small that it’s almost impossible to see and puts it at the center where the spiral will start
    Circ.color("Red")
    Circ.fillcolor("Black")
    Circ.shapesize(.1)
    Circ.goto(0, 0)
    Circ.pendown()
    Circ.speed(10)
    #this loop goes on for 40 lines for the spiral, for every line, it will go 1+1*i**2 forward and make a right turn. I is changed so it will gradually go more and more forward
    for i in range(40):
        Circ.forward(1 + 1 * i**2)
        Circ.right(90)
    #circ is set to be very wide and to go to the bottom right corner that way it fills the screen with red
    Circ.width(1500)
    Circ.goto(450, -450) 
    #P1 is set to show again that way it doesn’t mess with the rest of the program
    P1.showturtle()
#function that plays when the player presses left and selects easy mode
def ez():
    #decide is used to make sure the player does not input after their decision which would mess up the program
    decide()
    #DSi is set to global that way it is changed during broplan
    global DSi
    #P1 goes to the yellow circle that says easy and the background flashes yellow to indicate their decision
    P1.goto(-165, 0)
    wind.bgcolor("Yellow")
    P1.right(360)
    wind.bgcolor("White")
    P1.right(360)
    wind.bgcolor("Yellow")
    P1.right(360)
    wind.bgcolor("White")
    P1.right(360)
    #hides title1 so it does not appear in the game
    Title1.hideturtle()
    #Sets the speed of P1 to be 1 that way the player has more time to process simons inputs
    DSi = 1
    #uses hturt to hide the circles that way they don’t show up in the game
    hturt()
    #the game begins with the settings chosen
    bplan()
def mid():
    #decide is used to make sure the player does not input after their decision which would mess up the program
    decide()
    #DSi is set to global that way it is changed during broplan
    global DSi
    #P1 goes to the orange circle that says medium and the background flashes orange to indicate their decision
    P1.goto(-15, -150)
    wind.bgcolor("Orange")
    P1.right(360)
    wind.bgcolor("White")
    P1.right(360)
    wind.bgcolor("Orange")
    P1.right(360)
    wind.bgcolor("White")
    P1.right(360)
    #hides title1 so it does not appear in the game
    Title1.hideturtle()
    #Sets the speed of P1 to be 5 that way the player has average time to process simons inputs
    DSi = 5
    #uses hturt to hide the circles that way they don’t show up in the game
    hturt()
    #the game begins with the settings chosen
    bplan()
def hard():
    #decide is used to make sure the player does not input after their decision which would mess up the program
    decide()
    #DSi is set to global that way it is changed during broplan
    global DSi
    #P1 goes to the red circle that says Hard and the background flashes yellow, to orange, to red, then to black to indicate a a dying flame to indicate their decision
    P1.goto(135, 0)
    wind.bgcolor("Yellow")
    P1.right(360)
    wind.bgcolor("Orange")
    P1.right(360)
    wind.bgcolor("Red")
    P1.right(360)
    wind.bgcolor("Black")
    #after the flashing, it slowly hides the turtles to build suspension for the spiral animation
    P1.right(360)
    Title1.hideturtle()
    P1.right(360)
    Squ.hideturtle()
    P1.right(720)
    #calls function hspiral to do the spiral animation
    hspiral()
    #sets the turtle to max speed
    DSi = 10
    #uses hturt to make sure all of the turtles are gone
    hturt()
    #the game immediately begins after the spiral so the player has to pay extra attention
    bplan()
#the screen where the player gets to choose the difficulty/speed of the game
def dif():
    P1.penup()
    #goes to the middle of the 3 options
    P1.goto(-15, 0)
    #each turtle writes what difficulty they represent in different fonts and styles
    Squ.write("Medium", font=("Arial", 20, "italic"))
    Title1.write("Easy", font=("Comic Sans MS", 20, "normal"))
    Circ.write("HARD", font=("Times", 20, "bold"))
    #after they write, they move a bit to make the page look better
    Squ.goto(-15, -150)
    Circ.goto(135, 0)
    Title1.goto(-165, 0)
    #reappears  the turtles except turt and to make title1 yellow, squ orange, and circ red
    sturt()
    #sets the directions to do their corresponding functions
    wind.onkey(ez, "Left")
    wind.onkey(mid, "Down")
    wind.onkey(hard, "Right")
#clears the window
def cw():
    wind.clear()
#function for when the player loses and the end text and options appear
def g_end():
    #makes second global so other functions can see that second will equal true
    global second
    #P1 is hidden and writes the end screen by going down and writing
    P1.goto(-180, 0)
    P1.hideturtle()
    P1.write("GAME OVER", font=("Times", 50, "bold"))
    P1.goto(-180, -50)
    #goes right to delay between text
    P1.right(1080)
    P1.write("Your Score Is:", font=("Verdana", 40, "normal"))
    P1.goto(-180, -100)
    #goes extra right to build suspense
    P1.right(1080)
    #uses .format to do the last value in Score. The first time score will only have one value, but afterwards it will have more so the last one is the most recent
    P1.write("{0}!!!".format(Score[-1]), font=("Verdana", 40, "underline"))
    P1.goto(-180, -200)
    #if they have already played a game, then it will give their highest score
    if second == True:
        P1.write("High Score: {0}!!!".format(HighScore), font=("Verdana", 40, "italic"))
    #goes right so the player can process the high score before reading more
    P1.right(1080)
    P1.goto(-180, -250)
    #P1 writes Play again and back to title screen with its controls so the player knows how to do both
    P1.write("Play Again? [Press Up or Right]", font=("Verdana", 10, "normal"))
    P1.goto(-180, -300)
    P1.write("Back to title screen [Press Down or Left]", font=("Verdana", 10, "normal"))
    second = True
    #if the player does up or right, broplan will play and it acts as a retry button
    #if the player does down or left, it goes back to the title screen
    wind.onkey(broplan, "Up")
    wind.onkey(tiscreen, "Down")
    wind.onkey(broplan, "Right")
    wind.onkey(tiscreen, "Left") 
#the function that checks if the game is over
def bplan():
    decide()
    global E1 
    global S1
    E1 = turtle.Turtle()
    S1 = turtle.Turtle()
    broplan()
def gc():
    #sets the following to global so they are changed throughout the game
    global pturn
    global hsc
    global HighScore
    #Lp and La are set to be how many values are in the sequence and represent the players score
    Lp = len(pseq)
    Ls = len(seq)
    #S1 is hidden
    S1.hideturtle()
    #if pseq is the same as seq, the player won the round and the next round is started
    if pseq == seq:
        #pturn is set to false because it is now simons turn 
        pturn = False
        #generates another value for the sequence and clears pseq so they have to input everything again.
        gen_seq()
        pseq.clear()
        #p1 has penup so they don’t write. 
        #p1 does a victory circle to show they won the round
        P1.penup()
        P1.circle(15)
        #simon displays the updated sequence
        disp_seq()
    #if the length of the player sequence and the length of the normal sequence are the same, but they do not have the same values, then that means the player lost. 
    elif Lp == Ls and pseq != seq:
        #pauses the controls so they don’t move in the end screen
        plpause()
        #the score has the length of the sequence added to the end. This helps determine high scores and the current score
        Score.append(Ls)
        #if this is the second time a player has played after starting the program, it will determine the high score.
        if second == True:
            #hsc is set to be a copy of score
            hsc = Score.copy()
            #hsc is set to be sorted in numerical order
            hsc.sort()
            #now that it is sorted, the highest score is now the last integer, so the highscore is set to be the last one in list hsc
            HighScore = hsc[-1]
        #plays the end screen
        g_end()
def broplan():
    #uses decide to make sure the player can not control p1
    decide()
    #sets the following to be global that way they are changed outside the function 
    global E1
    global S1
    global seq
    global pseq
    global pturn
    global ge
    #the background color is set to be what the player chose
    wind.bgcolor(brcolor)
    #sets it to be white and black that way it always sticks out of the background 
    P1.color("White")
    P1.fillcolor("Black")
    #the shape of P1 is set to be what the player chose
    P1.shape(shape)
    #defines turtle E1 and is set to be color of background and small so it is not seen and it’s lines and circles are seen as blank
    E1.color(brcolor)
    E1.shapesize(.01)
    #defines S1 and appears it incase they went back to the title screen. 
    
    S1.showturtle()
    #set to red in preparation for sc
    S1.color("Red")
    #puts the penup to make sure it doesn’t accidentally draw
    S1.penup()
    # clears the following incase they went back to the title screen
    E1.clear()
    P1.clear()
    S1.clear()
    #set to be fast so it makes the board faster and goes to the following cords and changes color to fit which circle it is making
    S1.goto(0, 120)
    S1.speed(15)
    sc()
    S1.color("Blue")
    S1.goto(120, 0)
    sc()
    S1.color("Yellow")
    S1.goto(0,-120)
    sc()
    S1.color("Green")
    S1.goto(-120,0)
    sc()
    #after it is done s1 should be hidden
    S1.hideturtle
    #once S1 is done making the board P1 reappears and has its speed set to what the difficulty the player chose to pick has
    P1.showturtle()
    P1.speed(DSi)
    #E1 has ir go super fast to help with aesthetics
    E1.speed(12)
    #defines lists seq and pseq
    seq = []
    pseq = []
    #pturn is set to false initially to make the program run better
    pturn = False    
    ge = False
    #begins the game by generating the seq and displaying it which allows the player to begin 
    gen_seq()
    disp_seq()
#if the player chose the turtle, this function will be played to set the shape, play the animation, and go to the difficulty screen
def trt():
    decide()
    global shape
    P1.goto(0, 130)
    P1.pendown()
    P1.circle(20)
    shape = "turtle"
    Title1.clear()
    P1.clear()
    hturt()
    dif()
#if the player chose the circle, this function will be played to set the shape, play the animation, and go to the difficulty screen
def crc():
    decide()
    global shape
    P1.goto(150, -20)
    P1.pendown()
    P1.circle(20)
    shape = "circle"
    Title1.clear()
    hturt()
    P1.clear()
    dif()
#if the player chose the square, this function will be played to set the shape, play the animation, and go to the difficulty screen
def sq():
    decide()
    global shape
    P1.goto(0, -170)
    P1.pendown()
    P1.circle(20)
    shape = "square"
    Title1.clear()
    hturt()
    P1.clear()
    dif()
#if the player chose the turtle, this function will play the animation and go to the difficulty screen
def arrow():
    decide()
    P1.goto(-147.5, -20)
    P1.pendown()
    P1.circle(20)
    Title1.clear()
    hturt()
    P1.clear()
    dif()
#how the entire program starts!
tiscreen()
#if Broham != 1:
#    wind.mainloop()
