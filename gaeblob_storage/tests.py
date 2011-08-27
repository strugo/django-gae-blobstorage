from django.test import TestCase
from django.core.files.base import ContentFile

from gaeblob_storage.backends import BlobPropertyStorage


class HashPathStorageTest(TestCase):

    def setUp(self):
        self.storage = BlobPropertyStorage()

        self.content = 'test content'
        self.file = ContentFile(self.content)
        self.name = 'test'

    def tearDown(self):
        pass

    def test_save_file(self):
        path = self.storage.save(self.name, self.file)
        self.assertEqual(self.name, path)

    def test_open_file(self):
        path = self.storage.save(self.name, self.file)
        self.assertEqual(self.name, path)

        f = self.storage.open(path)
        self.assertEqual(self.content, f.content)
        
    def test_save_same_file(self):
        path_1 = self.storage.save(self.name, self.file)
        path_2 = self.storage.save(self.name, self.file)

        self.assertEqual(path_1, self.name)
        self.assertEqual(path_2, '%s_1'%(self.name))
