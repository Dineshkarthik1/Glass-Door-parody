from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data analyst',
    'location': 'delhi',
    'salary':'rs.100000'
  },
  {
    'id': 2,
    'title':'Data scientist',
    'location': 'hyderabad',
    'salary': 'rs.150000'
  }
]

@app.route("/")
def home():
  return render_template('home.html', jobs=JOBS, company_name = 'GlassDoor Parody')

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(
    host='0.0.0.0',
    debug=True
  )
