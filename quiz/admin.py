# from django.contrib import admin
# from .models import *

# # Register your models here.
# @admin.register(Main_field)
# class MainAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Main_field._meta.fields]

# @admin.register(Category)
# class MainAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Category._meta.fields]

# @admin.register(Sub_category)
# class MainAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Sub_category._meta.fields]


from django.contrib import admin
from .models import Main_field, Category, Sub_category,Question,Answers

# Inline for Category within Main_field
class CategoryInline(admin.StackedInline):
    model = Category
    fk_name = 'main_field_name'  # Specify the ForeignKey field
    extra = 1           #by this only 1 extra field will be showed there

# Inline for Sub_category within Category
class SubCategoryInline(admin.StackedInline):
    model = Sub_category
    fk_name = 'main_category'  # Specify the ForeignKey field
    extra = 1                   #by this only 1 extra field will be showed there

class QuestInline(admin.StackedInline):
    model = Question
    fk_name = 'ques_sub'
    extra = 1

class AnswerInline(admin.StackedInline):
    fk_name = 'question_Ans'
    model = Answers
    extra = 1

@admin.register(Answers)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Answers._meta.fields]


@admin.register(Question)
class QuestiondAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]                #write the lower level model name in upper model- like answer model is connected with question model
    list_display = [field.name for field in Question._meta.fields]

@admin.register(Main_field)
class MainFieldAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    list_display = [field.name for field in Main_field._meta.fields]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline]
    list_display = [field.name for field in Category._meta.fields]

@admin.register(Sub_category)
class SubCategoryAdmin(admin.ModelAdmin):
    inlines = [QuestInline]
    list_display = [field.name for field in Sub_category._meta.fields]

