from django.shortcuts import render,redirect,get_object_or_404
from aspirantapp.models import AspirantsModel,AspirantFeadbackModel
# from aspirantapp.views import materials, videos
from .models import UpscStudyMaterial,UpscInterviewVideos,UpscMockTest
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.


def admin_login(request):
    if request.method == 'POST':
        admin_Name = request.POST.get('admin-name')
        admin_password = request.POST.get('admin-password')
        # user = User.objects.create(admin_Name=admin_Name, admin_password=admin_password)
        
        if admin_Name == 'admin' and admin_password == 'admin':
            messages.success(request, 'Admin Logined successfully ')
            return redirect('admin-dashbord')

        else:
            messages.warning(request,'Invalid User name and password')
            return redirect('admin-login')

    return render(request,'admin/admin-login.html')


def admin_dashbord(request):
    aspirants = AspirantsModel.objects.all().count()
    materials = UpscStudyMaterial.objects.all().count()
    videos = UpscInterviewVideos.objects.all().count()
    mock_test = UpscMockTest.objects.all().count()

    context = {
        'aspirants':aspirants,
        'materials':materials,
        'videos':videos,
        'mock_test':mock_test,
    }

    return render(request, 'admin/admin-dashbord.html', context)

def pending_aspirants(request):
    data = AspirantsModel.objects.filter(status='Pending')

    paginater = Paginator(data, 3)
    page_number = request.GET.get('page')
    page = paginater.get_page(page_number)

    print(data)
    print("hello")
    return render(request,'admin/pending-aspirants.html',{'data':page})


def accept(request,id):
    print(id,'hi')
    data = AspirantsModel.objects.get(aspirant_id=id)
    # data = get_object_or_404(AspirantsModel,aspirant_id=id)
    data.status='Accept'
    data.save(update_fields=['status'])
    data.save()
    messages.success(request,"New aspirant accepted successfully")
    return redirect('pending-aspirants')

def reject(request,id):
   ta = AspirantsModel.objects.get(aspirant_id=id)
   ta.delete()
   messages.success(request, 'Aspirant rejected successfully')
   return redirect('pending-aspirants')


def all_aspirants(request):
    # aspirants = AspirantsModel.objects.filter(status='Accept')
    aspirants = AspirantsModel.objects.all()

    paginater = Paginator(aspirants, 3)
    page_number = request.GET.get('page')
    page = paginater.get_page(page_number)
    
    return render(request,'admin/all-aspirants.html', {'aspirants':page})

def delete_aspirant(request,id):
    ta = AspirantsModel.objects.get(aspirant_id=id)
    ta.delete()
    messages.success(request, 'Aspirant deleted successfully')
    return redirect('all-aspirants')


def add_study_material(request):
    if request.method== 'POST':
        title = request.POST.get('title')
        subject = request.POST.get('Subject_name')
        material_file = request.FILES['files']
        photo = request.FILES['material_photo']
        # print(photo)
        filename = material_file.name
        image = photo.name
        if (filename and filename.rsplit('.',1)[1].lower() in ['pdf','docx']) and (image and image.rsplit('.',1)[1].lower() in ['jpg','jpeg','png','gif']) :
            # if filename.rsplit('.',1)[1].lower() in ['pdf']:
            #     filename = title+'_'+str(id)+'.pdf'

            UpscStudyMaterial.objects.create(title=title,subject_name=subject, uploded_file=material_file, uplode_photo=photo)
            messages.success(request, 'Material has been added successfully')
            return redirect('add-study-material')
        else:
            messages.error(request, 'Please Upload valid pdf or docx document or image')
            return redirect('add-study-material')
     
    return render(request, 'admin/add-study-material.html')

def manage_study_material(request):
    all_materials = UpscStudyMaterial.objects.all().order_by('-material_id')

    paginater = Paginator(all_materials, 3)
    page_number = request.GET.get('page')
    page = paginater.get_page(page_number)

    return render(request,'admin/manage-study-material.html',{'all_materials':page})


