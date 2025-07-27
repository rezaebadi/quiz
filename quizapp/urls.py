from django.urls import path, include, re_path
from .views import *
app_name = 'data'
urlpatterns = [
    path("all-books/", AllBookView.as_view(), name="all_books"),
    path("survey/", SurveyView.as_view(), name="survey"),
    path("item_tag/", ItemTagView.as_view(), name="item_tag"),
]