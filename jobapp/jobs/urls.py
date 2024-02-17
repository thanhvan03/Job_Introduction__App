
from django.urls import path, re_path, include
from rest_framework import routers
from jobs import views

router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('joblistings', views.JobListingViewSet, basename='joblistings')
router.register('joblistings', views.JobListingDetailViewSet, basename='joblistingsdetail')
router.register('users', views.UserViewSet, basename='users')
router.register('comments', views.CommentViewSet, basename='comments')
router.register('ratings', views.RatingViewSet, basename='ratings')
router.register('users', views.UpdateUserViewSet, basename='update')
router.register('joblistings', views.JobListingViewSet, basename='add_tags')
router.register('jobapplications', views.JobApplicationViewSet, basename='submit')





urlpatterns = [
    path('', include(router.urls)),

]
