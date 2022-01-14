# Set the virtual environment

Create the virtual environment:

`python3 -m venv env`

Source it:

`source env/bin/activate`


Install librairies with pip and the requirements.txt file:
`python3 -m pip install -r requirements.txt`

# Initialize the database

Go to scripts, set the PYHTONPATH to include the src/ directory and run: python scripts/init_db.py

# Start the API

Once your database is created, move it to the base path of the repository (/jellysmack) and run:

`uvicorn src.main:app`

Follow the link http://127.0.0.1:8000 and use the swagger http://127.0.0.1:8000/docs.


# Personal comments
You will find for now the mandatory part of the project, meaning feature 1, 2 and 3.

Took me a day to do this.

This was done following a very basic git flow (manual one) workflow with according features branches following merge principle with no fast forward.
Tests were done using pytest and can be run directly with the pytest command after setting the right PYTHONPATH containing the src/ directory.
Script to launch them directly would have been easier, next step. 

Speaking of next steps, you will see in what has been done lots of stuff I would have improved later on such as:
- import style (Try to keep import in the simplest way, avoiding then confusion inside the code itself)
- Docstrings are missing and should be done carefully, to be processed by Sphinx having proper developer documentation.
- Tests have been started but not covering the entire code
- HTTP Exceptions handling have been neglected, and must not
- and so on to discuss ...

What has been chosen:
- I tried to split as possible the different part of the API, when necessary and in the smartest way possible (at least for me).
- Pydantic schemas have been implemented bringing the API more control over what is processed (even if it remains quite simple for now).
- Sqlite has been chosen to be quicker but must of course not to be put in production. Would have chosen Postgresql.
- I decided not to use typed python on purpose, as I don't consider it to be a better choice all the time and to be quicker. Might enforce robustness if to be in production
- About the database initialization script, I used both sqlite3 and SQLAchemy because it helped me to validate my models and found it easier as I am more familiar with Python than with SQL.