def edit(request,id):
    material = UpscStudyMaterial.objects.get(material_id=id)
    data = UpscStudyMaterial.objects.get(material_id=id)
    if request.method== 'POST' :
        title = request.POST.get('text')
        subject = request.POST.get('name')
        # photo1 = request.FILES['file']
        # photo2 = request.FILES['material-photo']
        
        if not request.FILES.get('file',False):
            # print('all up ex ph')
            data.title= title
            data.subject_name= subject

        if request.FILES.get('file',False):
            # print('first photo upo')
            file = request.FILES['file']
            data.title= title
            data.subject_name= subject
            data.uploded_file = file

            filename = file.name
            if filename and filename.rsplit('.',1)[1].lower() in ['pdf','docx']:
                data.uploded_file = file
            else:
                messages.error(request,'upload pdf format')
                return redirect('manage-study-material') 

            

        if  not request.FILES.get('material-photo',False):
            data.title= title
            data.subject_name= subject
            # data.uploded_file = photo1
 
        if request.FILES.get('material-photo',False):
            photo2 = request.FILES['material-photo']
            data.title= title
            data.subject_name= subject
            data.uplode_photo = photo2
            images = photo2.name
            if images and images.rsplit('.',1)[1].lower() in ['jpg','jpeg','png','gif']:
               data.upload_image =photo2
            else:
                messages.error(request,'upload valid image format')
                return redirect('manage-study-material')  
            
        
        data.save()
        messages.success(request, 'material edited successfully')
        return redirect('manage-study-material')

    else:     
        return render(request, 'admin/edit-material.html', {'material':material})

def delete(request,id):
   material= UpscStudyMaterial.objects.get(material_id=id)
   material.delete()
   messages.success(request, 'Material deleted successfully')
   return redirect('manage-study-material')

def add_interview_videos(request):
    
    if request.method == 'POST' :
        
        if not request.POST.get('title'):
            messages.info(request,"Please add the title")
            return redirect('add-interview-videos')
        title = request.POST.get('title')

        if not request.POST.get('subject_name'):
            messages.info(request,"Please add the subject name")
            return redirect('add-interview-videos')  
        subject = request.POST.get('subject_name')
        
        if not request.POST.get('video_link') and not request.FILES.get('upload_video',False):
            messages.warning(request,' upload video or  video link')
            return redirect('add-interview-videos')
        video_link = request.POST.get('video_link')

        if not request.FILES.get('upload_Image',False):
            messages.info(request,"Please upload Image")
            return redirect('add-interview-videos')  
        image = request.FILES.get('upload_Image')

        if request.FILES.get('upload_Image',False):
            image = request.FILES['upload_Image']
           
            images = image.name
            if images and images.rsplit('.',1)[1].lower() in ['jpg','jpeg','png','gif']:
                if request.POST.get('video_link') and not request.FILES.get('upload_video',False) :
                    print('wdfbv')
                    video_link = request.POST.get('video_link')
                    link = str(video_link)
                    url = link.replace('https://www.youtube.com/watch?v=','https://youtube.com/embed/')
                   
                    UpscInterviewVideos.objects.create(video_title=title, subject_name=subject, videos_image=image,video_link=url)

                if not request.POST.get('video_link') and request.FILES.get('upload_video',False):
                    print('wdfbv')
                    upload_video = request.FILES['upload_video']
              
                    UpscInterviewVideos.objects.create(video_title=title, subject_name=subject, videos_image=image,uplode_video=upload_video)
                messages.success(request,'video add successfully')
                return redirect('add-interview-videos')
            else:
                messages.info(request, 'image format not correct')
                return redirect('add-interview-videos')
                  
    else:
        return render(request, 'admin/add-interview-videos.html')

def manage_interview_videos(request):
    all_videos = UpscInterviewVideos.objects.all().order_by('-video_id')

    paginater = Paginator(all_videos, 3)
    page_number = request.GET.get('page')
    page = paginater.get_page(page_number)

    return render(request, 'admin/manage-interview-videos.html', {'all_videos':page})


