from django.shortcuts import render
import random

def lotto(request) :
    return render(request, 'lotto.html')

def result(request) :
    if request.method == "POST" :
        gameNum = int(request.POST['gameNum'])
        lottoList = []
        while len(lottoList) < gameNum :
            lottoSet = random.sample(range(1,46),6)
            lottoSet.sort()
            #만약 여러개의 로또 번호 추출 세트중 중복이 발생할 시 추가하지 않음
            for i in lottoList:
                if(i == lottoSet):
                    continue
            lottoList.append(lottoSet)
        data = {
            "gameNum" : gameNum,
            "lottoList" : lottoList
        }
        return render (request, 'result.html', data)
# Create your views here.
