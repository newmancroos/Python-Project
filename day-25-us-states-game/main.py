
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image= "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


file = pandas.read_csv("50_states.csv")

is_game_on=True

correct_state_count=0
wrong_answers = 0
guessed_states=[]
all_states = file.state.to_list()

while is_game_on:
    title = f"{correct_state_count}/50 states Correct"
    answer_state = screen.textinput(title=title, prompt="What's another state's name?").title()
    if answer_state =="Exit":
        break

    state= file[file.state==answer_state]
    guessed_states.append(answer_state)
    if state.empty:  # if answer_state not in all_states:
        wrong_answers+=1
        if wrong_answers >= 50:
            is_game_on = False
    else:
        correct_state_count+=1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state.x.item()), int(state.y.item()))
        # t.write(answer_state)
        t.write(state.state.item())

# state to learn.csv

not_in_answer = list((set(all_states) - set(guessed_states)))
pending_states = {"States":not_in_answer}

data_file = pandas.DataFrame(pending_states)
data_file.to_csv("Missing_states.csv")

# turtle.mainloop()

# screen.exitonclick()