def edit_videos(request,id):
    videos = UpscInterviewVideos.objects.get(video_id=id)
    data = get_object_or_404(UpscInterviewVideos,video_id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        subject = request.POST.get('subject_name')
        # upload_video = request.FILES['upload_video']
       
        video_link = request.POST.get('video_link')
        link = str(video_link)
        url = link.replace('https://www.youtube.com/watch?v=','https://youtube.com/embed/')

        if not request.FILES.get('upload_video',False):
            data.video_title = title
            data.subject_name = subject
            data.video_link = url

        if request.FILES.get('upload_video',False):
            upload_video = request.FILES['upload_video']
            data.video_title = title
            data.subject_name = subject
            print('vijay video')
            

            videoformat = upload_video.name
            if videoformat and videoformat.rsplit('.',1)[1].lower() in ['mp4']:
                data.uplode_video = upload_video
               
            else:
                messages.error(request, 'upload valid video format')
                return redirect('manage-interview-videos')

        if request.FILES.get('upload_Image',False):
            image = request.FILES['upload_Image']
            data.video_title= title
            data.subject_name = subject
            # data.video_link = video_link
            print('image1233456')
            images = image.name
            if images and images.rsplit('.',1)[1].lower() in ['jpg','jpeg','png','gif']:
                data.videos_image =image
              
            else:
                messages.info(request, 'image format not correct')
                return redirect('manage-interview-videos')

        data.save()
        messages.success(request, 'video details edited successfully')
        return redirect('manage-interview-videos')
    return render(request,'admin/edit-videos.html',{'videos':videos})

def delete_videos(request,id):
    videos = UpscInterviewVideos.objects.get(video_id=id)
    videos.delete()
    messages.success(request, 'video deleted successfully')
    return redirect('manage-interview-videos')


def add_mock_test(request):
    if request.method == "POST":
        title = request.POST.get('title')
        subject_name = request.POST.get('Subject_name')
        uplode_file = request.FILES['files']

        if not request.FILES.get('image',False):
            messages.info(request,"Please upload Image")
            return redirect('add-mock-test')  
        image = request.FILES['image']
        
        
        image = request.FILES['image']
        images = image.name
        filename = uplode_file.name
        if filename and filename.rsplit('.',1)[1].lower() in ['pdf','docx'] and(images and images.rsplit('.',1)[1].lower() in ['jpg','jpeg','png','gif']):
            
            UpscMockTest.objects.create(mock_test_title=title,mock_subject_name=subject_name,uploded_file=uplode_file, upload_image=image)
            messages.success(request, 'Material has been added successfully')
            return redirect('add-mock-test')
        else:
            messages.error(request,'upload material in pdf format')
            return redirect('add-mock-test')

    return render(request, 'admin/add-mock-test.html')

def manage_mock_test(request):
    mock_test = UpscMockTest.objects.all().order_by('-mock_test_id')

    paginater = Paginator(mock_test, 3)
    page_number = request.GET.get('page')
    page = paginater.get_page(page_number)
    
    return render(request, 'admin/manage-mock-test.html',{'mock_test':page})


def edit_mock_test(request,id):
    mock = UpscMockTest.objects.get(mock_test_id=id)
    edit_data = UpscMockTest.objects.get(mock_test_id=id)


    if request.method == 'POST':
        # print('mock')
        title = request.POST.get('title')
        subject = request.POST.get('Subject_name')
        # file = request.FILES['files']
        
        if not request.FILES.get('files', False):
            # print('first')
            edit_data.mock_test_title = title
            edit_data.mock_subject_name= subject


        if request.FILES.get('files',False):
            # print('third')
            
            file = request.FILES['files']
            edit_data.mock_test_title = title
            edit_data.mock_subject_name= subject
        
            filename = file.name
            if filename and filename.rsplit('.',1)[1].lower() in ['pdf','docx']:
                edit_data.uploded_file = file
                        
            else:
                messages.error(request,'upload material in pdf format')
                return redirect('manage-mock-test')

        if not request.FILES.get('image',False):
            edit_data.mock_test_title = title
            edit_data.mock_subject_name= subject

        if request.FILES.get('image',False):
            edit_data.mock_test_title = title
            edit_data.mock_subject_name= subject
            image = request.FILES['image']
            
            images = image.name
            if images and images.rsplit('.',1)[1].lower() in ['jpg','jpeg','png','gif']:
               edit_data.upload_image =image
            else:
                messages.error(request,'upload valid image format')
                return redirect('manage-mock-test')  

            # edit_data.save(update_fields=['mock_test_title','mock_subject_name', 'uploded_file'])
        edit_data.save()
        messages.success(request, 'mock paper edited successfully')
        return redirect('manage-mock-test')
    else:
        return render(request,'admin/edit-mock.html',{'edit_mock':mock})

def delete_mock_test(request,id):
    test = UpscMockTest.objects.get(mock_test_id=id)
    test.delete()
    messages.success(request, 'mock paper deleted successfully')
    return redirect('manage-mock-test')

def sentiment_analysis(request):
    feedback = AspirantFeadbackModel.objects.all().order_by('-feadback_id')

    paginater = Paginator(feedback, 3)
    page_number = request.GET.get('page')
    page = paginater.get_page(page_number)

    return render(request, 'admin/sentiment-analysis.html',{'feedback':page})

def sentiment_analysis_graph(request):
    very_positive = AspirantFeadbackModel.objects.filter(feedback_sentiment="very Positive").count()
    positive = AspirantFeadbackModel.objects.filter(feedback_sentiment="Positive").count()
    very_negetive = AspirantFeadbackModel.objects.filter(feedback_sentiment="very Negative").count()
    negetive = AspirantFeadbackModel.objects.filter(feedback_sentiment="Negative").count()
    neutral = AspirantFeadbackModel.objects.filter(feedback_sentiment="Neutral").count()
    print(very_positive,negetive)

    context = {
        'very_positive':very_positive,
        'positive' : positive,
        'very_negetive' : very_negetive,
        'negetive' : negetive,
        'neutral' : neutral,
    }

    return render(request, 'admin/sentiment-graph.html', context)


# search aspirants
def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        
        if query:
            persions = AspirantsModel.objects.filter(full_Name__icontains=query)
            return render(request,'admin/all-aspirants.html',{'aspirants':persions})
        else:
            messages.info(request, 'No information regaurding this name !!')
            return render(request,'admin/all-aspirants.html')


# searching  study materials 
def material_details(request):
    
    if request.method == 'GET':
        material = request.GET.get('material')
        if material:
            material_details = UpscStudyMaterial.objects.filter(title__icontains=material)
            return render(request,'admin/manage-study-material.html',{'all_materials':material_details})
        else:
            messages.info(request,'Materiala Not found')
            return render(request,'admin/manage-study-material.html')
        
    
# search videos
def videos_details(request):
    if request.method == 'GET':
        video = request.GET.get('video')
        if video:
            videos = UpscInterviewVideos.objects.filter(video_title__icontains=video)
            return render(request,'admin/manage-interview-videos.html',{'all_videos':videos})
        else:
            messages.info(request,'Video Not found')
            return render(request,'admin/manage-interview-videos.html')


# search mock papers
def mock_details(request):
    if request.method == "GET":
        mock = request.GET.get('mock')

        if mock:
            test_paper = UpscMockTest.objects.filter(mock_test_title__icontains=mock)
            return render(request,'admin/manage-mock-test.html', {'mock_test':test_paper})

        else:
            messages.info(request,'Mock test paper not found')
            return render(request,'admin/manage-mock-test.html')


# admin log out
def admin_logout(request):
    messages.success(request,'Admin log out successfully return to home page')
    return redirect('home')
