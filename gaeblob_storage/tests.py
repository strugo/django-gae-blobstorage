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

    def test_open_existing_file(self):
        path = self.storage.save(self.name, self.file)
        self.assertEqual(self.name, path)

        f = self.storage.open(path)
        self.assertEqual(self.content, f.content)

    def test_open_invalid_file(self):
        f = self.storage.open('foo bar')
        self.assertEqual(f, None)

    def test_exists_existing_file(self):
        path = self.storage.save(self.name, self.file)
        self.assertTrue(self.storage.exists(path))

    def test_exists_invalid_file(self):
        self.assertFalse(self.storage.exists('foo bar'))

    def test_delete_existing_file(self):
        self.test_exists_existing_file()
        self.storage.delete(self.name)
        self.assertFalse(self.storage.exists(self.name))

    def test_save_same_file(self):
        path_1 = self.storage.save(self.name, self.file)
        path_2 = self.storage.save(self.name, self.file)

        self.assertEqual(path_1, self.name)
        self.assertEqual(path_2, '%s_1'%(self.name))
