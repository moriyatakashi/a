from flask import*
from flask_sqlalchemy import*
from datetime import*
app=Flask(__name__)
db_uri="sqlite:///test2.db"
app.config["SQLALCHEMY_DATABASE_URI"]=db_uri
db=SQLAlchemy(app)
class Article(db.Model):
  id=db.Column(db.Integer,primary_key=True,autoincrement=True)
  pub_date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
  name=db.Column(db.String(80))
  article=db.Column(db.Text())
  thread_id=db.Column(db.Integer,db.ForeignKey('thread.id'),nullable=False)
  def __init__(self,pub_date,name,article,thread_id):
    self.pub_date=pub_date
    self.name=name
    self.article=article
    self.thread_id=thread_id
class Thread(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  threadname=db.Column(db.String(80),unique=True)
  article=db.relationship('Article',backref='thread',lazy=True)
  def __init__(self,threadname,article=[]):
    self.threadname=threadname
    self.article=article
@app.route("/")
def main():
  threads=Thread.query.all()
  return render_template("index.html",threads=threads)
if __name__=="__main__":app.run()