Features & User Stories
---

## Features

## Features left to implement 

- As a User I want to search for books without having to create a user.

- As a user I can search for books

- As a user I can Add new books

- As a user I can Edit book details

- As a Moderator I can review book information and tag is a validated

- As a Moderator I can delete books

- As a User I can rate and Review Books.

- As a User I can share/recommend this book to a friend

- As a User I can edit or delete My own review 

- As a User I have a profile page with my details and reviews I left.

- As a User I want to have a list with my favorite books, and I want to see that on my profile page

-  As a user if a search doesn't return a book, I want a quick link to create this new book entry.

-  As a Developer I want the site to have a responsive interface with a sensible colorScheme

-  As a Developer I want a Navigation Bar on the top of the page. 

- As a developer I want to hide the sign-up and login button once the user finishes authentication

- As a developer I want to organize the Book, Review and User into classes to model them as Objects. 
    
    - Broke down data model into three objects User, Book and Review, splitting each into its respective file.
    - Refactoring of all the imports where needed
    - **Test** Loaded index page, that queries all books and review, as well register feature available at the time of this change. 
        - Created new users and was able to confirm when user already exists.  

- As want to be able to create a user in order to create books and leave reviews
    - Register template created, 
    - Register functionally added to the routes.py file
    - mongo.db.user.insert(), moved to model.User object
    - **Test** Added new register_page_test, loads register page, fill and submit form
