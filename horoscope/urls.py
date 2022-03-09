from django.urls import path
from . import views

urlpatterns = [
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),  # конвертор str, int
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
