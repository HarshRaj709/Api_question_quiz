from rest_framework import serializers
from quiz.models import Main_field,Category,Sub_category,Question,Answers


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main_field
        fields = '__all__'

class FieldNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main_field
        fields = ['Field_name'] 

class CategorySerializer(serializers.ModelSerializer):
    # field = FieldNameSerializer()
    class Meta:
        model = Category
        fields = '__all__'

class CategoryName(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

class SubCatSerializer(serializers.ModelSerializer):
    # main_category = CategoryName()
    class Meta:
        model = Sub_category
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    # main_field_name = serializers.CharField(source='main_field_name.Field_name', read_only=True)
    # main_category = serializers.CharField(source='main_category.category_name', read_only=True)
    # ques_sub = serializers.CharField(source='ques_sub.sub_cat_name', read_only=True)
    class Meta:
        model = Question
        fields = '__all__'

class QuestionName(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['Question']

class AnsSerializer(serializers.ModelSerializer):
    # question_Ans = QuestionName()
    class Meta:
        model = Answers
        fields = '__all__'