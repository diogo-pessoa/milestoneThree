Milestore Three
---

## Requirements

- [python3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - microframework for a web application
- [Unittest](https://docs.python.org/3/library/unittest.html#module-unittest)
- [selenium](https://selenium-python.readthedocs.io/locating-elements.html#locating-elements) 
     - Selenium Python bindings provides a simple API to write functional/acceptance tests
     - [Requires] - [geckodriver](https://github.com/mozilla/geckodriver)

## local development

- python -m venv ./venv/
- source venv/bin/activate       
- pip install -r [requirements.txt](https://github.com/diogo-pessoa/milestoneThree/blob/master/requirements.txt)
- python app.py

Add local env.py file:

     import os
     
     os.environ.setdefault("IP", "0.0.0.0")
     os.environ.setdefault("PORT", "5000")

## Testing

[TESTING.md](/TESTING.md)
