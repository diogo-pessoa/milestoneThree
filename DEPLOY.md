App is deployed using heroku.

I have linked the github repository to The heroku and enabled automatic deploys. Hence, when a commit reaches master. It will automatically release a new version. 

Guide used as a base for this deployment document [Gunicorn on Heroku](https://devcenter.heroku.com/articles/python-gunicorn) 

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