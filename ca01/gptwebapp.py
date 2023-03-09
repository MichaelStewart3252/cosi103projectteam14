'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

# This is the nav_bar for all pages 
nav_bar=f'''
    <head>
        <link rel= "stylesheet" type= "text/css" href= "static/css/styles.css">
    </head>
    <div class="nav-bar">
        <h1 class="team-name">GPT Project Team 14</h1>
        <a href="/">Home</a>
        <a href="/about">About Page</a> 
        <a href="/team">Team Page</a>
        <a href="/ming">Ming-Shih</a>
        <a href="/xiaoran">Xiaoran</a>
        <a href="/harry">Harry</a>
    </div>
    '''

@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return nav_bar

@app.route('/team')
def team():
    return f'''
    {nav_bar}
    <div class="container">
        <div class="item">
            <h1>Xiaoran</h2>
            <ul>
                <li>Major: Computer Science</li>
                <li>Class standing: first-year master student</li>
                <li>Hometown: Beijing, China</li>
                <li>Role: Software Development and Emotional Support Engineer</li>
                <li>Fun fact: I was in a plane accident at the age of 12!</li>
            </ul>
        </div>
        <div class="item">
            <h1>Harry</h2>
            <ul>
                <li>Major: Computer Science & Anthropology</li>
                <li>Class standing: sophomore</li>
                <li>Hometown: Beijing, China</li>
                <li>Role: Software Development</li>
                <li>Fun fact: I love the color yellow, yea...</li>
            </ul>
        </div>
    </div>
    '''
@app.route('/about')
def about():
    return f'''
    {nav_bar}
    <div class="aboutContainer">
        <div class="item">
            <h2>Ming</h2>
            <p>My program generates a GPT response that tells the user what they should get to complete the course they are cooking.</p>
        </div>
        <div class="item">
            <h2>Xiaoran</h2>
            <p>My program asks the user to enter a date of their choice and return a holiday/national day of that specific date via ChatGPT openai API!</p>
        </div>
         <div class="item">
            <h2>Harry</h2>
            <p>My function provides a recipe for the course my user is looking fo. Eat well!</p>
        </div>
    </div>
    '''
@app.route('/ming', methods=['GET', 'POST'])
def ming():
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.get_tools_for_recipe(prompt)
        return f'''
        {nav_bar}
        <div class="answer">
            <h2>{answer}</h2>
        </div>
        '''
    else:
        return f'''
        {nav_bar}
        <div class="container">
            <h1>Ming-Shih</h1>
            <h2>Enter the course you're cooking and recieve a list of tools you'll need</h2>
            <form class="form" method="post">
                <textarea name="prompt"></textarea>
                <p><input class="submit" type=submit value="get response"><p/>
            </form>
        </div>
        '''
    
@app.route('/xiaoran', methods=['GET', 'POST'])
def xiaoran():
    if request.method == 'POST':
        date = request.form['date']
        answer = gptAPI.get_celebrate(date)
        return f'''
        {nav_bar}
        <div class="answer">
            <h2>{answer}</h2>
        </div>
        '''
    else:
        return f'''
        {nav_bar}
        <div class="container">
            <h1>Xiaoran</h1>
            <h2>What day is celebrated on </h2>
            <form class="form" method="post">
                <textarea name="date"></textarea>
                <p><input class="submit" type=submit value="get response"></p>
            </form>
        </div>
        '''
    
@app.route('/harry', methods=['GET', 'POST'])
def harry():
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.recipe(prompt)
        return f'''
        {nav_bar}
        <div class="answer">
            <h2>{answer}</h2>
        </div>
        '''
    else:
        return f'''
        {nav_bar}
        <div class="container">
            <h1>Harry C.</h1>
            <h2>Enter the course you're cooking tonight and you will receive the recipe for it</h2>
            <form class="form" method="post">
                <textarea name="prompt"></textarea>
                <p><input class="submit" type=submit value="get response"><p/>
            </form>
        </div>
        '''
    

# @app.route('/gptdemo', methods=['GET', 'POST'])
# def gptdemo():
#     ''' handle a get request by sending a form 
#         and a post request by returning the GPT response
#     '''
#     if request.method == 'POST':
#         prompt = request.form['prompt']
#         answer = gptAPI.getResponse(prompt)
#         return f'''
#         <h1>GPT Demo</h1>
#         <pre style="bgcolor:yellow">{prompt}</pre>
#         <hr>
#         Here is the answer in text mode:
#         <div style="border:thin solid black">{answer}</div>
#         Here is the answer in "pre" mode:
#         <pre style="border:thin solid black">{answer}</pre>
#         <a href={url_for('gptdemo')}> make another query</a>
#         '''
#     else:
#         return '''
#         <h1>GPT Demo App</h1>
#         Enter your query below
#         <form method="post">
#             <textarea name="prompt"></textarea>
#             <p><input type=submit value="get response">
#         </form>
#         '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)