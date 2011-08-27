from google.appengine.ext import db


class BlobPropertyFile(db.Model):
    content = db.BlobProperty()
