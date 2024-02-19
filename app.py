from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Accountant',
    'location': 'Nairobi',
    'salary': 'Ksh. 70,000'
  },
  {
    'id': 2,
    'title': 'Mechanic',
    'location': 'Thika',
    'salary': 'Ksh. 50,000'
  },
  {
    'id': 3,
    'title': 'Teacher',
    'location': 'Kisumu',
    'salary': 'Ksh. 45,000'
  },
  {
    'id': 4,
    'title': 'Sous Chef',
    'location': 'Mombasa',
    'salary': 'Ksh. 70,000'
  },
]

@app.route("/")
def hello():
  return render_template("home.html", jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)