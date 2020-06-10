# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    #这里可以统计字数，但是在前端怎么显示出来呢？
    # print(len(request.GET['text']))
    # return render(request, 'count.html')

    user_text = request.GET['text']
    tatol_count = len(user_text)
    #后面的属性都是传递参数
    #传递的参数必须是一个字典形

    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
     #元组排序分类必须加一个items，不然他就排序不了。
    sorted_dict = sorted(word_dict.items(), key=lambda w: w[1], reverse=True)
    return render(request, 'count.html', {'count': tatol_count,'text': user_text,'sorted':sorted_dict})