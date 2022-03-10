from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns = [
    path('', views.index),
    path('<my_date:sign_zodiac>/', views.get_my_date_converters),
    # path('<yyyy:sign_zodiac>/', views.get_yyyy_converters),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),  # конвертор str, int
    path('<my_float:sign_zodiac>/', views.get_my_float_converters),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horname'),
    # path('scorpio', views.scorpio),
    # path('aries', views.aries),
    # path('taurus', views.taurus),
    # path('gemini', views.gemini),
    # path('cancer', views.cancer),
    # path('virgo', views.virgo),
    # path('libra', views.libra),
    # path('sagittarius', views.sagittarius),
    # path('capricorn', views.capricorn),
    # path('aquarius', views.aquarius),
    # path('pisces', views.pisces)

]
