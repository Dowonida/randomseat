from django.shortcuts import render
import random
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
import json
import time
import tkinter
#시작은 python manage.py runserver 192.168.202.117:8000   왼쪽은 ip주소 맞춰서 입력
start_at=0#서버 시작시간을 적어주세요


# Create your views here.
member=["강동훈","김도원","김민수","김보경" ,"김수민" ,"김희제",
"류승태" ,"문소희","박정호","박준수","박준표", '없지롱~',
"백준봉" ,"양은진","엄형규","윤도현","이미현","이상찬",
"이은지" ,"정재훈","차은혁","최권민","최형규","황호선"]

memdic= [[0,f'image/{i}.jpg',i] for i in member]
#visit=[]
def go(request):
    global memdic #visit, 
    if request.method=="POST":
        
        a=int(list(request.POST)[1])
        memdic[a][0]=1

        context={

            'memdic':memdic,
        }
        return render(request,'randomseat/random.html',context)


    memdic= [[0,f'image/{i}.jpg',i] for i in member]
    random.shuffle(memdic)
    #visit=[]
    context={

        'memdic':memdic,
    }

    return render(request,'randomseat/random.html',context)
    pass

def gogo(request):
    if request.method=='GET':
        return render(request,'randomseat/p2.html')

@api_view(['POST'])
def jsoni(request):
    print('hi')
    print(request.data)
    response_data = {}
    response_data['result'] = 'error'
    response_data['message'] = 'Some error message'
    return HttpResponse(json.dumps(response_data), content_type="application/json")
    #return JsonResponse(data)









lotto=[i for i in range(1,25)]
lotto.remove(19)
lotto.remove(24)
end={ i:'seat'+str(i) for i in range(1,25)}
#end[1]='hihi'
dic={}
visited={i:0 for i in range(1,25)}#[0]*25

def ready(request):
    data={'my_num':'아직 안열림'}
    return JsonResponse(data)

@api_view(['POST'])
def reroll(request):
    if time.localtime(time.time()).tm_min<start_at:
        return ready(request)
    my_name=request.data['Name']
    #확정자면 되돌리고 진행
    if my_name in dic:
        my_seat=dic[my_name]
        if visited[my_seat]:
            visited[my_seat]=0
            lotto.append(my_seat)
            end[my_seat]='seat'+str(my_seat)
    #미확정자면 그냥 진행
    random.shuffle(lotto)

    dic[my_name]=lotto[0]
    data={'my_num':lotto[0]}
    return JsonResponse(data)

@api_view(['GET'])
def sendinfo(request):
    # print(dic)
    # print(end)
    # print(lotto)
    data={'current':end,
    'not':visited,}
    return JsonResponse(data)

@api_view(['POST'])
def checkin(request):
    my_name=request.data['Name']
    my_seat=dic[my_name]
    if visited[my_seat]==0:#미확정자리라면
        visited[my_seat]=my_name#확정시키고
        end[my_seat]='확정 됨'#my_name#이름을 저장함
        data={ 'my_num':'확정 완료'}#보내줄 데이터=자리,내 번호
        lotto.remove(my_seat)#중복된 번호 안나오도록
        return JsonResponse(data)
    else:
        data={'my_num':'늦음 ㅋ'}
        return JsonResponse(data)


@api_view(['GET'])
def result(request):

    data={'current':visited}
    return render(request, 'randomseat/result.html', data )