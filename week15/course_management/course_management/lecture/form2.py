from django.forms import ModelForm
from lecture.models import Lecture


class CreateLectureForm(ModelForm):
    class Meta:
        model = Lecture
        fields = '__all__'
