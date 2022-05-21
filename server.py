from unicodedata import name
from flask import Flask  
app = Flask(__name__)    

# localhost:5000/ - have it say "Hello World!"
@app.route('/')         
def hello_world():
    return 'Hello World!'  
# localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo!"

# Create a route that responds with "Hi" and whatever name is in the URL after /say/
# i.e. localhost:5000/say/flask - have it say "Hi Flask!"
@app.route('/say/<string:name>')
def say_hi(name):
    return "Hi, " + name + "!"

# Create a route that responds with the given word repeated as many 
# times as specified in the URL
@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    output= ""
    for line in range(num):
        output += f"{word} <br>"
    return output
    #testing some other ideas below to avoid the <br> no no
    # new_line = '\n'
    # return(f"{new_line}{new_line(num * word)}")

@app.route('/<wrong_answer>') 
def not_option(wrong_answer):
    return "Sorry! No response. Try again."

    
if __name__=="__main__": 
    app.run(debug=True, port=5000)    
# REMEMBER: Run the app in debug mode. set to false when deploying


