from django.urls import path
from .views import QuizCreate, QuizDelete, QuizList, QuizUpdate, QuizDetail, QuizListAPI, QuizPlay

urlpatterns = [
    path("", QuizList.as_view(), name = "quiz_list"),
    path("quiz/create/", QuizCreate.as_view(), name = "quiz_create"),
    path("quiz/delete/<int:pk>", QuizDelete.as_view(), name = "quiz_delete"),
    path("quiz/update/<int:pk>", QuizUpdate.as_view(), name = "quiz_update"),
    path("quiz/<int:pk>", QuizDetail.as_view(), name = "quiz_detail"),
    path("quiz/play/<int:pk>", QuizPlay.as_view(), name = "quiz_play"),
    #api
    path("API/quiz_list", QuizListAPI.as_view(), name = "quiz_listAPI")
]
