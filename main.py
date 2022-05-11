import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


def create_turtle(state,x,y):
    state_name = turtle.Turtle()
    state_name.ht()
    state_name.penup()
    state_name.goto(x, y)
    state_name.color("black")
    state_name.write(f"{state}")


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states)<50:
    guess = screen.textinput(title=f"[{len(guessed_states)}/50]States correct", prompt="Guess another state").title()
    if guess == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]

        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("States to learn")
        break
    if guess in all_states:
        guessed_states.append(guess)
        row = data[data.state == guess]
        create_turtle(guess, int(row.x), int(row.y))

#screen.exitonclick()
