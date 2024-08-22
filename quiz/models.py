from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Main_field(BaseModel):
    Field_name = models.CharField(max_length=200)

    def __str__(self):
        return self.Field_name
    
class Category(BaseModel):
    # field = models.ForeignKey(Main_field,on_delete=models.CASCADE,related_name='field')
    main_field_name = models.ForeignKey(Main_field,on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name
    
class Sub_category(BaseModel):
    main_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    Main_field_name = models.ForeignKey(Main_field,on_delete=models.CASCADE)
    sub_cat_name = models.CharField(max_length=200)

    def __str__(self):
        return self.sub_cat_name
    
class Question(BaseModel):
    Levels_Choice = [('Easy','Easy'),("Medium","Medium"),("Hard","Hard")]
    main_field_name = models.ForeignKey(Main_field,on_delete=models.CASCADE)
    main_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    ques_sub = models.ForeignKey(Sub_category,on_delete=models.CASCADE)
    Level = models.CharField(max_length=50,choices=Levels_Choice)
    Question = models.CharField(max_length=500)
    marks = models.IntegerField()
    
    def __str__(self):
        return self.Question[:50]
    
class Answers(BaseModel):
    answer = models.CharField(max_length=250)
    is_correct = models.BooleanField(default=False)
    question_Ans = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.answer[:50]
