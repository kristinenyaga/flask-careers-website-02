import sqlalchemy
from sqlalchemy import create_engine,text
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv() 

password = os.environ['MYSQLPASSWORD']
username = os.environ['MYSQLUSERNAME']

engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@localhost/careersDb")

def load_jobs():
    connection = engine.connect()
    result = connection.execute("SELECT * FROM jobs")
    jobs = [dict(row) for row in result.all()]
    return jobs


def load_job(id):
    with engine.connect() as conn:
       query = "SELECT * FROM jobs WHERE id = :job_id"
       result = conn.execute(text(query), job_id=id)
       job = result.all()
       if len(job) == 0:
           return None
       else:
          return(dict(job[0]))


def apply_job(application,id):
    with engine.connect() as conn:
       query = """
    INSERT INTO applications (job_id, full_name, email, education, work_experience, resume_url, linkedin_url)
    VALUES (:job_id, :full_name, :email, :education, :work_experience, :resume_url, :linkedin_url)
    """

       result = conn.execute(text(query),
                              job_id=id,
                              full_name=application['full_name'],
                              email=application['email'],
                              work_experience=application['work_experience'],
                             resume_url=application['resumeurl'],
                             linkedin_url=application['linkedinurl'],
                             education=application['education']
                             )

# with engine.connect() as conn:
#   result = conn.execute(text("SELECT * FROM jobs"))
#   print("type of result.all()",type(result.all()))
#   print("type of result",type(result))
#   result_all= result.all()
#   print(result_all)
