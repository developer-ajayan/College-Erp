from multiprocessing import context
from . models import *
def college_info(self):
    college =CollegeInformation.objects.first()
    context={}
    context['college']=college
    context['video_widget']=VideoWidget.objects.first()
    return context