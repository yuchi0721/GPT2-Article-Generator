from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from GPT2_Chinese_master.generate import * 

def produce_content(request):
    if request.method=='POST':
        keyword=request.POST['keyword']
        length=request.POST['length']
        paragraph=request.POST['paragraph']
        industry=request.POST['industry']
        print(industry)
        produced_content_temp=generate_main('[CLS]'+keyword,industry,int(length),int(paragraph))
        produced_content=''
        for paragraph in produced_content_temp:
            paragraph=paragraph.replace('[UNK]','')
            produced_content+=paragraph+'\n\n'  
    return render(request,'genarate.html',locals())

def index(request):
    return render(request,'index.html')

