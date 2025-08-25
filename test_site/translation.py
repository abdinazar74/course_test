from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Exam)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'questions')

@register(Assingment)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Review)
class ProductTranslationOptions(TranslationOptions):
    fields = ('comment',)

@register(Course)
class ProductTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')


