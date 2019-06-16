from flask import flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# database location = using sqlite shop database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
# initalising database
db = SQLAlchemy(app)

class Todo(db.Model):
    email = db.column(db.String(30), primary_key=True)
    password = db.Column(db.String(20), nullable=False)

#can send and recieve information
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)