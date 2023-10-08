from django.urls import path

from WebExam6.Profile.views import home_page, profile_create, catalogue_page, profile_details, profile_edit, \
    profile_delete

urlpatterns = (
    path('', home_page, name='index'),
    path('profile/create/', profile_create, name='profile-create'),
    path('catalogue/', catalogue_page, name='catalogue'),
    path('profile/details/', profile_details, name='profile-details'),
    path('profile/edit/', profile_edit, name='profile-edit'),
    path('profile/delete/', profile_delete, name='profile-delete'),
)
