from django.core.files.storage import Storage

from google.appengine.ext import db

from gaeblob_storage.models import BlobPropertyFile

class BlobPropertyStorage(Storage):
    def _save(self, name, content):
        path = self.path(name)
        blob = BlobPropertyFile(key_name=path)
        blob.content = content.read()
        blob.put()
        return path

    def exists(self, name):
        if BlobPropertyFile.get_by_key_name(self.path(name)):
            return True
        else:
            return False

    def _open(self, name, mode='rb'):
        return BlobPropertyFile.get_by_key_name(self.path(name))

    def delete(self, name):
        BlobPropertyFile.get_by_key_name(self.path(name)).delete()

    def path(self, name):
        return name.strip()
