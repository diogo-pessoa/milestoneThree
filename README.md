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

- [FEATURES.md](/UserStories.md)

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
    - [Flask_blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
      - to improve code organization, by build a more module structure on the project
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
    - [MagicMock](https://docs.python.org/3/library/unittest.mock.html)
- Deployment
  - [heroku](http://heroku.com)
- Data Storage
    - [MongoDb](https://www.mongodb.com/) 
        - Data storage technology of choice
    - [flask-pymongo](https://flask-pymongo.readthedocs.io/en/latest/) 
        - package to support mongo data manipulation.
    - [mongo local docker image](https://hub.docker.com/_/mongo/)
    - [mongoTools(Dump/Restore)](https://docs.mongodb.com/database-tools/mongorestore/) 
    
- Local development tools
    - IDE [PyCharm](https://www.jetbrains.com/pycharm/)
    - [docker]()
    - [docker-compose]()
    - [brew]() 
    
## Deployment 
    
[DEPLOY.md](https://github.com/diogo-pessoa/the-bookshelf/blob/master/DEPLOY.md)

## local development

## Testing

Once you have your local environment setup follow the steps on the Testing document to run tests frequently and avoid regression.

- [TESTING.md](https://github.com/diogo-pessoa/the-bookshelf/blob/master/TESTING.md)

## Credits 

### Content 

#### Images:

[default_book_cover_image](https://pixabay.com/vectors/book-cover-education-layout-page-307045/) from [pixabay](https://pixabay.com/) 

### Acknowledgements

Ideas in app structure and data management inspired by the miguel Grinberg's [flask mega-tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

- [login_required decorator](https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/)

- [get_config_function_for_unittesting](https://stackoverflow.com/questions/56029111/how-do-i-mock-pymongo-for-testing-with-a-flask-app)
  - Useful for setting up unittest framework in order to Mock MongoPy calls. Once TestConfig is loaded and imported to test. I was able to user `MagicMock` to return mock values from database calls