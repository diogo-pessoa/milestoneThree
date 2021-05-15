Features & User Stories
---

## Features

- As a Developer I want the site to have a responsive interface with a sensible colorScheme
  - Using Materilize framework with a brown color-scheme listed
    on [UX section of README](https://github.com/diogo-pessoa/the-bookshelf#ux)

- As a Developer I want a Navigation Bar on the top of the page.
- Using materialize there's new responsive NavBar to base.html template, That is also a sidebar on base.html for smaller
  screen

- As a developer I want to hide the sign-up and login button once the user finishes authentication
  - **Feature** added if statement to base.html template that checks if `user.session` exists and shows Navbar elements
    accordingly
  - **Test** [login_page_test.py](https://github.com/diogo-pessoa/the-bookshelf/blob/master/test/html_test/login_page_test.py)
    Tests which navBar element shows-up when page loads after login
- As a developer I want to organize the Book, Review and User into classes to model them as Objects.
  - Broke down data model into three objects User, Book and Review, splitting each into its respective file.
  - Refactoring of all the imports where needed
  - **Test** Loaded index page, that queries all books and review, as well register feature available at the time of
    this change.
    - Created new users and was able to confirm when user already exists.
- As want to be able to create a user in order to create books and leave reviews
  - Register template created
  - Register functionally added to the routes.py file
  - mongo.db.user.insert(), moved to model.User object
  - **Test** Added new register_page_test, loads register page, fill and submit form
  
- As a Developer I want to run tests before every commit to make sure new features don't cause regression
  - Added a pre-commit hook which executes both UnitTest and Selenium(integration) suites
  - `cat .git/hooks/pre-commit`
    
      
      python -m unittest discover -s test/src/bookshelf -p "*_test.py" -v
      if [ $? -eq 0 ]; then
            python -m unittest discover -s test/html_test -p "*_test.py" -v
      fi

- As a User I want to Check My Personal Details on my profile Page
  - Profile Page has a Tab on `Books`, where User get a chance to review all his favorite Books and Rates left

- As a User I have a profile page with my details and reviews I left.
  - Profile Page has a Tab on `Reviews`, with a List of books listed with the rate, Book Name and comment

- As a User I want to have a list with my favorite books, and I want to see that on my profile page
  - Profile Page has a Tab on `Books`, where User get a chance to review all his favorite Books and Rates left
  
- As a User I want to search for books without having to create a user.
  - Books Page link is available on NavBar view does not validate if user is logged in. Any anonymous access can visit the page and query for books.
  
- As a user I can search for books
  - Included Search_bar on top of Books page. 
    - Added new route [/search](https://github.com/diogo-pessoa/the-bookshelf/blob/master/app/book/views.py)
    - new Method on [BookModel](https://github.com/diogo-pessoa/the-bookshelf/blob/master/app/model/book_model.py) to query books collection index, based on user input
    - Added include [search_bar.html](https://github.com/diogo-pessoa/the-bookshelf/blob/master/app/book/templates/search_bar.html) on Books.html template 
  - Creating collection index:
    inside the project root directory, start a session on the Python REPL  and run the command list below.
      note: "when running this the MONGO_URI has to be available to pymongo"


     from app import mongo
     mongo.db.books.create_index([("title", "text"), ("author", "text")])
 

  - **Test** [search_bar_test.py](https://github.com/diogo-pessoa/the-bookshelf/blob/master/test/html_test/search_bar_test.py)
    `all test are passing`
    - test_search_bar_text_content - validate the search_bar field content is visible and matches expected value
    - test_book_page_buttons - validate the search_bar field content is visible and matches expected value
    - test_search_for_book_1 - Runs functional test on search looking for 'Book1' - expects book to show on page main list
    - test_search_no_matching_result - Runs functional test on search looking for 'Book1' - expects heading 4 with message alerting for no matches
    - test_search_by_author - Runs functional test on search looking for author "Jon Doe" - expects list  of books on page body
  
  - Implementation is based on the MiniProject(flask) search lesson: [Search Within The Database](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/0d4e3419132440d9b2c0943f80dc54a8/)

  - **Work-In-Progress** As a user I can Edit book details
    - New route book.edit()
    - New book_model.update_book() With Call to mongoDB to update object by Id
    - New template edit.html with HTML form
    - **Test** Added unittest to validate book input and output 
    - **Test** New selenium test validation check for existing fields and if form fields are loaded on template

- **Follow-up** Allow User to Update personal Details
  - Added support to post form on profile page allowing user to update his personal information
    
  - **Test** Added unittest to User Class method related to update_info form

- As a user I want to update my password
  -  Added a first path to allow user to update his own password, on Profile page user can submit form to update his information, including password
    
- As a user I want to navigate to a book from my favorites list
 - Added url_for(link) on the template my favorite books, now user can go to the book from his profile page

## Features Left to Implement

- As a user I can Add new books

-  As a user if a search doesn't return a book, I want a quick link to create this new book entry.

- As a Moderator I can review book information and tag when it is validated

- As a Moderator I can delete books

- As a User I can rate and Review Books.

- As a User I can share/recommend this book to a friend

- As a User I can edit or delete My own review

- **Follow-up** from the BOOKS table I want to sort and order books and add pagination


- As a Developer I want to present a friendly 404 (Not found) or Error Page when the user hits a problem on the page, allowing the to navigate back to the page 