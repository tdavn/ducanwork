from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<int:year><int:month><int:day><slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('edit_post/<int:year><int:month><int:day><slug:pk>/', views.UpdatePostView.as_view(), name='update_post'),
]
