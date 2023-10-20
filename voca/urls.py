from django.urls import path
from .import views

app_name = 'voca'
urlpatterns = [
    path('', views.home, name='home'),
    path('word_detail/<int:pk>', views.WordDetailView.as_view(), name='word_detail'),
    path('edit/<int:pk>', views.EditWordView.as_view(), name='edit_word')
]