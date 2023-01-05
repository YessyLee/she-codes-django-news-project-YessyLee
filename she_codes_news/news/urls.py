from django.urls import path, include
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), #this bring us to index, views.py IndexView class in views.py
    path('<int:pk>/', views.StoryView.as_view(), name='story'), #int pk primary key in number
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('<int:pk>/comment/', views.AddCommentView.as_view(), name ='addComment'),
    path('news/edit/<int:pk>', views.UpdateStoryView.as_view(), name ='updateStory'),
    path('news/<int:pk>/delete', views.DeleteStoryView.as_view(), name ='deleteStory'),
    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('searchstory', views.SearchStoryView, name='searchstory'),
]
