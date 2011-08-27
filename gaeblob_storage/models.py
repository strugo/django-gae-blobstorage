from google.appengine.ext import db


class BlobPropertyFile(db.Model):
    path = db.StringProperty()
    data = db.BlobProperty()
