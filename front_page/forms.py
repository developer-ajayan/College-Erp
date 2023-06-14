from django import forms
from .models import *

class CollegeInformationForm(forms.ModelForm):
    class Meta:
        model = CollegeInformation
        fields = ('name', 'address', 'email', 'phone', 'logo')



# class VideoFormWidget(forms.widgets.FileInput):
#     template_name = 'video_widget.html'

class FrontPageForm(forms.ModelForm):
    class Meta:
        model = VideoWidget
        fields = ('vision', 'mission', 'core_values','video')
    

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Noticeboard
        fields = ('title', 'content')
    def save(self,request,commit=True, *args, **kwargs):
    
        instance = super(NoticeForm, self).save(commit=False)
        if not instance.id:
            # New notice being created, set the "posted_by" field
            instance.posted_by = request.user
        if commit:
            instance.save()
        return instance