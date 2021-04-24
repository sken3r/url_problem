# URL Shortener
Create a URL shortener using django and postgres with tracing functionality

## Install dependencies
Use Make target to set up the virtual env:
`make install-dependencies`

Open your favorite IDE import the project, and you should be ready to go

## Run the project in a docker container

* Run `docker-compose build`
* Run `docker-compose up`

## Run the project on your local machine
From command line:

* Source the new built env `source .venv/bin/activate`

* Run migrations before running the project `python manage.py migrate`

* Run the server `python manage.py runserver`

## How to use
Once you chose your favorite method to run the project and it is up and running you can run the following command to see it in action. 

 Call `shorten_url/` with your favorite URL, and see the magic happening

### Example:
```
curl --header 'application/x-www-form-urlencoded' -XPOST -d'url=https://docs.djangoproject.com/en/3.1/' http://127.0.0.1:8000/shorten_url/
```
