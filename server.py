from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/index.html')
def hello_world():
    return render_template('index.html')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)


def write_to_database(data):
	with open('database.txt','a') as database:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		database.write(f'\n email:  {email},subject:  {subject},message:  {message}')

def write_to_csv(data):
	with open('database.csv',newline='', mode='a') as db:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		writer=csv.writer(db,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	try:
    		data=request.form.to_dict()
    		write_to_csv(data)
    		return redirect('/thankyou.html')

    	except:
    		return 'Could not write to database'
	
    else:
        return 'Invalid username/password'