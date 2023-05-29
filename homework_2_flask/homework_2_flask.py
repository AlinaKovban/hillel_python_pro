from flask import Flask
import pandas as pd
import random
import string


app = Flask(__name__)

@app.route('/password')
def generate_password():
    password = string.ascii_letters + string.digits + string.punctuation 
    result = ''.join(random.choices(password, k = random.randint(10, 20)))
    return result
    

@app.route('/calculate_average')
def calculate_average():
    height_weight = pd.read_csv('hw.csv')
    mean_height = height_weight[' Height(Inches)'].mean()
    mean_weight = height_weight[' Weight(Pounds)'].mean()
    return f'<p>Average height: {round(mean_height, 2)}  <br>Average weight: {round(mean_weight, 2)}</p>'
