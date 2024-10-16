from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('question/', views.question_view, name='question_view'),
    path('choice/', views.choice_view, name='choice_view'),
    path('success/', views.success_view, name='success'),
]