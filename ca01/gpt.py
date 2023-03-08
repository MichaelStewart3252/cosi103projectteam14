'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''
import openai

class GPT():


    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def result(self, self_obj, prompt):
        '''Ming: I added this function that returns the results to avoid writing this so many times in our program'''
        completion = openai.Completion.create(
            engine=self_obj.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )
        return completion
    
    def getResponse(self,prompt):
        ''' template to generate a GPT response '''
        completion = self.result(self,prompt)
        response = completion.choices[0].text
        return response
    
    def recipe(self,course):
        ''' Generate a GPT response '''
        prompt = 'genrate a recipe for ' + course
        completion = self.result(self, prompt)
        response = completion.choices[0].text
        return response 
    
    def get_tools_for_recipe(self, course):
        '''Ming'''
        '''generates a GPT response that tells the user what they should get to complete the course they are cooking'''
        prompt = f'what are the things I would need to cook {course} as a college student'
        completion = self.result(self, prompt)
        response = completion.choices[0].text
        return response 
    
    #Xiaoran's prompt of getting what day is it today!
    def get_celebrate(self, date):
        prompt = f'What day is celebrated on {date}?'
        completion = self.result(self, prompt)
        response = completion.choices[0].text
        return response
        
if __name__=='__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g.recipe("chicken"))