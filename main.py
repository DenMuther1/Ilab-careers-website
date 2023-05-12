from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Nairobi',
  'salary': 'Ksh 100,000'
}, {
  'id': 2,
  'title': 'Front End Developer',
  'location': 'Remote',
  'salary': 'Ksh 200,000'
}, {
  'id': 3,
  'title': 'Back End Developer',
  'location': 'Kisumu',
}, {
  'id': 4,
  'title': 'Data Engineer',
  'location': 'Mombasa',
  'salary': 'Ksh 300,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs=JOBS,
                         company_name='Ilab Technologies')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
