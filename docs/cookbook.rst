========
Cookbook
========

Amazon
------

Using eu-west-1
^^^^^^^^^^^^^^^

.. code-block:: python

    LIBCLOUD_PROVIDERS = {
        'default': {
            'type': 'libcloud.storage.types.Provider.S3_EU_WEST',
            'user': os.environ.get('AWS_ACCESS_KEY'),
            'key': os.environ.get('AWS_SECRET_KEY'),
            'bucket': 'my-assets',
            'base_url': 'https://s3-eu-west-1.amazonaws.com/my-assets/',
        },
    }

    DEFAULT_FILE_STORAGE = 'djlibcloud.providers.default'
    MEDIA_URL = LIBCLOUD_PROVIDERS['default']['base_url']

    STATICFILES_STORAGE = 'djlibcloud.providers.default'
    STATIC_URL = LIBCLOUD_PROVIDERS['default']['base_url']

Google Cloud Storage
--------------------

.. code-block:: python

    LIBCLOUD_PROVIDERS = {
        'default': {
            'type': 'libcloud.storage.types.Provider.GOOGLE_STORAGE',
            'user': os.environ.get('GOOGLE_ACCESS_KEY'),
            'key': os.environ.get('GOOGLE_SECRET_KEY'),
            'bucket': 'my-assets',
            'base_url': 'https://storage.googleapis.com/my-assets/',
        },
    }

    DEFAULT_FILE_STORAGE = 'djlibcloud.providers.default'
    MEDIA_URL = LIBCLOUD_PROVIDERS['default']['base_url']

    STATICFILES_STORAGE = 'djlibcloud.providers.default'
    STATIC_URL = LIBCLOUD_PROVIDERS['default']['base_url']

Rackspace Cloudfiles
--------------------

.. code-block:: python

    LIBCLOUD_PROVIDERS = {
        'default': {
            'type': 'libcloud.storage.types.Provider.CLOUDFILES',
            'user': os.environ.get('RACKSPACE_USER_NAME'),
            'key': os.environ.get('RACKSPACE_API_KEY'),
            'bucket': 'my-assets',
            'base_url': 'https://<long>-<hash>.ssl.cf5.rackcdn.com',
        },
    }

    DEFAULT_FILE_STORAGE = 'djlibcloud.providers.default'
    MEDIA_URL = LIBCLOUD_PROVIDERS['default']['base_url']

    STATICFILES_STORAGE = 'djlibcloud.providers.default'
    STATIC_URL = LIBCLOUD_PROVIDERS['default']['base_url']

Microsoft Azure
---------------

.. code-block:: python

    AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME')
    LIBCLOUD_PROVIDERS = {
        'default': {
            'type': 'libcloud.storage.types.Provider.AZURE_BLOBS',
            'user': AZURE_ACCOUNT_NAME,
            'key': os.environ.get('AZURE_ACCOUNT_KEY'),
            'bucket': 'my-assets',
            'base_url': 'https://%s.blob.core.windows.net/my-assets/' % AZURE_ACCOUNT_NAME,
        },
    }

    DEFAULT_FILE_STORAGE = 'djlibcloud.providers.default'
    MEDIA_URL = LIBCLOUD_PROVIDERS['default']['base_url']
    # or
    STATICFILES_STORAGE = 'djlibcloud.providers.default'
    STATIC_URL = LIBCLOUD_PROVIDERS['default']['base_url']

Using django-pipeline
----------------------

.. code-block:: python

    # core/storage.py

    from djlibcloud.storage import LibCloudStorage
    from pipeline.storage import PipelineMixin

    class PipelineCloudStorage(PipelineMixin,
                               LibCloudStorage):
        """ UNTESTED! """
        pass

.. code-block:: python

    # settings.py
    LIBCLOUD_PROVIDERS = {
        'static': {
            'class': 'core.storage.PipelineCloudStorage',
            'type': ...
        },
    }

    STATICFILES_STORAGE = 'djlibcloud.providers.static'
    STATIC_URL = LIBCLOUD_PROVIDERS['static']['base_url']
