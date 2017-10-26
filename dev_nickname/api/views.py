from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .serializers import TodoSerializer
from django.http import HttpResponse
from django.shortcuts import render
from .forms import NameForm
from .character_converter import chara2romaji
from .romaji_converter import romaji2hiragana
from .romaji_converter import romaji2katakana
import json


def hiragana(request):
    if request.method == 'POST':
        
        # 配列を作成
        dic = []
        
        for key in request.POST:
        
         # 送られてきたリクエストを全てローマ字変換
         n = chara2romaji(request.POST[key])

         # 全てローマ字に変換された文字列をひらがなに変換
         nickname = romaji2hiragana(n)
         
         # 配列にセット
         dic.append({key:nickname + "さん"})
        
        
        # json形式に変換
        result = json.dumps(dic, ensure_ascii=False)
        
        # 結果を返す
        response = HttpResponse(content=result, content_type='application/json; charset=UTF-8', status=200)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
        
    else:
        
        # フォーム表示
         form = NameForm()
         return render(request, 'name.html', {'form': form})


def katakana(request):
    if request.method == 'POST':
        
        # 配列を作成
        dic = []
        
        for key in request.POST:
        
         # 送られてきたリクエストを全てローマ字変換
         n = chara2romaji(request.POST[key])

         # 全てローマ字に変換された文字列をカタカナに変換
         nickname = romaji2katakana(n)
         
         # 配列にセット
         dic.append({key:nickname + "さん"})
        
        
        # json形式に変換
        result = json.dumps(dic, ensure_ascii=False)
        
        # 結果を返す
        response = HttpResponse(content=result, content_type='application/json; charset=UTF-8', status=200)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
        
    else:
        
        # フォーム表示
         form = NameForm()
         return render(request, 'name.html', {'form': form})
