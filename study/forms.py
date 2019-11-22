from django import forms

from .models import Test, Quest, Answer, Schools

class TestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = ('title', 'author',)
    
    class Meta1:
        model = Quest
        fields = ('question', 'test')
        
    class Meta2:
        model = Answer
        fields = ('answer', 'quest')
