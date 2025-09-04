from flask import Flask

server = Flask(__name__)

@server.route("/")
def greeting():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTljZmVpd2VmcTFtdjQxa2ZlNXFiMWVnMzdhOWVjbnI0bXEzeTRtdCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/G6sJqVpD1U4jC/giphy.gif'>"
            )

if __name__ == "__main__":
    server.run(debug=True)