from flask import Flask,render_template,request
from flask.json import jsonify
from database import load_jobs,load_job,apply_job
app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    jobs = load_jobs()
    return render_template('home.html',jobs=jobs)
@app.route('/api/jobs')
def jobs():
    return jsonify(jobs)

@app.route('/job/<id>')
def showjob(id:int):
    job=load_job(id)
    if not job:
        return 'Not Found',404
    else:
        requirements=job['requirements'].split('.')
        responsibilities = job['responsibilities'].split('.')
        return render_template('singlejob.html', job=job,requirements=requirements,responsibilities=responsibilities)


@app.route('/job/<id>/apply', methods=['POST'])
def applyjob(id):
    application = request.form
    apply_job(application,id)
    job=load_job(id)
    return render_template('applicationsubmitted.html',job=job,application=job)


if __name__ == '__main__':
    app.run(debug=True)
