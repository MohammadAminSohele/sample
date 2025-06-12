from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Question , Catagory
from .forms import ResponseForm

import re

def calculate_progress(answer, keywords):
    answer = answer.lower()
    matched = 0
    
    for keyword in keywords:
        # استفاده از regex برای تطابق دقیق کلمات
        pattern = r'\b' + re.escape(keyword) + r'\b'
        if re.search(pattern, answer):
            matched += 1
    
    return (matched / len(keywords)) * 100 if keywords else 0

def answer_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            # محاسبه درصد تطابق
            user_answer = form.cleaned_data['answer'].lower()
            keywords = question.get_keywords_list()
            progress=calculate_progress(user_answer,keywords)
            unused_keywords = [keyword for keyword in keywords if keyword.lower() not in user_answer]
            context =  {
                'progress':progress,
                'unused_keywords':unused_keywords
            }
            return render(request, 'result.html',context)
    else:
        form = ResponseForm()
    
    return render(request, 'question.html', {
        'question': question,
        'form': form
    })

class Question_List(ListView):
    template_name = 'question_list.html'
    queryset=Question.objects.all()

def Question_List_By_Catagory(request, slug):
    category = get_object_or_404(Catagory, slug=slug)
    questions = category.questions.all()  # Access related questions via ManyToManyField
    return render(request, "Question_List_By_Catagory.html", {"category": category, "questions": questions})
    