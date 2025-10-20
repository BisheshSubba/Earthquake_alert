from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('predictorpage.urls')),
    path('api/', include('predictionmodel.urls'))
]
