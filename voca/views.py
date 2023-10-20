from django.shortcuts import render
from .models import Voca
from .forms import VocaInputForm, VocaEditForm
from django.views.generic import DetailView, CreateView, UpdateView
from datetime import date, timedelta, datetime
import random


# Create your views here.
def home(request):
    words = Voca.objects.all()
    words_3d = []
    words_7d = []
    words_14d = []
    words_30d = []
    word_2_review = []
    word_pool = []
    pooling_word = 'Nothing'

    def extract_day(ini_list, crit, input_date=0):
        for word in words:
            if (date.today() - timedelta(days=crit)) <= word.created.date() <= (date.today() - timedelta(days=input_date)):
                ini_list.append(word)
        return ini_list
    
    for word in words:
        if word.created.date() == date.today() - timedelta(days=3) or word.created.date() == date.today() - timedelta(days=7) or word.created.date() == date.today() - timedelta(days=14) or word.created.date() == date.today() - timedelta(days=30):
            word_2_review.append(word)
        if word.created.date() < date.today() - timedelta(days=30):
            word_pool.append(word)    

    three_day = extract_day(words_3d, 3)
    a_week = extract_day(words_7d, 7, 3)
    two_week = extract_day(words_14d, 14, 7)
    a_month = extract_day(words_30d, 30, 14)
    # consider the empty word-pool
    if len(word_pool)>0:
        pooling_word = random.choice(word_pool)

    # for word in words:
    #     print(word.created.day)
    #     print(word.word_entry)
    #     print(word.created.date())
    #     three_day = word.created.date() - timedelta(days=3)
    #     print(three_day, date.today())
    #     test_day = word.created.date() + timedelta(days=1)
    #     if test_day == date.today():
    #         print('yes')
    #     else: print('no')
    #     x=date.today() - word.created.date()
    #     if x > timedelta(days=2): print('oh yeah') 
    #     else: print('oh no') 
    #     print()
    today_date = datetime.now().day
    return render(request, 'voca/home.html', {'words':words, 'today_date':today_date, 'three_day':three_day, 'a_week':a_week, 'two_week':two_week, 'a_month':a_month, 'word_2_review':word_2_review, 'pooling_word':pooling_word, 'word_pool': word_pool, 'today_word': pooling_word})


class WordDetailView(DetailView):
    model = Voca
    template_name = 'voca/voca_detail.html'


class AddWordView(CreateView):
    model = Voca
    form_class = VocaInputForm
    template_name = 'voca/add_word.html'


class EditWordView(UpdateView):
    model = Voca
    form_class = VocaEditForm
    template_name = 'voca/edit_word.html'

