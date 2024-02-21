from sqlalchemy import create_engine, text
import os 
db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca : /etc/ssl/cert.pem"
    }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))

    return jobs

def load_job_from_db(id)
  with engine.connect() as conn
    result = conn.execute(text("select * from jobs where id = :value"), value=id)
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])
      

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("insert into applications (job_id, full_name, email, linked_in url, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :resume_url")
    conn.execute(query, job_id=job_id, full_name=data['full_name'], email=data['email'], linkedin_url=data['linkedin_url'], resume_url=data['resume_url'],)
  
                          
