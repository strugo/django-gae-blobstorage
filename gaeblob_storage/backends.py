from django.core.files.storage import Storage

from google.appengine.ext import db

from gaeblob_storage.models import BlobPropertyFile

class BlobPropertyStorage(Storage):
    def save(self, name, content):
        blob = BlobPropertyFile(key_name=name)
        blob.data = content.read()
        blob.put()
        return name

    def exists(self, name):
        if BlobPropertyFile.get_by_key_name(name):
            return True
        else:
            return False

    def open(self, name):
        return BlobPropertyFile.get_by_key_name(name)
