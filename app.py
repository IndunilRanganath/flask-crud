# from crypt import methods
# from urllib import request
from flask import Flask,render_template,request,redirect
from models import db,StudentModel




app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config['SQLALCHMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()
 

@app.route('/create', methods= ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')

app.run(host='localhost',  port=5000)