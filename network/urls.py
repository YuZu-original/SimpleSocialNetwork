from rest_framework.routers import DefaultRouter

from network import views

router = DefaultRouter()
router.register(r"post", views.PostViewSet)
router.register(r"comment", views.CommentViewSet)

urlpatterns = router.urls
