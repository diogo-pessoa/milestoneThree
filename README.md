The Bookshelf
---

The Bookshelf site: [visit here](https://the-bookshelf-milestone-three.herokuapp.com/).

A project to review books you read, leave reviews, rate your best reads. Share your favourite choices.

#### Description


## UX

### color Scheme & Typography 

Using Materilize for a responsive front-end. 

- Color Scheme from [materializecss color Scheme](https://materializecss.com/color.html)

    - Lighter
        
        ![lighter](https://github.com/diogo-pessoa/the-bookshelf/blob/master/readme-content/colorScheme/Lighter.png)

    - Darker
    
        ![brown](https://github.com/diogo-pessoa/the-bookshelf/blob/master/readme-content/colorScheme/darker.png)


### Entity Relationship Model

- [Diagram](https://github.com/diogo-pessoa/the-bookshelf/blob/master/readme-content/er_diagram.png)

### Wireframes

#### Mobile view 

- [Login](https://github.com/diogo-pessoa/the-bookshelf/blob/master/wireframes/Mobile/Login_Mobile.png)
- [Register](https://github.com/diogo-pessoa/the-bookshelf/blob/master/wireframes/Mobile/Register_Mobile.png)
- [Book](https://github.com/diogo-pessoa/the-bookshelf/blob/master/wireframes/Mobile/Book_Mobile.png)
- [Profile](https://github.com/diogo-pessoa/the-bookshelf/blob/master/wireframes/Mobile/Profile_Mobile.png)

#### Desktop view 

- [Login](https://github.com/diogo-pessoa/the-bookshelf/blob/master/wireframes/Desktop/Login.png) 
- [Register](https://github.com/diogo-pessoa/the-bookshelf/blob/master/wireframes/Desktop/Register.png)
- [Book](https://github.com/diogo-pessoa/the-bookshelf/blob/master/wireframes/Desktop/Book.png)
- [Profile](https://github.com/diogo-pessoa/the-bookshelf/blob/master/wireframes/Desktop/Profile.png)

## Features 

For User Stories and Features 

- [FEATURES.md](/FEATURES.md)

## Technologies Used 

- Design 
    - [balsamiq](https://balsamiq.com/)
        - to Build wireframes
    - [LucidCharts](https://www.lucidchart.com/) 
        - to build entity relationship diagram
- Application
    - [python3](https://www.python.org)
    - [pip](https://pypi.org/project/pip/)
      - installs project dependencies
    - [Flask](https://flask.palletsprojects.com/en/1.1.x/)
      - Python http micro framework  
    - [venv](https://docs.python.org/3/library/venv.html)
        - For a clean local development environment
- Front-End
    - [materialize](https://materializecss.com/)
    - [font awesome](https://fontawesome.com/)
    - [Jquery](https://jquery.com/)

- Testing
    - [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/)
    - [geckodriver](https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path)
    - [selenium](https://selenium-python.readthedocs.io/locating-elements.html#locating-elements)
    - [unittest](https://docs.python.org/3/library/unittest.html)
- Deployment
  - [heroku](dashboard.heroku.com)
- Data Storage
    - [MongoDb](https://www.mongodb.com/)
    
## Deployment 
    
App is deployed using heroku.

I have linked the github repository to The heroku and enabled automatic deploys. Hence, when a commit reaches master. It will automatically release a new version. 

#### Steps:
- `Login` to heroku [login](https://id.heroku.com/login)
- On `Landing Page`  click on create a new app [image](https://github.com/diogo-pessoa/the-bookshelf/blob/master/readme-content/heroku-deploy/createNewApp.png)
- After you click on  `create new App` Add information related to your app [image](https://github.com/diogo-pessoa/the-bookshelf/blob/master/readme-content/heroku-deploy/App_info.png)
- On tab `Deploy` link your account with github [image](https://github.com/diogo-pessoa/the-bookshelf/blob/master/readme-content/heroku-deploy/link_account_to_github.png)
- On tab `Deploy` run a manual Deploy from master branch [image](https://github.com/diogo-pessoa/the-bookshelf/blob/master/readme-content/heroku-deploy/manual_deploy.png)
- On tab `Settings` Setup Config Vars with environment variables [image](https://github.com/diogo-pessoa/the-bookshelf/blob/master/readme-content/heroku-deploy/config_vars.png)
- Check Logs through the UI [image](https://github.com/diogo-pessoa/the-bookshelf/blob/master/readme-content/heroku-deploy/check_log_UI.png)
    - or CLI: `#heroku logs --tail --app the-bookshelf-milestone-three`
    - content should be similar to the following

            2021-04-12T19:52:15.000000+00:00 app[api]: Build started by user
            2021-04-12T19:52:41.897820+00:00 app[api]: Deploy 76b4e2a6 by user com
            2021-04-12T19:52:41.918465+00:00 app[api]: Scaled to web@1:Free by user 
            2021-04-12T19:52:41.897820+00:00 app[api]: Release v9 created by user 
            2021-04-12T19:52:48.856622+00:00 heroku[web.1]: Starting process with command `python app.py`
            2021-04-12T19:52:51.000000+00:00 app[api]: Build succeeded

- On `Deploy` tab Enable auto deploy from master branch [image](https://github.com/diogo-pessoa/the-bookshelf/blob/master/readme-content/heroku-deploy/automatic_deploy.png)

## local development

- [python3](https://www.python.org/downloads/) 
- [pip](https://pip.pypa.io/en/stable/installing/) 

Required to run the local development environment.

- Setup Local environment

        python -m venv ./venv/
        source venv/bin/activate

- Install dependencies
  
            brew install geckodriver 
    
    on MacOs, Required to run Selenium tests with Firefox
    
            pip install -r requirements_dev.txt 
        
    (requirements_dev has extra dependencies for selenium, not needed on production App.)

- create `.flaskenv` file
  
The project uses `python-dotenv` to load environment variables, set the variable on a local `.flaskenv`
    make sure to add this file to `.gitignore` as it may eventually hold sensitive data

        FLASK_APP=thebookshelf.py
        DEBUG=True
        IP=0.0.0.0
        PORT=5000

- Run app
  

        #run flask app
        flask run 
        open http://http://127.0.0.1:5000/

## Testing

Once you have your local environment setup follow the steps on the Testing document to run tests frequently and avoid regression.

- [TESTING.md](/TESTING.md)

## Credits 

### Content 

### Acknowledgements

Constantly used recommendations from the miguel Grinberg's [flask mega-tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

