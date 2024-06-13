from django.urls import path
from inicio import views
# from inicio.views import inicio, template1, template2, template3, template4, probando 

urlpatterns = [
    path('', views.inicio),
    path('template1/<str:nombre>/<str:apellido>/<int:edad>', views.template1),
    path('template2/<str:nombre>/<str:apellido>/<int:edad>', views.template2),
    path('template3/<str:nombre>/<str:apellido>/<int:edad>', views.template3),
    path('template4/<str:nombre>/<str:apellido>/<int:edad>', views.template4),
    path('probando/', views.probando),
    path('autos/crear/<str:marca>/<str:modelo>', views.crear_auto)
]
