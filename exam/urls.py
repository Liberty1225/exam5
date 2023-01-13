from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from account import views as acc_view
from news import views as news_view

acc_router = DefaultRouter()
acc_router.register('register', acc_view.RegisterAuthorAPIView)

news_router = DefaultRouter()
news_router.register('news', news_view.NewsViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="News Clone API",
      default_version='v-0.01-alpha',
      description="API для взаимодействия с Новости API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="aitegin1225@gmail.com"),
      license=openapi.License(name="No Licence"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/token/', obtain_auth_token),

    path('api/accounts/', include(acc_router.urls)),
    path('api/news/', include(news_router.urls)),
    path('api/news/<int:news_id>/', news_view.NewsViewSet.as_view()),
    path('api/news/<int:news_id>/comment/', news_view.CommentViewSet.as_view()),

    # documentation URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_doc'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_doc'),

]


# urlpatterns = [
#    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#    ...
