from .models import Article, Relationship, Tag

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet



class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inline = [RelationshipInline]
    list_display = ('id', 'title', 'text', 'published_at', 'image')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
