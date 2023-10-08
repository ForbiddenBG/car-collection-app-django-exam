from django.urls import path

from WebExam6.Car.views import car_create, car_details, car_edit, car_delete

urlpatterns = (
    path('car/create/', car_create, name='car-create'),
    path('car/<int:id>/details/', car_details, name='car-details'),
    path('car/<int:id>/edit/', car_edit, name='car-edit'),
    path('car/<int:id>/delete/', car_delete, name='car-delete'),
)
