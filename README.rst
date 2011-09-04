Django-gae-blobstorage
=======================

A Django storage backend that uses Google App Engine's BlobProperty_ to store files to the Google App Engine 
Datastore.

It only works on Google App Engine and you will also need the Djangoappengine_ backend for Django-Nonrel_.

Datastore entities on Google App Engine can't be bigger than 1 MB, so files stored using django-gae-blobstorage can't be lager than 
1 MB too!

Installation
====================================

* get the code:

    git clone https://fhahn@github.com/fhahn/django-gae-blobstorage.git
   


* set *DEFAULT_FILE_STORAGE* to **gaeblob_storage.backends.BlobPropertyStorage** and 
  add **gaeblob_storage** to your *INSTALLED_APPS*

  settings.py::

      DEFAULT_FILE_STORAGE = 'gaeblob_storage.backends.BlobPropertyStorage'

      INSTALLED_APPS = (      
          ...
          'gaeblob_storage',
      )

* include **gaeauth.urls** in your urlconf to **login**, **logout** and **authenticate**
  
  urls.py::
   
    urlpatterns = patterns('',
         ...
         (r'^files/', include('gaeblob_storage.urls')),
    )

* the file **bar.jpg**  can be accessed via */files/serve/bar.jpg*


Urls
========

Django-gae-blobstorage provides following named urls:

gaeblob_serve
  serves the requested file


Usage 
=====================

*FileFields* and *ImageFields* are now storing files as BlobProperties in the GAE Datastore and behave like files
saved to the a file system.

.. _BlobProperty: https://code.google.com/appengine/docs/python/datastore/typesandpropertyclasses.html#BlobProperty
.. _Djangoappengine: http://www.allbuttonspressed.com/projects/djangoappengine
.. _Django-Nonrel: http://www.allbuttonspressed.com/projects/django-nonrel
