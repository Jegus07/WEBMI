from django.urls import path
from . import views


from django.urls import path
from . import views
from .views import inscription

urlpatterns = [
    path('', views.inscription, name='inscription'),  # ← rendre accessible via /inscription/
    path('', inscription, name='inscription'),
]

