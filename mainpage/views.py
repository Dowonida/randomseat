from django.shortcuts import render
import random
# Create your views here.
List=["강동훈","김도원","김민수","김보경" ,"김수민" ,"김희제",
"류승태" ,"문소희","박정호","박준수","박준영","박준표",
"백준봉" ,"양은진","엄형규","윤도현","이미현","이상찬",
"이은지" ,"정재훈","차은혁","최권민","최형규","황호선"]



def func(request):
    random.shuffle(List)
    context={ '목록': List,
    'col':list(range(24)),





    }




    return render(request,'hello.html',context)