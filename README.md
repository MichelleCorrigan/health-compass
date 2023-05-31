# Health Compass

![Responsive screenshot](readme-images/multi-screens.png)

## A Nutrion and Lifestyle Coaching Site
>A site to purchase nutrition and coaching programmes, as well as blog content and testimonials to share help and advice.

## [Live site](https://health-compass.herokuapp.com/) | [Repository](https://github.com/MichelleCorrigan/health-compass)

---
## Deployment

### Create an external database
1. Log in to [ElephantSQL](https://www.elephantsql.com/)
2. Click Create New Instance
3. Give your plan a Name, select the free plan, click Select Region
4. Select data-center nearest you, click Review
5. Check all details are correct then click Create Instance
6. Return to dasboard, click on your new database, copy the database URL to your clipboard

### Create Heroku App
1. Log in to [Heroku](https://www.heroku.com)
2. Click New, select New app
3. Name your app, select region closest to you, click Create app
4. In Settings, reveal Config Vars
5. Add a new config var named DATABASE_URL, paste in the URL from ElephantSQL as the value

In your IDE terminal install:
  `pip3 install dj_database_url==0.5.0 psycopg2`
 
Update requirements.txt file:
  `pip freeze > requirements.txt`

Add the DATABASE_URL to your env.py file or environment variables in gitpod

Go to settings.py and  `import dj_database_url` underneath the import for os

Comment out the default  `DATABASES`  setting, add the following underneath:

``` DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }

```
In the terminal:
1. Run migrations
2. Create a superuser

Return to settings.py and delete the previous Databases entry, un-commenting out the default setting

In the root directory of your project, create a file called "Procfile" and add  `web: gunicorn project_name.wsgi` 
    
In settings.py 
1. Add ['app_name.heroku.com', 'localhost'] to  `ALLOWED_HOSTS`
2. Add the key value of: `DISABLE_COLLECTSTATIC`  and set it to 1. When you have  staticfiles to push then remove this variable
3. Set `DEBUG = 'DEVELOPMENT' in os.environ`
    
Commit and push these changes to GitHub

Then use `git push heroku main` to deploy to Heroku

In the Heroku deploy tab, connect to Github, connect to your repository and enable automatic deploys

In the settings tab, update the config vars with the following:

| Key | Value  |
| -- | -- |
|AWS_ACCESS_KEY_ID|From AWS in CSV Download|
|AWS_SECRET_ACCESS_KEY|From AWS in CSV Download|
|DATABASE_URL|From ElephantSQL dashboard|
|SECRET_KEY|Randomly Generated Django Key|
|USE_AWS|True|

Click on open app at the top of the page to view your deployed app

---


## Bugs
- My Account dropdown menu doesn't function.
- Once deployed, links to the Programmes page and Programme details page became tempermental. 
- These will be fixed before resubmission.