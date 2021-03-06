"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

import authentication.views, review.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
            template_name='authentication/login.html',
            redirect_authenticated_user=True),
         name='login'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('home/', review.views.home, name='home' ),
    path('posts/', review.views.posts_user, name='posts'),
    path('posts/create-ticket/', review.views.create_ticket, name='create-ticket'),
    path('posts/edit-ticket/<int:pk>/', review.views.EditTicket.as_view(), name='edit-ticket'),
    path('posts/delete-ticket/<int:pk>/', review.views.DeleteTicket.as_view(), name='delete-ticket'),
    path('posts/<int:id>/', review.views.DetailTicket.as_view(), name='detail-ticket'),
    path('posts/<int:id>/add/', review.views.ReviewFormView.as_view(), name='response'),
    path('posts/new-review/', review.views.new_review, name='new-review'),
    path('posts/edit-review/<int:pk>/', review.views.EditReview.as_view(), name='edit-review'),
    path('posts/delete-review/<int:pk>/', review.views.DeleteReview.as_view(), name='delete-review'),
    path('follows/', review.views.FollowsList.as_view(), name='follows'),
    path('follows/search-follows/', review.views.search_follows, name='search-follows'),
    path('follows/add-follow/', review.views.add_follow, name='add-follow'),
    path('follows/unfollow/', review.views.unfollow, name='unfollow')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
