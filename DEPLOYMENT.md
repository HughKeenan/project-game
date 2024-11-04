# Deployment

+ This app was deployed to Heroku

## Local Deployment

Using your repository, open a workspace in Gitpod

1. Install dependencies:

+ Open the terminal window and type: pip3 install -r requirements.txt

2. Create a .gitignore file in the root directory of the project. Add env.py and pycache files to ensure data privacy

3. Create a .env file. This will contain the following environment variables:

    ```
    python
    import os

      os.environ['SECRET_KEY'] = 'Add a secret key'
      os.environ['DATABASE_URL'] = 'will be used to connect to the database'
      os.environ['DEBUG'] = 'True'
    ```

+ During development DEBUG is set to True, but must be changed to False before final deployment

4. To make migrations on updates to models, run the following in the terminal
    ```
        python3 manage.py makemigrations
        python3 manage.py migrate
    ```

5. Create a superuser to access the admin environment.
    ```
        python3 manage.py createsuperuser
    ```
+ Enter the requested information (username, email and password).

6. Run the app with the following command in the terminal:
    ```
        python3 manage.py runserver
    ```

7. Open the provided link in browser to see your app.

To access the admin environment:

Add /admin/ to the home link.
Enter the superuser's username and password.

## Heroku Deplyoment

+ Go to www.heroku.com 

+ Log in or create a new account.

+ Create a new app.

![Create New App](documentation/deployment/new_app.png)

+ Name the app (the app must have aunique name) and select the appropriate region for your location (Europe or America).

![Name and region](documentation/deployment/region_and_name.png)     

+ Use the terminal command pip3 install gunicorn ~20.1 and freeze to your requirements.txt byt typing pip3 freeze local > requirements.txt in the terminal.

+ Create a Procfile in your workspace

![Procfile](documentation/deployment/procfile.png)

+ The procfile must contain the following:
    ```
        web: gunicorn <app_name>.wsgi
    ```

+ In the project's settings.py file, ensure Debug=False and add '.herokuapp.com' to the list of ALLOWED_HOSTS

+ Navigate to the resources tab and ensure you are using an eco Dyno, and remove any Postgres database add-ons

+ In the app's settings tab, open Config Vars 

+ Ensure the config vars are as follows:
| Key|Value|
|--|--|
| DATABASE_URL | <CI postgres database url> | 
| DISABLE_COLLECTSTATIC | 1 |
| SECRET_KEY | <your choice of secret key> |

 
+ Commit any changes made and push to Github

+ Go into your app in Heroku, open the Deploy tab. search for your github repository and connect it to the app. Manually deploy the app from the main branch. You can also at this point set up automatic deploys so an up to date version will deploy every time you push to github.

+ Ahead of final deployment, set debug to False locally and delete DISABLE_COLLECTSTATIC from config vars. Then commit and push the changes to GitHub.
