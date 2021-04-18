Tests
---

## Techonologies used:

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
  
  