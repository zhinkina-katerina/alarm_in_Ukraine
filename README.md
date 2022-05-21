# Alarm in Ukraine
This project was created based on API https://alerts.com.ua/en.

The purpose of this project is to display air alerts in the regions of Ukraine.

The frequency of alarms is presented as a chart, from the smallest number of alarms to the largest.
Data can be viewed for all time, for a week, and also for 24 hours.

Data update frequency - 5 minutes.

# Technology

- Python 3.7

- Django 3.2.13

- Celery + Redis

- Postgresql

- Heroku


# Installation 
##Local

1. Clone the repository

2. Create a virtual environment in the root folder `python -m venv venv`

3. Activate the virtual environment `venv\Scripts\activate.bat`

4. Install the dependencies `pip install -r requirements.txt`

5. Copy and fill in with your data `cp .env.example .env`

6. Run database migrations `python manage.py migrate`

7. Start seeding the database `python states_siding.py`

8. In terminal-1 run celery-beat
`celery -A alarm_in_Ukraine beat`

9. ВIn terminal-2 run celery worker
`celery -A alarm_in_Ukraine worker -l INFO`

10. To start the server, enter `python manage.py runserver`


##Heroku
1. Set up environment variables Heroku in Setting/Config_Vars

2. Log in to your Heroku

3. Use Git to clone app's source code to your local machine

4. Deploy app to Heroku using Git - `git push heroku main`




