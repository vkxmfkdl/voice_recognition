from django.shortcuts import render
from .forms import UploadFileForm
from .models import UploadFileModel
from . import sentiment as stm
from . import read_analysis
from datetime import datetime
from collections import Counter
# Create your views here.

# 감성 분석 모델 관련 패키지#
from tensorflow.keras import models
from tensorflow.keras.models import load_model
import json
import os
from pprint import pprint
from konlpy.tag import Okt
import numpy as np
import nltk

model = load_model('sentimental/meeting_mlp_model.h5')

if os.path.isfile('sentimental/train_docs.json'):
        with open('sentimental/train_docs.json', encoding='utf-8') as f:
            train_docs = json.load(f)
okt = Okt()
selected_words=[]

def index(request):
    return render(request, 'index.html')
    
def load(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('files') #field name in model
        if form.is_valid():
            for f in files:
                file_instance = UploadFileModel(files=f)
                file_instance.save()
        else:
            print('load failed')
        
        return render(request, 'load.html', {'form':form})
    
def result(request):
    return render(request, 'result.html')


def login_ok(request):
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
    
    return render(request, 'login_ok.html')

def content(request):
    # 오늘 날짜로 폴더 찾기
    now = datetime.now()
    digital_month = str(now.month)
    if(now.month < 10):
        digital_month = "0"+digital_month
    digital_day = str(now.day)
    if(now.day < 10):
        digital_day = "0"+digital_day
    dirname = "media\\"+str(now.year)+"-"+digital_month+"-"+digital_day+"\\"

    sas = stm.sentiment()
    sas.sentimental_analysis(dirname)
    content_list = sas.get_list()
    return render(request, 'content.html',{"list":content_list})


def detail_analysis(request):
    # 오늘 날짜로 폴더 찾기
    now = datetime.now()
    digital_month = str(now.month)
    if(now.month < 10):
        digital_month = "0"+digital_month
    digital_day = str(now.day)
    if(now.day < 10):
        digital_day = "0"+digital_day
    dirname = "media\\"+str(now.year)+"-"+digital_month+"-"+digital_day+"\\"

    ras = read_analysis.read_analysis()
    speech_list = ras.sum_json_file(dirname)
    thetext = ras.all_text_merge()

    # 텍스트 요약    
    summarize_text = ras.data_summarize(4)
    import_keywords = ras.data_keywords(10)

    talker_list = set() # 회의 참여자
    list_of_talker = []
    speech_time = 0
    min_speech_time = 0xFFFFFF
    max_speech_time = 0
    for s in speech_list:
        talker_list.add(s["name"])
        list_of_talker.append(s["name"])
        max_speech_time = max(s["time"], max_speech_time)
        min_speech_time = min(s["time"], min_speech_time)
    
    #발화시간 계산
    speech_time = max_speech_time - min_speech_time
    speech_time = round(speech_time, 2)
    # talker_list = ['민철', '민재', '경민']
    talker_list = list(talker_list) # 발화자
    number_of_participants = len(talker_list) # 발화자 수
    # number_of_talker = Counter{"민철":20, "민재":30, "경민":24}
    number_of_talker = []
    for k, n in Counter(list_of_talker).items():
        number_of_talker.append(n)
    # number_of_talker = Counter(list_of_talker)  # 발화 수
    total_talk = 0
    for n in number_of_talker:
        total_talk += n

    sas = stm.sentiment()
    sas.sentimental_analysis(dirname)
    state_list = set()
    sentimental_list = sas.get_list()
    list_of_sent = []
    number_of_sentimental = []
    for s in sentimental_list:
        list_of_sent.append(s["state"])

    # number_of_sentimental = [80, 40, 60]
    for k, n in Counter(list_of_sent).items():
        number_of_sentimental.append(n)

    number_of_keywords = []
    for ls in import_keywords:
        number_of_keywords.append(ras.get_text().count(ls))

    context = {
        "summarize_text" : summarize_text,
        "import_keywords" : import_keywords,
        "number_of_keywords" : number_of_keywords,
        "talker_list" : talker_list,
        "number_of_talker" : number_of_talker,
        "total_talk" : total_talk,
        "number_of_sentimental" : number_of_sentimental,
        "speech_time" : speech_time,
        "number_of_participants" : number_of_participants,
    }
    print(context)
    return render(request, 'detail_analysis.html', context)

def main(request):
    return render(request, 'main.html')