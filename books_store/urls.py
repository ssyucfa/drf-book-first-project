from rest_framework import routers

from . import views

urlpatterns = [

]

router = routers.SimpleRouter()

router.register(r'book', views.BookViewSet)

urlpatterns += router.urls

