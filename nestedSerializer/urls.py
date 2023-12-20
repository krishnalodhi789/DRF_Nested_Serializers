from django.urls import path, include
from rest_framework.routers import DefaultRouter
from nestedSerializer import views
# router = DefaultRouter()
# router.register("authorlistview", views.AthorListView, basename="authorlistview")
# router.register("postlistview", views.PostListView, basename="postlistview")

urlpatterns = [
    # path("api/", include(router.urls))
    path('api/authorlistview/',views.AuthorListView.as_view()),
    path('api/authordetailview/<int:pk>/',views.AuthorDetailView.as_view(), name='author-detail'),
    path('api/postlistview/',views.PostListView.as_view()),
    path('api/postdetailview/<int:pk>/',views.PostDetailView.as_view(), name='post-detail'),
]
