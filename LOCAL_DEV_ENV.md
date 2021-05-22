

## setup mongo


Configure a local password for your mongo DB on [docker-compose.yml](https://github.com/diogo-pessoa/the-bookshelf/blob/master/docker-compose.yml)
  update [.flaskenv](https://github.com/diogo-pessoa/the-bookshelf/blob/master/flaskenv.sample) with `MONGO_URI=mongodb://<user>>:password@localhost:27017/thebookshelf`
  note: user and password have to correspond to docker-compose.yml value.

## Run mongoDB container

        
        #with docker service running localy and docker-compose installed
        # RUn from project root dir, docker-compose looks for file named docker-compose.yml
        docker-compose up

## Restore DB 
Once container is running, use mongodb-database-tools to load the dump of the sample db  
  
    
    brew install mongodb-database-tools    
    mongorestore --host=localhost:27017 --password=example --user=root    

## Activate virtual environment

        python -m venv ./venv/
        source venv/bin/activate

## Install dependencies
  
            brew install geckodriver 
    
    on MacOs, Required to run Selenium tests with Firefox
              
            pip install -r requirements_dev.txt 
        
    **Note:** requirements_dev has extra dependencies for selenium, not needed on production App, hence two separate files

## create `.flaskenv` file
  
The project uses `python-dotenv` to load environment variables, set the variable on a local `.flaskenv`
    make sure to add this file to `.gitignore` as it may eventually hold sensitive data

        DEBUG=True
        FLASK_RUN_PORT=5000
        FLASK_RUN_HOST=localhost
        Environment=Development
        FLASK_APP=thebookshelf.py
        MONGO_URI=MONGO_URI=mongodb://example:example@localhost:27017/thebookshelf

## Run flask
  
        
        #https://flask-pymongo.readthedocs.io/en/latest/
        #run flask app
        flask run 
        open http://http://127.0.0.1:5000/