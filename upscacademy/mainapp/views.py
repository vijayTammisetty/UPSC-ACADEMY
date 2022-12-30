from django.shortcuts import render
from adminapp.models import UpscInterviewVideos, UpscMockTest, UpscStudyMaterial
from aspirantapp.models import AspirantsModel,AspirantFeadbackModel
from aspirantapp.models import AspirantsModel

# Create your views here.


def home(request):
    aspirants = AspirantsModel.objects.all().count()
    materials = UpscStudyMaterial.objects.all().count()
    videos = UpscInterviewVideos.objects.all().count()
    mock_test = UpscMockTest.objects.all().count()
    feedbacks=AspirantFeadbackModel.objects.all().order_by('-feadback_id')[0:4]
    context = {
        'aspirants':aspirants,
        'materials':materials,
        'videos':videos,
        'mock_test':mock_test,
        'feedback':feedbacks,
    }

    return render(request,'main/index.html', context)

# def admin(request):
#     return render(request,'main/admin-login.html')



def about(request):
    return render(request,'main/about.html')

def course(request):
    return render(request,'main/courses.html')

def contact(request):
    return render(request,'main/contact.html')

