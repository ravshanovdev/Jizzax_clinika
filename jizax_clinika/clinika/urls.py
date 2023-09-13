from django.urls import path
from .views import CategoryAPiView, BodyApiView, AddCategoryApiView, AddBlogPostAPiView, RegistrationApiView
urlpatterns = [
    path('', BodyApiView.as_view(), ),
    path('category/', CategoryAPiView.as_view(), ),
    path('add_post/', AddBlogPostAPiView.as_view(), ),
    path('add_category/', AddCategoryApiView.as_view(), ),
    path('registration/', RegistrationApiView.as_view(), ),




]


