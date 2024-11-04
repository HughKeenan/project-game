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

+ Create a new app. The app must have aunique name

+ Select the appropriate region for your location (Europe or America)

+ Create a Procfile in your workspace