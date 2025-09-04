from flask import Flask
import random

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
number_choice = random.choice(numbers)
print(number_choice)

server = Flask(__name__)

@server.route("/")
def greeting():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<p>Insert the number into the URL like so: .../6</p>"
            "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTljZmVpd2VmcTFtdjQxa2ZlNXFiMWVnMzdhOWVjbnI0bXEzeTRtdCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/G6sJqVpD1U4jC/giphy.gif'>"
            )

@server.route(f"/<int:guess>")
def guess_number(guess):
    if guess == number_choice:
        return ("<h1>Correct!</h1>"
                "<img src='https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3aHo2dG1ocXlkdHkwcWR5dzE0YXZhc2R4MnU3dXc2cXQyNzBodG93OCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/HyDAt79JnlY4M/giphy.gif'>"
                )
    elif guess > number_choice:
        return ("<h1>You are too high! Try again.</h1>"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXpmc3MzZG83c2s5dmd6dGR5MzA2aWF0aXVwcGFtb2t1MHU3cGdmMiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/1gdie6tuheZwGlnfwj/giphy.gif'>"
                )
    elif guess < number_choice:
        return ("<h1>You are too low! Try again.</h1>"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTlobTMxbTl5ODRpcDliMGJyMHRqYmhrcWtvN3hiaTh5NXYzbnhubCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/VhtZXXrOBJiItOyFee/giphy.gif'>"
                )

if __name__ == "__main__":
    server.run(debug=True)