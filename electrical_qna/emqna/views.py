from django.conf import settings
from django.shortcuts import render, redirect
from google import genai
from .models import QnaRecord
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('ask_question')
        else:
            messages.error(request, 'Registration failed. Invalid information.')
    else:
        form = UserRegisterForm()
    
    return render(request, 'emqna/register.html', {'form': form})

@login_required 
def ask_question(request):
    
    api_key = settings.GEMINI_API_KEY 
    answer_text = None
    
    if not api_key:
        return render(request, "emqna/ask_question.html", {"error": "Error: API Key is not configured."})
        
    client = genai.Client(api_key=api_key) 
    
    if request.method == "POST":
        question_text = request.POST.get("question") 
        
      
        system_instruction = (
       "You must answer ONLY Electrical Machines questions. Keep all answers short and clear. "
        "If the question is unrelated, reply only: "
       "'I can only answer queries related to Electrical Machines. Please ask an Electrical Machines related question.'"
        )

        
        contents = [
            system_instruction,
            f"User Question: {question_text}"
        ]
        
        try:
            completion = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=contents
            )
            
           
            answer_text = completion.text.strip() if completion.text else "AI returned an empty response."
        
        except Exception as e:
            answer_text = f"Error retrieving AI response: {e}"

        QnaRecord.objects.create(
            user=request.user, 
            question_text=question_text,
            answer_text=answer_text
        )
        
        return redirect("ask_question")
        
    questions = QnaRecord.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        "questions": questions,
    }
    return render(request, "emqna/ask_question.html", context)