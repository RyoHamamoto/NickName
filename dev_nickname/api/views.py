from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .serializers import TodoSerializer
from django.http import HttpResponse
from django.shortcuts import render
from .forms import NameForm
from .character_converter import chara2romaji
from .romaji_converter import romaji2hiragana
import json

def name(request):
    if request.method == 'POST' and request.POST["name"]:
        
        # 送られてきたリクエストを全てローマ字変換
        n = chara2romaji(request.POST["name"])

        # 全てローマ字に変換された文字列をひらがなに変換
        nickname = romaji2hiragana(n)
        
        # 配列を作成
        dic = []
        
        # 配列にセット
        dic = [("name", nickname + "さん")]
        
        # json形式に変換
        result = json.dumps(dic, ensure_ascii=False)
        
        # 結果を返す
        response = HttpResponse(content=result, content_type='application/json; charset=UTF-8', status=200)
        return response
        
        
        # return render(request, 'name.html', {'namae': response})
    else:
        # response = HttpResponseNotFound()
        # return resopnse
        
        # フォーム表示
         form = NameForm()
         return render(request, 'name.html', {'form': form})


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer