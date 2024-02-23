from sqlalchemy import create_engine, text
import os

""" Create an engine."""
db_conn_str = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_conn_str,connect_args={
  "ssl": {
    "ssl_ca":"/etc/ssl/cert.pem"
  }
})

def row_to_dict(row):
  """
  Convert a SQLAlchemy row object to a dictionary.
  """
  return {key: getattr(row, key) for key in row._asdict()}


""" create a connection with the database and get jobs."""

def get_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from listings"))

    jobs = []
    for row in result:
      jobs.append(row_to_dict(row))

    return jobs

def get_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM listings WHERE id = :value"), value=id)
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return row_to_dict(rows[0])


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("insert into applications (job_id, full_name, email, linked_in url, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :resume_url")
    conn.execute(query, job_id=job_id, full_name=data['full_name'], email=data['email'], linkedin_url=data['linkedin_url'], resume_url=data['resume_url'],)