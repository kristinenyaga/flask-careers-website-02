from flask import Flask,render_template
from flask.json import jsonify

app = Flask(__name__, static_folder='static')
JOBS=[
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Delhi,India',
        'salary':'Rs. 15,000'
    },
        {
        'id':1,
        'title':'Backend Developer',
        'location':'Delhi,India',
        'salary':'Rs. 15,000'
    },
        {
        'id':1,
        'title':'frontend developer',
        'location':'Delhi,India',
        'salary':'Rs. 18,000'
    },
    {
        'id': 1,
        'title': 'Data scientist',
        'location': 'Delhi,India',
        'salary': 'Rs. 17,000'
    }
]
@app.route('/')
def home():
    return render_template('home.html',jobs=JOBS)
@app.route('/api/jobs')
def jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)
