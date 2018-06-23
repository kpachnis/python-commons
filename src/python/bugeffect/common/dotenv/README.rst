dotenv
======

**dotenv** will read the contents of a json file and export them as
environment variables.

The default file name is ``.env``; for an alternative use
``dotenv.load('filename')``.

Django usage
------------

In the manage.py and/or wsgi.py add

.. code:: python

   import dotenv

   dotenv.load()

Django notes
~~~~~~~~~~~~

Because the environment variables are exported as strings, if you set
``DEBUG`` to any value, it will always be ``True``.

For production deployments you could just not set ``DEBUG``, and in the
``settings.py`` file, set it to ``False``.

.. code:: python

   DEBUG = os.getenv('DEBUG', False)

An alternative approach is, to set ``DEBUG`` to either 0 or 1.

``0 -> False``, ``1 -> True``.

Then, in the ``settings.py`` file you can convert the ``DEBUG``
environment variable to a boolean value as in the following example

.. code:: python

   DEBUG = bool(int(os.getenv('DEBUG', False)))

Example JSON file
~~~~~~~~~~~~~~~~~

.. code:: json

   {
     "DEBUG": 1,
     "DATABASE_URL": "postgres://db_user:db_pass@db_host/db_name",
     "MEDIA_ROOT": "/srv/www.example.com/media",
     "STATIC_ROOT": "/srv/www.example.com/static"
   }
