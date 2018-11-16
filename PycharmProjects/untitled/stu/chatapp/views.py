from django.shortcuts import render


from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import random


def keyboard(request):
    return JsonResponse({
        'message':{
            'text':'드시고 싶은 메뉴를 골라주세요'
        },
        'type': 'buttons',
        'buttons': ['밥류', '고기류']
    })


@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == '밥류':
        ricelist = ['등촌칼국수', '전주식당', '맘보', '알촌', '디왈리', '준호네 부대찌개', '경원분식', '아토', '육연차']
        rice_rand = random.randrange(0, 10)
        rice = ricelist[rice_rand]

        return JsonResponse({
            'message': {
                'text': ricelsit,'와 같은 메뉴가 있습니다.\n 제가 추천해드릴 메뉴는', rice, '입니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['밥류', '고기류']
            }

        })

    elif datacontent == '고기류':
        meatlist = ['포크포크', '태평돈가스', '치킨스팟', '내가 찜한 닭', '태평곱창']
        meat_rand = random.randrange(0, 5)
        meat = meatlist[meat_rand]

        return JsonResponse({
            'message': {
                'text': meatlist,'와 같은 메뉴가 있습니다.\n 제가 추천해드릴 메뉴는', meat, '입니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['밥류', '고기류']
            }

        })
