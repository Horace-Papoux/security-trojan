FROM python:3.11

WORKDIR /code

# Install pipenv
RUN pip install pipenv

# Copy Pipfile and Pipfile.lock to container, from api folder
COPY Pipfile Pipfile.lock /code/

# Change directory to /code
WORKDIR /code

# Install dependencies
RUN pipenv install

# Copy project files to container
COPY ./api /code/

# Setup database (run ./api/src/db/init_db.py)
RUN pipenv run python src/db/init_db.py

# Export flask app
ENV FLASK_APP=app

# Run the flask application
CMD ["pipenv", "run", "python", "app.py"]