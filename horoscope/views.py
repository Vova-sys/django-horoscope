from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число из 4х цифр - {sign_zodiac}')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали вещественное число - {sign_zodiac}')


def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату - {sign_zodiac}')


def index(request):
    zodiacs = list(zodiac_dict)
    """
    <ol>
        <li>aries</li> 
        <li>taurus</li>
        <li>gemini</li>
        ...
    </ol>
    """
    result = ''
    for sign in zodiacs:
        redirect_path = reverse('horname', args=[sign])
        result += f"<li> <a href='{redirect_path}'> {sign.title()} </a> </li>"
    response = f"""
    <ul>
      {result}
    </ul>"""
    return HttpResponse(response)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    return render(request, 'horoscope/info_zodiac.html')



def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horname', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)

# Динамический URL
# def get_info_about_sign_zodiac(request, sign_zodiac):
#     if sign_zodiac == 'leo':
#         return HttpResponse('Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).')
#     elif sign_zodiac == 'scorpio':
#         return HttpResponse('Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).')
#     elif sign_zodiac == 'aries':
#         return HttpResponse('Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).')
#     elif sign_zodiac == 'taurus':
#         return HttpResponse('Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).')
#     elif sign_zodiac == 'cancer':
#         return HttpResponse(' Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).')
#     elif sign_zodiac == 'gemini':
#         return HttpResponse('Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).')
#     elif sign_zodiac == 'virgo':
#         return HttpResponse('Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).')
#     elif sign_zodiac == 'libra':
#         return HttpResponse('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).')
#     elif sign_zodiac == 'sagittarius':
#         return HttpResponse('Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).')
#     elif sign_zodiac == 'capricorn':
#         return HttpResponse('Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).')
#     elif sign_zodiac == 'aquarius':
#         return HttpResponse('Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).')
#     elif sign_zodiac == 'pisces':
#         return HttpResponse('Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).')
#     else:
#         return HttpResponseNotFound(f'Неизвестный знак зодиака - {sign_zodiac}')

# def leo(request):
#     return HttpResponse('Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).')
#
# def scorpio(request):
#     return HttpResponse('Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).')
#
# def aries(request):
#     return HttpResponse('Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).')
#
# def taurus(request):
#     return HttpResponse('Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).')
#
# def cancer(request):
#     return HttpResponse(' Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).')
#
# def gemini(request):
#     return HttpResponse('Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).')
#
# def virgo(request):
#     return HttpResponse('Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).')
#
# def libra(request):
#     return HttpResponse('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).')
#
# def sagittarius(request):
#     return HttpResponse('Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).')
#
# def capricorn(request):
#     return HttpResponse('Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).')
#
# def aquarius(request):
#     return HttpResponse('Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).')
#
# def pisces(request):
#     return HttpResponse('Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).')
