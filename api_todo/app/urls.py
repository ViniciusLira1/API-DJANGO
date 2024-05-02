# from django.urls import path
# from app.views import TodoListAndCreate,TodoPutDelete

# urlpatterns = [
#     path('',TodoListAndCreate.as_view()),
#     path('post/',TodoListAndCreate.as_view()),
#     path('<int:pk>/',TodoPutDelete.as_view())

# ]


from app.views import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',TodoViewSet)
urlpatterns = router.urls
