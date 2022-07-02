# Django Models #
This is my submision for the assignment on APIs.

I was asked to build a URL shortener and to do this I made use of the _djangorestframework_, which I installed using
`pip install djangorestframework`

These are some of the steps I followed:
- After creating the new project and the app I called _link_, I created models in it and made migrations.
-Next I created a new python file called _serializers.py_, this was to hold the logic for our serializers which inherits from _djangorestframework's_ `serializer.ModelSerializer` 
-Moving on, I went on to creating the views and adding them to the _urls.py_ file.
