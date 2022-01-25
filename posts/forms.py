from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Posts, Tags, PostsAndTags, Comments
from ckeditor.fields import RichTextField

categories = (
    ("Games", "Games"),
    ("Automotive", "Automotive"),
    ("Clothes", "Clothes"),
    ("Electronics", "Electronics"),
    ("Books", "Books"),
)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts

        fields = [
            'title',
            'tags',
            'content',
            'postPicture',
        ]

    title = forms.CharField(label='Title:', widget=forms.TextInput(attrs={"placeholder": "Title"}))
    tags = forms.CharField(label='Tags:', widget=forms.TextInput(attrs={"placeholder": "Tags"}))
    content = forms.CharField(widget=CKEditorWidget())
    postPicture = forms.FileField(label='Post picture:')


class CreateTagForm(forms.ModelForm):
    class Meta:
        model = Tags

        fields = [
            'tagContent',
        ]


class CreatePostTagForm(forms.ModelForm):
    class Meta:
        model = PostsAndTags

        fields = [
            'postID',
            'tagID',
        ]


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comments

        fields = [
            'comment',
        ]