from django.urls import path
from mySEblog.views import homepage, postview,addpost, editpost, search_posts,deletepost
from recommendation.views import recommend_view
from .admin import custom_admin_site
urlpatterns = [
    path('', homepage, name='homepage'),
    path('post/<int:pk>', postview, name='postview'),
    path('add_post/', addpost, name='add-post'),
    path('post/edit/<int:pk>', editpost, name='update-post'),
    path('recommend/', recommend_view, name='recommend'),
    path('post/<int:pk>/delete', deletepost, name='delete-post'),
    path('search/', search_posts, name='search-posts'),
    path('admin/', custom_admin_site.urls, name='admin-site'),
]
