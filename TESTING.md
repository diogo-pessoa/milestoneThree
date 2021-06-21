Tests
---

## Technologies used:


### database for Test

All Integration tests(selenium Tests), were written based on collections on [/dump](https://github.com/diogo-pessoa/the-bookshelf/blob/master/dump) folder. If you are running this for the first time, Install mongo `database-tools` [installation_doc](https://docs.mongodb.com/database-tools/installation/installation/) 

and run a mongo restore as described below. 



```
 creates a new database or adds data to an existing database. By default, mongorestore reads the database dump in the dump/ sub-directory 
 of the current directory; to restore from a different directory, pass in the path to the directory as a final argument.
```


     mongorestore --host=localhost:27017 --password=example --username=root
     

### Selenium tests 

With the local Application Running and [.flaskenv](https://github.com/diogo-pessoa/the-bookshelf/blob/master/flaskenv.sample) setting the proper credentials see [local Development](https://github.com/diogo-pessoa/the-bookshelf/blob/master/TESTING.md##local-development) to setup flask locally 
    
    
    flask run
    # to test each view individually
    python -m unittest discover -s test/html_test/main -p "*_test.py" -v 
    python -m unittest discover -s test/html_test/auth_view -p "*_test.py" -v 
    python -m unittest discover -s test/html_test/book_view -p "*_test.py" -v 
    python -m unittest discover -s test/html_test/user_view -p "*_test.py" -v 

    # TO run all test
    python -m unittest discover -s test/html_test/*_view -p "*_test.py" -v  

## UnitTest
    
    # make sure to export the .flaskenv variable. The pymongo model, relies on app and mongo. 
    # The test pre-loads these in order to mock the call to the  method that invokes Application  Models 
    python -m unittest discover -s test/src/bookshelf -p "*_test.py" -v


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

### Bugs

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
  
- **Bug** If a user tried know the profile path `/profile/user` he can see anybody's profile page. 
  - **Fix** Created new flask decorator that checks if session cookie exists `login_required` If user does not have a session he is redirected to the login page
  - **Test** try to reach endpoint `http://0.0.0.0:5000/profile/willfarnaby` straight though url, with decorator request is redirected to login page. 
  

- **Bug** New book Edit form is setting causing inconsistency with the Book object returned from Data Storage

that all happens because of the design choice to use the book title on the url. This is intentional to let user navigate to different books by title if he wants. 
This was caused by an inconsistency on the Book class. when the `book.get_dict()` was called from the `book_model.update_book()` It was returning a poorly formatted string. That caused a cascading effect. Then when the redirect occurred to the single_book page, the `book_model.find_by_title()`.  
    
    AttributeError: 'NoneType' object has no attribute 'get_title'

  - ** Fix ** added new method set_raw_title() to format the_title and refined the get_tile() methods.   
  - **UnitTest** New unittest to test Book title formatting
    
    
    test_get_formatted_title (book_test.ReviewTest) ... ok
    test_get_object_dict (book_test.ReviewTest) ... ok
    test_get_reviewed_returns_false (book_test.ReviewTest) ... ok
    test_raw_title (book_test.ReviewTest) ... ok
    test_set_title (book_test.ReviewTest) ... ok
    test_set_title_with_None (book_test.ReviewTest) ... ok
    test_set_title_with_empty_value (book_test.ReviewTest) ... ok
    test_set_title_with_multiple_spaces (book_test.ReviewTest) ... ok


**TESTING**

-**Update in Review Class Behaviour**

 cause: Initially application used book title to query for related reviews. However with the introduction with the Edit Book functionality, the book title became fluid, hence a new story was created to update this behaviour to use the unique field objectId.
 notes:  - Refactor review to reference book by `ObjectId()` rather than book title (see #TODO in book.views)

 **Fix**:
  - Single book page, Book Reviews
  - Refactoring on Review Class to use `ObjectIds` for both `reviewer` and `Book` fields
  - Refactoring of tests to reflect new fields
  - Creating setter for reviewer name based on uniqueID (relying on DB storage)
  - Refactoring of review_model.py to user User and book IDs
  - Adding unittests for review Class
  - Selenium test for review section in book_page

- **Bug** `Sign-up` page does not ask user to repeat password.
  **Fix** added new input field on register form
    On Register view see if fields match, then create new user. 
    If field does not match warn user with flash message
  **Test** Added selenium test to test behaviour


- **Bug** Refactoring on Profile.html 
  The Remodeling of the review table required a refactoring on the profile route. Review table was storing `strings`, now they store ObjectIds. 
  That is to improve consistency on the stored data. A review can only exist for a book that has an entry on the application. Strings fields were very tolerant and didn't have a relation with the Book collection.
  
  - **Fix**
    Refactor the Review class to support ObjectIds and have setters for a String field. 
    Now Profile route gets reviews built from stored on Application Collections only.
    
  - **Test**
    - Added Unittest for Review class.
    - Navigate to Profile page tabs and confirm fields are showing
    - On Favorite books there's still a need to fix each book rate

## Refactoring
- **Done**
In order to improve the ability to test and the compartmentalization of the code a new class `ManageUsers` was created all the logic from routes login and register was moved to this class. This allowed writing unittests for each method separately.

 - Benefits:
   - predictable behaviour
   - flask views are only handling flask specifics
   - Further testing 
   - single responsibility for each Class and component
    - Flask only interacts with Application classes
    - Each SuperClass is handling the integration with the mongo model. If I ever decided for a different data storage type, It's possible to update the class to inherit  from a new Super class (which would in turn replace the current Pymongo implementation). 
  
 - new Class [ManageUsers](https://github.com/diogo-pessoa/the-bookshelf/blob/master/src/bookshelf/manage_users/manage_users.py)
 - **Test**
   - [Register](https://github.com/diogo-pessoa/the-bookshelf/blob/master/test/src/bookshelf/register_test.py)
   - [Login](https://github.com/diogo-pessoa/the-bookshelf/blob/master/test/src/bookshelf/login_test.py)
  -  [ManageUsersTest](https://github.com/diogo-pessoa/the-bookshelf/blob/master/test/src/bookshelf/manage_users_test.py)

 - new Class [ManageBooks](https://github.com/diogo-pessoa/the-bookshelf/blob/master/src/bookshelf/manage_books/manage_books.py)
 - **Test**
   - [Books](https://github.com/diogo-pessoa/the-bookshelf/blob/master/test/src/bookshelf/manage_books_test.py)
  
- new Class [ManageReviews](https://github.com/diogo-pessoa/the-bookshelf/blob/master/src/bookshelf/manage_reviews/manage_reviews.py)
 - **Test**
   - [Reviews](https://github.com/diogo-pessoa/the-bookshelf/blob/master/test/src/bookshelf/manage_review_test.py)
  
