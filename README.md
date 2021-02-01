# advance-ticket-system
Support Centre - Advanced Django Ticket System

To run locally, do the usual:

#. Create a Python 3.6 virtualenv

#. Install dependencies::

    pip install -r requirements.txt
    
#. Migrate database access
    ./manage.py migrate

#. Create a superuser::

   ./manage.py createsuperuser

#. Populate the www and docs hostnames in the django.contrib.sites app::

   ./manage.py loaddata fixtures/file_name.json

#. Run
 ./manage.py runserver
 
http://127.0.0.1:8000 
