import turtle
import time #i am here using time because the move of the food or dot  moves very fast hence it cant appear so    `2make it slow using time module
import random #for random food spot

delay=0.1
#score
score=0
high_score=0

#for setting the screen
w = turtle.Screen() #here the variable i took as w i consider it as window
w.title("THE SNAKE GAME")
w.bgcolor("blue")
w.setup(width=600, height=600)
w.tracer(0)#turns off the animation on the screen

#now here we are going to create a snake head
head=turtle.Turtle()
head.speed(0) #0 is the fastest animation speed not screen speed
head.shape("square")
head.color("black")
head.penup()#we use penup so we doesnot draw anything
head.goto(0,0)#because i want it to start from center of the screen
head.direction="stop"

#now here we are going to create a snake food
food=turtle.Turtle()
food.speed(0) #0 is the fastest animation speed not screen speed
food.shape("circle")
food.color("red")
food.penup()#we use penup so we doesnot draw anything
food.goto(0,100)#because i want it to start from center of the screen



segments =[] #it is beacause when a snake touches food we need to add a segment
#pen used to draw or write the score
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score:0 high_score:0",align="center",font=("Courier",24,"normal"))

#function to make the dot or food move
def go_up():
      if head.direction!="down":
          head.direction="up"
      
def go_down():
      if head.direction!="up":
          head.direction="down"
def go_left():
      if head.direction!="right":
          head.direction="left"
def go_right():
      if head.direction!="left":
          head.direction="right"

def mov():#for four directions
    if head.direction == "up":
           y=head.ycor() #here the ycor in goto is 0
           head.sety(y+20)#here i setted it to move up 20 each time

    if head.direction == "down":
           y=head.ycor() #here the ycor in goto is 0
           head.sety(y-20)#here i setted it to move down 20 each time

    if head.direction == "left":
           x=head.xcor() #here the xcor in goto is 0
           head.setx(x-20)#here i setted it to move up 20 each time

    if head.direction == "right":
           x=head.xcor() #here the xcor in goto is 0
           head.setx(x+20) #here i setted it to move right 20 each time
           
#some keys are connected with the specific functions
w.listen()
w.onkeypress(go_up,"5")
w.onkeypress(go_down,"2")
w.onkeypress(go_left,"1")
w.onkeypress(go_right,"3")





#main game loop because the tracer is in speed mode
while True:
       w.update()#everytime the loop runs it updates the screen
       #check for the collision with border
       if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
             time.sleep(1)
             head.goto(0,0)
             head.direction="stop"
             #hide the segments
             for segment in segments:
                  segment.goto(1000, 1000)

            #clear the segment list
             segments.clear()
            #reset the score
             score=0
             #reset thr delay
             delay=0.1

             pen.clear()
             pen.write("Score:{} high_score:{}".format(score, high_score),align="center",font=("Courier",24,"normal"))
      
       #check for the collision with food
       if head.distance(food)<20:
             #move the food to a random spot
            x=random.randint(-290, 290)
            y=random.randint(-290, 290)
            food.goto(x,y)

            #adding a segment
            n_segment= turtle.Turtle()
            n_segment.speed(0)
            n_segment.shape("square")
            n_segment.color("pink")
            n_segment.penup()
            segments.append(n_segment)
            #shorten the delay
            delay -= 0.001

            #increasing the score
            score +=10
            if score>high_score:
                  high_score=score
            pen.clear()
            pen.write("Score:{} high_score:{}".format(score, high_score),align="center",font=("Courier",24,"normal"))
      #move the end segment first in reverse order
       for index in range(len(segments)-1,0,-1):
             x=segments[index-1].xcor()
             y=segments[index-1].ycor()
             segments[index].goto(x,y)
       #move segment 0 to where the head is
       if len(segments)>0:
             x=head.xcor()
             y=head.ycor()
             segments[0].goto(x,y)

            
       mov()#using the same function in loop so it works
       #check for the head collision with the body segment
       for segment in segments:
             if segment.distance(head)<20:
                   time.sleep(1)
                   head.goto(0,0)
                   head.direction="stop"
                   #hide the segments
                   for segment in segments:
                       segment.goto(1000, 1000)

                   #clear the segment list
                   segments.clear()
                   #reset the score 
                   score = 0
                   #reset the delay
                   delay=0.1
                   #update the score display
                   pen.clear()
                   pen.write("Score:{} high_score:{}".format(score, high_score),align="center",font=("Courier",24,"normal"))
              
      

       time.sleep(delay)




w.mainloop()#it helps the window to keep ope