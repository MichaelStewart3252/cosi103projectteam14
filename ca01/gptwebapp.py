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


@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <head>
            <link rel= "stylesheet" type= "text/css" href= "static/css/styles.css">
        </head>
        <h1>GPT Project Team 14</h1>
        <div class="nav-bar">
            <a href="{url_for('team')}">Team Page</a>
            <a href="{url_for('about')}">About Page</a>
            <a href="{url_for('ming')}">Ming-Shih</a>
            <a href="{url_for('xiaoran')}">Xiaoran</a>
        </div>
    '''

@app.route('/team')
def team():
    nav_bar=f'''
    <head>
        <link rel= "stylesheet" type= "text/css" href= "static/css/styles.css">
    </head>
    <div class="nav-bar">
        <a href="{url_for('index')}">Home</a> 
        <a href="{url_for('about')}">About Page</a>
        <a href="{url_for('team')}">Team Page</a>
        <a href="{url_for('ming')}">Ming-Shih</a>
        <a href="{url_for('xiaoran')}">Xiaoran</a>
    </div>
    '''
    return f'''
    {nav_bar}
    <div class="container">
    <h1>Xiaoran</h2>
    <ol>
        <ul>Major: Computer Science</ul>
        <ul>Class standing: first-year master student</ul>
        <ul>Hometown: Beijing, China</ul>
        <ul>Role: Software Development and Emotional Support Engineer</ul>
        <ul>Fun fact: I was in a plane accident at the age of 12!</ul>
    </ol>
    </div>
    '''
@app.route('/about')
def about():
    nav_bar=f'''
    <head>
        <link rel= "stylesheet" type= "text/css" href= "static/css/styles.css">
    </head>
    <div class="nav-bar">
        <a href="{url_for('index')}">Home</a>
        <a href="{url_for('about')}">About Page</a> 
        <a href="{url_for('team')}">Team Page</a>
        <a href="{url_for('ming')}">Ming-Shih</a>
        <a href="{url_for('xiaoran')}">Xiaoran</a>
    </div>
    '''
    return f'''
    {nav_bar}

    '''
@app.route('/ming', methods=['GET', 'POST'])
def ming():
    # This is the nav_bar for all pages 
    nav_bar=f'''
    <head>
        <link rel= "stylesheet" type= "text/css" href= "static/css/styles.css">
    </head>
    <div class="nav-bar">
        <a href="{url_for('index')}">Home</a>
        <a href="{url_for('about')}">About Page</a> 
        <a href="{url_for('team')}">Team Page</a>
        <a href="{url_for('ming')}">Ming-Shih</a>
        <a href="{url_for('xiaoran')}">Xiaoran</a>
    </div>
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.get_tools_for_recipe(prompt)
        return f'''
        {nav_bar}
        <div class="answer">
            <h2>{answer}<h2/>
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
        <div/>
        '''
    
@app.route('/xiaoran', methods=['GET', 'POST'])
def xiaoran():
    
    nav_bar=f'''
    <head>
        <link rel= "stylesheet" type= "text/css" href= "static/css/styles.css">
    </head>
    <div class="nav-bar">
        <a href="{url_for('index')}">Home</a>
        <a href="{url_for('about')}">About Page</a> 
        <a href="{url_for('team')}">Team Page</a>
        <a href="{url_for('ming')}">Ming-Shih</a>
        <a href="{url_for('xiaoran')}">Xiaoran</a>
    </div>
    '''
    if request.method == 'POST':
        date = request.form['date']
        answer = gptAPI.get_celebrate(date)
        return f'''
        {nav_bar}
        <div class="answer">
            <h2>{answer}<h2/>
        </div>
        '''
    else:
        return f'''
        {nav_bar}
        <div class="container">
            <h1>Xiaoran Liu</h1>
            <h2>What day is celebrated on </h2>
            <form method="post">
                <textarea name="date"></textarea>
                <p><input type=submit value="get response">
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