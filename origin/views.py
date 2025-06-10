from django.shortcuts import render, get_object_or_404
from .models import Question, UserResponse
from .forms import ResponseForm

def answer_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            # محاسبه درصد تطابق
            user_answer = form.cleaned_data['answer'].lower()
            keywords = question.get_keywords_list()
            matched = sum(1 for k in keywords if k in user_answer)
            progress = (matched / len(keywords)) * 100 if keywords else 0
            
            # ذخیره پاسخ
            UserResponse.objects.create(
                user=request.user,
                question=question,
                answer=form.cleaned_data['answer'],
                progress=progress
            )
            return render(request, 'result.html', {'progress': progress})
    else:
        form = ResponseForm()
    
    return render(request, 'question.html', {
        'question': question,
        'form': form
    })