from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    # Looks for more routes within the Library app
    path('', include("library.urls"), name="library"),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path('docs/', SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    path('admin/', admin.site.urls),
]
