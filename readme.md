First Create Project as ususal.
Here i used User.objects.create_user to add users you can use UserCreationForm of Django for that also, as i showed in my previous Email_verification project..

After that you have to install 1 module 'pip install django-allauth'

After that make some changes in your Settings.py file

STEP2:

    OPEN SETTINGS.PY IN MYPROJECT FOLDER

    INSTALLED_APPS = [ 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles', 'django.contrib.sites', #must add this 
    'myapp',

    'allauth',   
    'allauth.account',  
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google', 
    ]

    AUTHENTICATION_BACKENDS = ( 'django.contrib.auth.backends.ModelBackend', 'allauth.account.auth_backends.AuthenticationBackend', )

    Add this is Middleware - 'allauth.account.middleware.AccountMiddleware',

    SITE_ID = 2 
    LOGIN_REDIRECT_URL = '/'    #where you want to land user after login, in my case i write profile page..
    SOCIALACCOUNT_LOGIN_ON_GET = True #add this otherwise you will see ugly 'continue page'
    ACCOUNT_LOGOUT_ON_GET = True    #add this otherwise when user try to logout then he will see want to continue page.

    SOCIALACCOUNT_PROVIDERS = {
         'google': {
             'SCOPE': [
                 'profile', 'email', 
                 ], 
                 'AUTH_PARAMS': {
                     'access_type': 'online', 
                     } 
                     } 
                     }

STEP3:

    CREATE TEMPLATE CREATE SOCIAL_APP FOLDER AND ADD INDEX.HTML

    {% load socialaccount %} <!doctype html>

    Clike HereLogin with Google Accounts.

STEP4:

    #ADD PATH IN URLS.PY in settings

    from django.contrib import admin

    urlpatterns = [

    path('accounts/', include('allauth.urls')), ] #important

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

STEP7: #Add social applications in your adminpannel

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

    You can check all available functions through this link - [http://127.0.0.1:8000/accounts/]


-------------------------------------------------------------------------------------------------------------
Now for GIthub <-------------------------


# settings.py

INSTALLED_APPS = [
    ...
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github', #just add this 
    ...
]

AUTHENTICATION_BACKENDS = [
    ...
    'allauth.account.auth_backends.AuthenticationBackend', #already added for google 
    ...
]

SITE_ID = 1  # Set your SITE_ID, if not set already

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': ['user', 'repo'],
        'VERIFIED_EMAIL': True,
    }
}

    App registration (get your key and secret here)
    https://github.com/settings/applications/new

    
    Development callback URL
    http://127.0.0.1:8000/accounts/github/login/callback/

else everything is same...

Check out Full Django Notes on my repo:[]
