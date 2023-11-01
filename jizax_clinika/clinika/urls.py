

from django.urls import path
from .views import CategoryAPiView, BodyApiView, AddCategoryApiView, AddBlogPostAPiView, \
    RegistrationApiView, UpdateBlogApiView, DeleteBlogApiView, DetailBlogApiView, DeleteCategoryApiView
urlpatterns = [
    path('', BodyApiView.as_view(), ),
    path('category/', CategoryAPiView.as_view(), ),
    path('add_post/', AddBlogPostAPiView.as_view(), ),
    path('add_category/', AddCategoryApiView.as_view(), ),
    path('registration/', RegistrationApiView.as_view(), ),
    path('update/<int:pk>/', UpdateBlogApiView.as_view(), ),
    path('delete/<int:pk>/', DeleteBlogApiView.as_view(), ),
    path('detail/<int:pk>/', DetailBlogApiView.as_view(), ),
    path('delete_category/<int:pk>/', DeleteCategoryApiView.as_view(), ),






]


