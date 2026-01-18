from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Quiz, QuizUser
from .forms import QuizForm
from rest_framework import generics
from .serializers import QuizSerializer
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404

# Create your views here.

class QuizList(ListView):
    model = Quiz
    context_object_name = "quizes"
    template_name = "quiz_app/quiz_list.html"

class QuizDetail(DetailView):
    model = Quiz
    context_object_name = "quiz"
    template_name = "quiz_app/quiz_detail.html"
    
    def post(self, request, pk):
        quiz = get_object_or_404(Quiz, pk = pk)
        if not request.user:
            raise Http404()
        quiz_user = QuizUser.objects.filter(user = request.user, quiz = quiz).first()
        if not quiz_user:
            quiz_user = QuizUser.objects.create(user = request.user, quiz = quiz)
        
        return redirect("quiz_play", pk = quiz_user.pk)
        

class QuizCreate(CreateView):
    model = Quiz
    context_object_name = "quiz"
    template_name = "quiz_app/quiz_create.html"
    form_class = QuizForm
    success_url = "/"

    def __str__(self):
        return self.name
    

class QuizUpdate(UpdateView):
    model = Quiz
    context_object_name = "quiz"
    template_name = "quiz_app/quiz_update.html"
    form_class = QuizForm

    def __str__(self):
        return self.name
    
    def get_success_url(self):
        return "/quiz/" + str(self.object.pk)

class QuizDelete(DeleteView):
    model = Quiz
    context_object_name = "quiz"
    template_name = "quiz_app/quiz_delete.html"
    success_url = "/"

    def __str__(self):
        return self.name
    
class QuizPlay(QuizDetail):
    model = QuizUser
    context_object_name = "quiz_user"
    template_name = "quiz_app/quiz_play.html"
#API

class QuizListAPI(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    