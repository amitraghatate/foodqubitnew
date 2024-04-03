from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from .views import create_user

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signupProcess/<str:api_key>/', views.signupProcess, name='signupProcess'),
    path('foodProcess/<str:api_key>/', views.signupProcess, name='foodProcess'),
    path('mealProcess/<str:api_key>/', views.signupProcess, name='mealProcess'),
    path('fitnessProcess/<str:api_key>/', views.signupProcess, name='fitnessProcess'),
    path('api/signin/', views.signin, name='signin'),
    path('api/viewUserData/<str:api_key>/', views.viewUserData, name='viewUserData'),
    path('api/updateUser/<str:api_key>/', views.updateUser, name='updateUser'),
    path('api/logout/<str:api_key>/', views.logout, name='logout'),
    path('api/deleteAccount/<str:api_key>/', views.deleteAccount, name='deleteAccount'),
    path('api/changePassword/<str:api_key>/', views.changePassword, name='changePassword'),
    # path('', views.start, name='start'),
    # path('home/', views.home, name='home'),
    # path('food/', views.food, name='food'),
    # path('signupProcess/', views.signupProcess, name='signupProcess'),
    # path('diet/', views.diet, name='diet'),
    # path('diet/dietProcess', views.dietProcess, name='dietProcess'),
    # path('meal/', views.meal, name='meal'),
    # path('meal/mealProcess', views.mealProcess, name='mealProcess'),
    # path('fitness/', views.fitness, name='fitness'),
    # path('fitness/fitnessProcess', views.fitnessProcess, name='fitness'),
    # path('lastSignup/', views.lastSignup, name='lastSignup'),
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login_view, name='login'),
]
