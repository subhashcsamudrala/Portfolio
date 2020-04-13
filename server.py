from flask import Flask, render_template
from flask import request
import csv
import pdb
app = Flask(__name__)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    try:

        if request.method == 'POST':
            data = request.form.to_dict()
            write_to_csv(data)

            return data
        else:
            return 'something went wrong!'
        return 'hi'
    except:
        return 'some exception'


def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('eggs.csv', 'w', newline='') as csvfile:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([email,subject,message])

@app.route('/')
@app.route('/<string:page_name>')
def hello_world(page_name=None):
    return render_template(page_name)

