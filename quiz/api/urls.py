from rest_framework.routers import DefaultRouter
from django.urls import path,include
from quiz.views import StartField,CategoryView,SubCategry,AnswerView,QuestionView

router = DefaultRouter()
router.register('Main_Field',StartField,basename='Start')
router.register('Category',CategoryView,basename='Categories')
router.register('Sub_category',SubCategry,basename='SubCat')
router.register('question',QuestionView,basename='question')
router.register('Answer',AnswerView,basename='Answer')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'))
    # path('field/',StartField.as_view(),name='Field')
]
