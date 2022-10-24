from django.shortcuts import render
import random
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json

@api_view(['GET','POST'])
def home(request):
    if request.method =='GET':
        return render(request,'randomseat/random2.html')
    # POST 요청일 때
    if request.method == 'POST':
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        
        data = json.loads(request.body)
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #print(data)
        # do something
        print(data)

        context = {
            'result': data,
        }
        return JsonResponse(context)


# Create your views here.
member=["강동훈","김도원","김민수","김보경" ,"김수민" ,"김희제",
"류승태" ,"문소희","박정호","박준수","박준표", '없지롱~',
"백준봉" ,"양은진","엄형규","윤도현","이미현","이상찬",
"이은지" ,"정재훈","차은혁","최권민","최형규","황호선"]

memdic= [[i,f'image/{member[i]}.jpg',member[i],0] for i in range(len(member))]
#visit=[]
@api_view(['GET','POST'])
def go(request):
    global memdic #visit, 
    if request.method=="POST":
        
        #a=int(list(request.POST)[1])
        a=int(json.loads(request.body))
        memdic[a][3]=1

        context={

            'memdic':memdic,
            
            
        }
        return JsonResponse(context)


    memdic= [[i,f'image/{i}.jpg',[i],0] for i in range(len(member))]
    random.shuffle(memdic)
    #visit=[]
    context={

        'memdic':memdic,
        'numbers': range(24),
        'dic':{str(i):i for i in range(24)},
    }

    return render(request,'randomseat/random.html',context)