from django import forms
from .models import Comment, Watch


class FeedbackForm(forms.Form):
    rating_site = forms.ChoiceField(
        label='Оцените сайт по 5-бальной шкале',
        choices=[(1, '1 - Очень плохо'), (2, '2 - Плохо'), (3, '3 - Средне'), (4, '4 - Хорошо'), (5, '5 - Отлично')],
        widget=forms.RadioSelect(),
        required=True
    )
    rating_design = forms.ChoiceField(
        label='Оцените дизайн сайта',
        choices=[(1, '1 - Очень плохо'), (2, '2 - Плохо'), (3, '3 - Средне'), (4, '4 - Хорошо'), (5, '5 - Отлично')],
        widget=forms.RadioSelect(),
        required=True
    )
    suggestions = forms.CharField(
        label='Ваши пожелания',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        required=False
    )
    recommend = forms.BooleanField(
        label='Рекомендуете ли сайт другим?',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    feedback_type = forms.ChoiceField(
        label='Тип отзыва',
        choices=[('positive', 'Положительный'), ('negative', 'Отрицательный')],
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Оставьте комментарий...'}),
        }
        labels = {
            'text': '',
        }


class WatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ['brand', 'model', 'description', 'price', 'image']