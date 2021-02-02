# advance-ticket-system
Support Centre - Advanced Django Ticket System

<p align="center">
  <img width="800" height="600" src="https://github.com/cseshahriar/advance-ticket-system/blob/main/docs/screenshoot.png">
</p>

To run locally, do the usual:

#. Create a Python 3.9 virtualenv
    
    python3 -m venv env_name

#. Install dependencies::

    pip install -r requirements.txt
    
#. Migrate database access
    
    ./manage.py migrate

#. Create a superuser::
   
    ./manage.py createsuperuser

#. Loaddata:

    ./manage.py loaddata fixtures/file_name.json

#. Runserver 

    ./manage.py runserver
 
    http://127.0.0.1:8000 
