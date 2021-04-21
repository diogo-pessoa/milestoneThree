Tests
---

## Technologies used:

## Selenium 
With the local Application Running

    flask run
    python -m unittest discover -s test/html_test -p "*_test.py" -v

## UnitTest

    python -m unittest discover -s test/ -p "*_test.py" -v


## Tests
    
- Pymongo 

**Error** `The "dnspython" module must be installed to use mongodb+srv:// URIs`

**Fix** [GitHub issue](https://github.com/getredash/redash/issues/2603)

- **Problem** the basic `app.py` caused a few problems with circular dependencies when running flaks locally. [The Flask mega-tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
suggests an alternative app structure to exactly to avoid this problem. 
  **Fix** breaking down the `app.py` file into a routes.py and `__init__.py` loading the packages in the right order. This is to save time in later, as I plan to break down the code in to a few different modules.
  
- As now I'm using `flask run` to update port and host, it is needed to set the proper environment variables
  - flask load variables: [blog post](https://prettyprinted.com/tutorials/automatically_load_environment_variables_in_flask) 
  - **Fix** adding following variables to `.flaskenv`
    
        
      FLASK_RUN_PORT=5000
      FLASK_RUN_HOST=0.0.0.0
      Environment=Development
      FLASK_APP=thebookshelf.py
  
  
- **Problem** moving menu on smaller screen to right side. 
  - **Fix** from [CodeInstitute class](https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/02-UserAuthenticationAndAuthorization/02-register_page/static/js/script.js) included attribute `edge: right`
    to `js` file. 
    

### Automated Test

- [test/html_test](https://github.com/diogo-pessoa/the-bookshelf/blob/master/test/html_test)
  - [links_test.py](https://github.com/diogo-pessoa/the-bookshelf/blob/master/test/html_test/links_test.py)
    
    This test the links on Nav_bar, by loading the index page and clicking on the link, defined on each test. Test then waits for the page to load and checking for an HTML element on target page.
    