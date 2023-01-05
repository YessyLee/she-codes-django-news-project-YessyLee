from django.contrib import admin

# Register your models here.
from . models import NewsStory, Comment, Category
# 
# from . import models #importing all of the models

admin.site.register(NewsStory)
admin.site.register(Comment)
admin.site.register(Category)