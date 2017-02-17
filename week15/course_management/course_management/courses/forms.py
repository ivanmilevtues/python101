from django import forms
from courses.models import Course


class CreateCourseForm(forms.Form):
    course_name = forms.CharField(max_length=128, label='Course Name:')
    desc = forms.CharField(max_length=264, label='Description:')
    start_date = forms.DateField(widget=forms.SelectDateWidget,
                                 label='Start Date:')
    end_date = forms.DateField(widget=forms.SelectDateWidget,
                               label='End Date:')

    def save(self, commit=True):
        course = Course.objects.create(name=self.cleaned_data['course_name'],
                                       description=self.cleaned_data['desc'],
                                       start_date=self.cleaned_data['start_date'],
                                       end_date=self.cleaned_data['end_date'])

        course.save()
        return course


class EditCourseForm(forms.Form):
    course_name = forms.CharField(max_length=128, label='Course Name:',
                                  required=False)
    description = forms.CharField(max_length=264,
                                  label='Description:', required=False)
    start_date = forms.DateField(widget=forms.SelectDateWidget,
                                 label='Start Date:', required=False)
    end_date = forms.DateField(widget=forms.SelectDateWidget,
                               label='End Date:', required=False)
