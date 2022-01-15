"""
    * we will work on a project which is the US states using csv data and Turtle , we will try to enter the maximum state name that we know
    * in order to insert the image it must be on .gif extension
    *#inserting the image by creating a variable contains the path of the image then add it as a attribute in the addshape ,
        then changing the shape of the turtle into the name of the variable you create it

"""
import turtle
import pandas


def create_turtle(x, y, state_name):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.write(state_name)


# configuring the Screen :
screen = turtle.Screen()
screen.title("US states Game Guessing Created by Ziraoui AnaS")
screen.setup(width=735,height=500)

# inserting the image :
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# we will now extract informations from the csv
data = pandas.read_csv("50_states.csv")
state = data.state.to_list()
x_value = data["x"]
y_value = data["y"]
correct_guessed_states = []
while len(correct_guessed_states) <= 50:
    # asking the user to enter a State Name:
    user_input = str(screen.textinput(title=f"{len(correct_guessed_states)}/50 correct", prompt="Enter a US State : , Type 'Exit' for Exit")).title()
    if user_input in state:
        correct_guessed_states.append(user_input)
        state_data = data[data.state == user_input]
        create_turtle(int(state_data.x) , int(state_data.y) ,user_input)
    elif user_input == "Exit":
        missed_states = [i for i in state if i not in correct_guessed_states]
        m_s = pandas.DataFrame(missed_states)
        m_s.to_csv("States_Missed")
        break


