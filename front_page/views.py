from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages

from django.views import View
from .forms import *
import json
from django.http import HttpResponse
# Create your views here.
class FrontpageView(View):
    def get(self,request,*args,**kwargs):
        template_name="front_page.html"
        return render(request,template_name)


def create_college(request):
    if request.method == 'POST':
        form = CollegeInformationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CollegeInformationForm()
    
    return render(request, 'front_page_college_info_form.html', {'form': form})

def edit_college(request, pk):
    college = get_object_or_404(CollegeInformation, pk=pk)

    if request.method == 'POST':
        form = CollegeInformationForm(request.POST, request.FILES, instance=college)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CollegeInformationForm(instance=college)

    return render(request, 'front_page_college_info_form.html', {'form': form})


def create_frontpage(request):
    if request.method == 'POST':
        form = FrontPageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')  # Replace 'home' with the URL name for the home page
    else:
        form = FrontPageForm()
    
    return render(request, 'create_frontpage.html', {'form': form})


def edit_frontpage(request, pk):
    college = get_object_or_404(VideoWidget, pk=pk)

    if request.method == 'POST':
        form = FrontPageForm(request.POST, request.FILES, instance=college)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FrontPageForm(instance=college)

    return render(request, 'create_frontpage.html', {'form': form})

def create_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect('list_notice')
    else:
        form = NoticeForm()
    
    return render(request, 'create_notice.html', {'form': form})

def edit_notice(request, notice_id):
    notice = get_object_or_404(Noticeboard, id=notice_id)
    
    if request.method == 'POST':
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save(request)
            return redirect('list_notice')
    else:
        form = NoticeForm(instance=notice)
    
    return render(request, 'create_notice.html', {'form': form})


def delete_notice(request):
    resp={'status' : 'failed', 'msg':''}
    if request.method == 'POST':
        id = request.POST['id']
        notice = get_object_or_404(Noticeboard, id=id)
        if notice:
            try:
                notice.delete()
                resp['status'] = 'success'
                messages.success(request,'Class has been deleted successfully.')
            except Exception as e:
                raise print(e)
            return HttpResponse(json.dumps(resp),content_type="application/json")
    return redirect('list_notice')


def list_notice(request):
    notices = Noticeboard.objects.all()
    context={}
    context['page_title'] = "Class Management"
    context['notices'] = notices
    return render(request, 'list_notice.html',context)
