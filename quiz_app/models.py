from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = "quiz_image", blank = True, null = True)

class QuizUser(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    data_win = models.DateTimeField(auto_now_add = True)

class Question(models.Model):
    text = models.CharField(max_length = 120)
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE, related_name = "questions")
    image = models.ImageField(blank = True, null = True)
    video = models.FileField(blank = True, null = True)

class Answer(models.Model):
    correct = models.BooleanField()
    text = models.CharField(max_length = 120)
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name = "answers")

class UserAnswer(models.Model):
    quiz_user = models.ForeignKey(QuizUser, on_delete = models.CASCADE)
    user_question = models.ForeignKey(Question, on_delete = models.CASCADE)
    user_answer = models.ForeignKey(Answer, on_delete = models.CASCADE)

class Results(models.Model):
    points = models.IntegerField()
# Create your models here.
