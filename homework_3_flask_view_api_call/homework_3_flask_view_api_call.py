import pandas as pd

import requests

from http import HTTPStatus

from flask import Flask, request, Response
from faker import Faker


app = Flask(__name__)

fake_data = Faker("UK")

@app.route("/students")
def generate_students():
    counter = request.args.get("input_counter", "1000")
    counter_int = int(counter)
    students = []
    for _ in range(int(counter_int)):
        birthday = fake_data.date_of_birth(minimum_age=18, maximum_age=60).strftime("%Y-%m-%d")
        person = fake_data.first_name() + " " + fake_data.last_name() + " " + fake_data.email() + " " + fake_data.password() + " " + birthday
        students.append(person)
        
    data_frame = pd.DataFrame(students)
    data_frame.to_csv("students.csv", index=False)
    
    students_str = "<br>".join(students)
    return students_str
    

@app.route("/bitcoin_value")  
def get_bitcoin_value():
    url = "https://bitpay.com/api/rates"
    data_from_url = requests.get(url, {})
    value_currency = data_from_url.json()
    currency = request.args.get("currency", "USD")
    convert = request.args.get("convert", "1")
    
    if data_from_url.status_code not in (HTTPStatus.OK):
        return Response(
            "ERROR: Something went wrong",
            status=data_from_url.status_code
        )
    
    for rate in value_currency:
        if rate['code'] == currency:
            bitcoin_rate = float(rate['rate'])
            break
    else:
        return f"Currency {currency} not found"

    converted_value = float(convert) * bitcoin_rate
    
    return f"1 bitcoin in {currency} is {bitcoin_rate}. {convert} bitcoin(s) = {converted_value} {currency}."
            
    





