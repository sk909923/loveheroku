from flask import Flask,render_template,request,redirect,url_for
from flask.wrappers import Request 
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:123123123@localhost/postgres"
# app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://gvuagmyojfxnrf:efa91db5ad2207402e79c8a5c1b919fceddf6cd757c3d357ee316002d66e70b2@ec2-34-193-113-223.compute-1.amazonaws.com:5432/d7st1u7mj6lhiq"
app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://chrvrnohxcqwxs:f1e31a8843911d00e1b694fdd28cec82cd2761e09ea18cbdee771f4b1c35b78a@ec2-34-232-191-133.compute-1.amazonaws.com:5432/d1mp5f9ntis6pt"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
db = SQLAlchemy(app)
class mytable(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30))
    name2=db.Column(db.String(30))
    percentage=db.Column(db.Integer)

@app.route('/main',methods=['GET'])
def home():
    return  render_template("index.html")

@app.route('/process',methods=['POST'])
def process():
    prince=request.form['name']
    princess=request.form['pname']
    boy=(len(prince))
    girl=(len(princess))
    rnd=random.randint(1,20)
    percentage=100-(boy*girl)-rnd
    data=mytable(name=prince,name2=princess,percentage=percentage)
    db.session.add(data)
    db.session.commit()
    return render_template("result.html",result=percentage)





if __name__=='__main__':
    app.run()
