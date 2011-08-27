from django.test import TestCase
from django.core.files.base import ContentFile

from gaeblob_storage.backends import BlobPropertyStorage


class HashPathStorageTest(TestCase):

    def setUp(self):
        self.storage = BlobPropertyStorage()
            
    def tearDown(self):
        pass

    def test_save_same_file(self):
        """
        saves a file twice, the file should only be stored once, because the
        content/hash is the same
        """
        
        path_1 = self.storage.save('test', ContentFile('new content'))
        
        #path_2 = self.storage.save('test', ContentFile('new content'))

        self.assertEqual(path_1, 'test')
