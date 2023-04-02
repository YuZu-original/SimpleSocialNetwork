from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.safestring import mark_safe

from network.models import Post, Comment
from utils.utils import calculate_age


@admin.display(description="Автор")
def author_link(obj):
    return mark_safe(
        '<a href="{}">{}</a>'.format(
            reverse("admin:core_user_change", args=(obj.author.pk,)),
            obj.author,
        )
    )


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    def clean(self):
        author = self.cleaned_data.get("author")
        if author:
            age = calculate_age(author.date_of_birth)
            if age < 18:
                raise ValidationError(
                    "You're still young. The minimum age is 18 years."
                )

        title = self.cleaned_data.get("title")
        if title:
            words = set(title.split())
            intersection = words & {"ерунда", "глупость", "чепуха"}
            if intersection:
                raise ValidationError(
                    "This field should not contain the words: %s."
                    % ", ".join(intersection)
                )

        return self.cleaned_data


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "text", author_link)
    readonly_fields = (author_link, "created_at", "updated_at")
    list_filter = ("created_at",)
    inlines = (CommentInline,)
    form = PostForm


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", author_link, "post_link")
    readonly_fields = (author_link, "post_link", "created_at", "updated_at")

    @admin.display(description="Пост")
    def post_link(self, obj):
        return mark_safe(
            '<a href="{}">{}</a>'.format(
                reverse("admin:network_post_change", args=(obj.post.pk,)),
                obj.post.title,
            )
        )
