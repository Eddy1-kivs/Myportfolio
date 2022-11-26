from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/submit_form', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_data_csv(data)
            return render_template('main.html')
        except:
            return "did not submit"
    else:
        return 'message not send'

@app.route('/<string:page_name>')
def page(page_name='/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')

def write_data_csv(data):
    name = data['name']
    surname = data['surname']
    email = data['email']
    message = data["message"]
    with open('db.csv', 'a', newline='') as csvfile:
        db_write = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_write.writerow([name, surname, email, message])



app.run(host='0.0.0.0', port=8080, debug=True)