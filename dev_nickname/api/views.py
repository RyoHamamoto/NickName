from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .serializers import TodoSerializer
from django.http import HttpResponse
from django.shortcuts import render
from .forms import NameForm
from .character_converter import chara2romaji
from .romaji_converter import romaji2hiragana
from .romaji_converter import romaji2katakana
from collections import OrderedDict
import json
import mojimoji


def hiragana(request):
    print(request.POST)
    if request.method == 'POST':
        
        # 配列を作成
        od = OrderedDict()

        for key in sorted(request.POST):
         
            # アルファベット以外半角を全角へ変換する処理
            nam  = mojimoji.zen_to_han(request.POST[key])
            name = mojimoji.han_to_zen(nam, ascii=False)
            
            # 送られてきたリクエストを全てローマ字変換
            n = chara2romaji(name)
    
            # 全てローマ字に変換された文字列をひらがなに変換
            nickname = romaji2hiragana(n)
             
            # 配列にセット
            if nickname != "":
                od[key] = nickname + "さん"
            else:
                od[key] = nickname
            
        # json形式に変換
        result = json.dumps(od, ensure_ascii=False)
        
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
        od = OrderedDict()
        
        for key in sorted(request.POST):
        
            # アルファベット以外半角を全角へ変換する処理
            nam  = mojimoji.zen_to_han(request.POST[key])
            name = mojimoji.han_to_zen(nam, ascii=False)
            
            # 送られてきたリクエストを全てローマ字変換
            n = chara2romaji(name)
    
            # 全てローマ字に変換された文字列をカタカナに変換
            nickname = romaji2katakana(n)
             
             # 配列にセット
            if nickname != "":
                od[key] = nickname + "さん"
            else:
                od[key] = nickname
        
        
        # json形式に変換
        result = json.dumps(od, ensure_ascii=False)
        
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
