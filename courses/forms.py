from django import forms

from .models import Course


class CourseForm(forms.ModelForm):
    """Form for add new items to Course database through the site

    image - set the field as not obligatory.

    """
    def __init__(self, *args, **kwards):
        """For changing titles."""
        super(CourseForm, self).__init__(*args, **kwards)
        self.fields['slug'].label = 'Название URL'
        self.fields['title'].label = 'Название курса'
        self.fields['description'].label = 'Описание курса'
        self.fields['image'].label = 'Изображение курса'

    class Meta:
        """Meta class that address to database.

        model - database.
        fields - the display order database's fields in the html page.

        """
        model = Course
        fields = ['slug', 'title', 'description', 'image']