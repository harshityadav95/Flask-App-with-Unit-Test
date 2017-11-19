from flask import Flask,request, session
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hillwoods@localhost/test'
db=SQLAlchemy(app)
app.debug=True

class Mapinf(db.Model):
    key=db.Column(db.Text,primary_key=True)
    place_name=db.Column(db.Text)
    admin_name1=db.Column(db.Text)
    latitude=db.Column(db.Numeric)
    longitude=db.Column(db.Numeric)
    accuracy=db.Column(db.Integer)


    def __init__(self, key,place_name, admin_name1, latitude, longitude,accuracy):
        self.key=key
        self.place_name=place_name
        self.admin_name1=admin_name1
        self.latitude=latitude
        self.longitude=longitude
        self.accuracy=accuracy

    def __repr__(self):
        return '<User %r>'% self.admin_name1


@app.route('/')
def hello():
    return  render_template('add.html') 



@app.route('/post_location', methods=['POST'])
def post_ad():
     
    key=None
    key=request.form['key']
    latitude=request.form['latitude']
    longitude=request.form['longitude']

    if not db.session.query(Mapinf).filter((Mapinf.key == key) | (Mapinf.latitude == latitude), (Mapinf.longitude == longitude) ).count():
        loc=Mapinf(request.form['key'],request.form['place_name'],request.form['admin_name1'],request.form['latitude'],request.form['longitude'],request.form['accuracy'])
        #could have used abs (a-b)>0.01 to check aprrox lat +long values
        #round didnt work         
        db.session.add(loc)
        db.session.commit()
        return  render_template('ok.html')
    else:
         return  render_template('fail.html')

  

if __name__ == '__main__':
    app.run()
