import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Guessing Game')
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
jimmy = turtle.Turtle()
jimmy.hideturtle()


guessed = 0
data = pd.read_csv("50_states.csv")
states = data.state.to_list()
data_x = data.x.to_list()
data_y = data.y.to_list()
print(states)
while guessed<=50:
    answer = screen.textinput(f"Guessed States {guessed}/50", "Whats another state in U.S.A.:")
    answer = answer.title()
    if answer in states:
        state = data[data.state == answer]
        state_x = data_x[states.index(answer)]
        state_y = data_y[states.index(answer)]
        jimmy.teleport(state_x,state_y)
        jimmy.write(f"{answer}",False,"center",("Arial",10,"normal"))
        guessed+=1
        states.remove(answer)
        data_x.remove(state_x)
        data_y.remove(state_y)

    elif answer =="Exit":
        break

print(states)
df = pd.DataFrame(states)
df.to_csv("States_to_Learn.csv")