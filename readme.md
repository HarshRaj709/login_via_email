First Create Project as ususal.
Here i used User.objects.create_user to add users you can use UserCreationForm of Django for that also, as i showed in my previous Email_verification project..

After that you have to install 1 module 'pip install django-allauth'

After that make some changes in your Settings.py file

STEP2:

    OPEN SETTINGS.PY IN MYPROJECT FOLDER

    INSTALLED_APPS = [ 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles', 'django.contrib.sites',
    'myapp',

    'allauth',   
    'allauth.account',  
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google', 
    ]

    AUTHENTICATION_BACKENDS = ( 'django.contrib.auth.backends.ModelBackend', 'allauth.account.auth_backends.AuthenticationBackend', )

    SITE_ID = 1 LOGIN_REDIRECT_URL = '/'

    SOCIALACCOUNT_PROVIDERS = { 'google': { 'SCOPE': [ 'profile', 'email', ], 'AUTH_PARAMS': { 'access_type': 'online', } } }

STEP3:

    CREATE TEMPLATE CREATE SOCIAL_APP FOLDER AND ADD INDEX.HTML

    {% load socialaccount %} <!doctype html>

    Clike HereLogin with Google Accounts.

STEP4:

    #ADD PATH IN URLS.PY in settings

    from django.contrib import admin

    urlpatterns = [

    path('accounts/', include('allauth.urls')), ]

STEP5:

    #RUN MIGRATIONS

    python manage.py makemigrations python manage.py migrate

STEP6:

    CREATE API CONSOLE WATCH VIDEO CAREFULLY

    1.Go to this link-> https://console.developers.google.com/

    2.Dashbord create a project and proceed

    3.Dashbord go to Credentials On the dropdown, choose OAuth Client ID option

    4.Dashbord OAuth consent screen create external give app name and save

    5.Create OAuth client ID Authorized Javascript origins -> http://127.0.0.1:8000 Authorized redirect URL -> http://127.0.0.1:8000/accounts/google/login/callback/

    6.Get the credentails

STEP7: #Add social applications

    Provider Id: Google 
    Name: Google 
    API Client id: Secret key:

STEP8: #ADD SITEID ITS UNIQUE TO EACH CLIENTID

    #USING TERMINAL ENTER THIS CMD

    .\manage.py shell or python manage.py shell

    from django.contrib.sites.models import Site
    sites=Site()
    sites.domain='http://127.0.0.1:8000/'
    sites.name='htpp://127.0.0.1:8000/'
    sites.save()
    print(sites.id)

    This will give your site id...