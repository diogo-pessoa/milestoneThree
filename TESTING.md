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
  - **Fix**
    from [CodeInstitute class](https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/02-UserAuthenticationAndAuthorization/02-register_page/static/js/script.js)
    included attribute `edge: right`
    to `js` file.

### Automated Test

- [test/html_test](https://github.com/diogo-pessoa/the-bookshelf/blob/master/test/html_test)
  - [links_test.py](https://github.com/diogo-pessoa/the-bookshelf/blob/master/test/html_test/links_test.py)

    This test the links on Nav_bar, by loading the index page and clicking on the link, defined on each test. Test then
    waits for the page to load and checking for an HTML element on target page.


- [test/html_test](https://github.com/diogo-pessoa/the-bookshelf/blob/master/test/html_test)
  - [login_page_test.py](https://github.com/diogo-pessoa/the-bookshelf/blob/master/test/html_test/login_page_test.py)

    This automates basic checks on Login page.
    - Fills and submits Login form
    - Check if NavBar is updates with conditional `Log out` link
    - Clicks Log out navbar link
    - Asserts `Login` link is available on NavBar

- [test/src/bookshelf](https://github.com/diogo-pessoa/the-bookshelf/blob/master/test/src/bookshelf)

  This Directory has all Unittests:


        python -m unittest discover -s test/src/bookshelf -p "*_test.py" -v
          test_get_object_dict (review_test.ReviewTest) ... ok
          test_check_password (user_test.UserTest) ... ok
          test_get_dict (user_test.UserTest) ... ok
          test_get_favorite_books (user_test.UserTest) ... ok
          test_get_user_first_name (user_test.UserTest) ... ok
          test_get_user_last_name (user_test.UserTest) ... ok
          test_get_username (user_test.UserTest) ... ok
          test_is_moderator (user_test.UserTest) ... ok
          
          ----------------------------------------------------------------------
          Ran 8 tests in 0.169s
          
          OK



- [test/html_test/profile_page_test](https://github.com/diogo-pessoa/the-bookshelf/blob/master/test/html_test/profile_page_test.py)
  
extended test to look for tabs on Profile Page Body 
  - After Login Action clicks on different tabs and confirm table content was loaded from DB with test user content
    - while running test It exposed the bugs listed:
      - **Bugfix** for My favorite_books.html page, missing Books object
        - Due to the refactoring on User() and model, changes were need on the page `my_favorite_books` template to properly load the book name
        - Adding books variable to profile page view and looping through that variable on the page template
      - **BugFix** for my_reviews.html removing extra td from comment column 
        - Noticed content was dislocated to the right due to extra td element on template for loop

- **Bug**
  At Profile Page if user has not left a review yet footer was going ove table.
  - Fix added a div `row` to wrap include My_review.html template now even when table is empty space is in page is preserved
  - Test Login, navigate to profile, click on tab Reviews. 