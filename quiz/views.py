from rest_framework.response import Response
from .models import Main_field,Category,Sub_category,Question,Answers
from .api.serializers import MainSerializer,CategorySerializer,SubCatSerializer,QuestionSerializer,AnsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

# Create your views here.
class StartField(ModelViewSet):
    queryset = Main_field.objects.all()
    serializer_class = MainSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

class SubCategry(ModelViewSet):
    queryset = Sub_category.objects.all()
    serializer_class = SubCatSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

class QuestionView(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]


class AnswerView(ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnsSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]


