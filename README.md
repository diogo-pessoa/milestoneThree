The Bookshelf
---

The Bookshelf site: [visit here](#the-bookshelf).

A project to review books you read, leave reviews, rate your best reads. Share your favourite choices.

#### Description


## UX

### color Scheme & Typography 

Using Materilize for a responsive front-end. 

- Color Scheme from [materializecss color Scheme](https://materializecss.com/color.html)

    - [lighter](#readme-content/colorScheme/Lighter.png)
    - [brown](#readme-content/colorScheme/darker.png)


### Entity Relationship Model

- [Diagram](#readme-content/er_diagram.png)

### Wireframes

#### Mobile view 

- [Login](wireframes/Mobile/Login_Mobile.png)
- [Register](wireframes/Mobile/Register_Mobile.png)
- [Book](wireframes/Mobile/Book_Mobile.png)
- [Profile](wireframes/Mobile/Profile_Mobile.png)

#### Desktop view 

- [Login](wireframes/Desktop/Login.png) 
- [Register](wireframes/Desktop/Register.png)
- [Book](wireframes/Desktop/Book.png)
- [Profile](wireframes/Desktop/Profile.png)

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
- Data Storage
    - [MongoDb](https://www.mongodb.com/)
- Front-End
    - [materialize](https://materializecss.com/)
    - [font awesome](https://fontawesome.com/)
    - [Jquery](https://jquery.com/)

- Testing
    - [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/)
    - [geckodriver](https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path)
    - [selenium](https://selenium-python.readthedocs.io/locating-elements.html#locating-elements)
    - [unittest](https://docs.python.org/3/library/unittest.html)
    
## Deployment 
    
Not Deployed Yet

## local development

[python3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) are required to run the local development environment.

- Setup Local environment


    python -m venv ./venv/
    source venv/bin/activate
- Install dependencies
  

    brew install geckodriver (on MacOs, Required to run Selenium tests with Firefox)
    pip install -r requirements_dev.txt (requirements_dev has extra dependecies for seleniums, not needed on production App.)

- create env.py file

    
    os.environ.setdefault("IP", "0.0.0.0")
    os.environ.setdefault("PORT", "")
    os.environ.setdefault("SECRET_KEY", "")
    # Ideally you setup a separate Database to store DevContent
    os.environ.setdefault("MONGO_URI", "mongodb+srv://<url>")
    os.environ.setdefault("MONGO_DBNAME", "")

- Run app
  

    # run flask app
    python3 app.py
    open http://http://127.0.0.1:5000/

## Testing

Once you have your local environment setup follow the steps on the Testing document to avoid regression during development

- [TESTING.md](/TESTING.md)

## Credits 

### Content 

### Acknowledgements

