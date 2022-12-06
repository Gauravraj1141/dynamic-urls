from django.urls import path, register_converter
from . import converters, views

# Here we register our converter
register_converter(converters.FiveDigitNumber, 'yyyyy')

urlpatterns = [
    # here we give **kwargs in our path
    path('/<int:my_id>/', views.home,
         {"myname": "pallo"}, name="student"),
    path('/<int:my_id>/<int:my_subid>/', views.subhome, name="student"),
    path('/<int:my_id>/<int:my_subid>/<int:my_superid>/',
         views.superhome, name="student"),

    path('converter/<yyyyy:fivedigits>/', views.converterpath, name="converter")

]
