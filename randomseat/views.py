from django.shortcuts import render
import random
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
import json
import time
import tkinter
#시작은 python manage.py runserver 192.168.202.117:8000   왼쪽은 ip주소 맞춰서 입력
start_at=0#서버 시작시간을 적어주세요
end_at=1#서버 닫을 시간 


# Create your views here.
member=["강동훈","김도원","김민수","김보경" ,"김수민" ,"김희제",
"류승태" ,"문소희","박정호","박준수","박준표", '없지롱~',
"백준봉" ,"양은진","엄형규","윤도현","이미현","이상찬",
"이은지" ,"정재훈","차은혁","최권민","최형규","황호선"]

memdic= [[0,f'image/{i}.jpg',i] for i in member]


def gogo(request):#최초 페이지를 보내주는 함수 
    if request.method=='GET':
        return render(request,'randomseat/p2.html')

lotto=[i for i in range(1,25)] #비어있는 자리 리스트 
lotto.remove(19)
lotto.remove(24)
end={ i:'seat'+str(i) for i in range(1,25)}
#end[1]='hihi'
dic={}
visited={i:0 for i in range(1,25)}#[0]*25



@api_view(['POST'])
def reroll(request): #자리 번호를 다시 뽑음. 확정 전이므로 중복 가능 
    now=time.localtime(time.time()).tm_min
    if now<start_at:
        data={'my_num':'아직 안열림'}
        return JsonResponse(data)

    my_name=request.data['Name']
    #확정자면 되돌리고 진행
    if my_name in dic:
        my_seat=dic[my_name]
        if visited[my_seat]:
            lotto.append(my_seat)
            end[my_seat]='seat'+str(my_seat)
            visited[my_seat]=0
    #미확정자면 그냥 진행
    random.shuffle(lotto)

    dic[my_name]=lotto[0]
    data={'my_num':lotto[0]}
    return JsonResponse(data)

@api_view(['GET'])
def sendinfo(request): #현재까지의 자리 배치 상황을 보내주는 함수 
    data={'current':end,
    'not':visited,}
    return JsonResponse(data)

@api_view(['POST']) 
def checkin(request): #확정지어서 자리를 고정하는 함수. 더 이상 리롤에서 확정된 번호는 나오지 않음 
    my_name=request.data['Name']
    my_seat=dic[my_name]
    if visited[my_seat]==0:#미확정자리라면
        visited[my_seat]=my_name#확정시키고
        end[my_seat]='확정 됨'#my_name#이름을 저장함
        data={ 'my_num':'확정 완료'}#보내줄 데이터=자리,내 번호
        lotto.remove(my_seat)#중복된 번호 안나오도록
        #return JsonResponse(data)
    elif visited[my_seat]==my_name:
        data={'my_num':'확정 완료'}
        
    else:
        data={'my_num':'늦음 ㅋ'}
    return JsonResponse(data)


@api_view(['GET'])
def result(request):

    data={'current':visited}
    return render(request, 'randomseat/result.html', data )