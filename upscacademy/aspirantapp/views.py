from django.contrib import messages
from django.shortcuts import render,redirect

from adminapp.models import UpscInterviewVideos, UpscMockTest, UpscStudyMaterial
from .models import AspirantFeadbackModel, AspirantsModel
from textblob import TextBlob

# Create your views here.

def dashboard(request):
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
        'feedback' :feedbacks,
    }
    return render(request, 'aspirant/aspirant-index.html',context)

def aspirant_register(request):
    if request.method == "POST" and 'profile' in request.FILES:
        print('method post')
        name = request.POST.get('fullname')
        print(name)
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile_number = request.POST.get('number')
        profile = request.FILES['profile']
        education =request.POST.get('education')
        state= request.POST.get('state')
        country = request.POST.get('country')
        address = request.POST.get('address')
        pin = request.POST.get('pin')
        
        try:
            print('try')
            AspirantsModel.objects.get(Email=email)
            messages.warning(request,'Email already exists')
            return redirect('register')
        
        except:
            image = profile.name
            print('table created')
            if image and image.rsplit('.',1)[1].lower() in ['jpg','jpeg','png','gif'] :
                AspirantsModel.objects.create(
                    full_Name=name,
                    email=email,
                    password=password,
                    phone_Number=mobile_number,
                    profile=profile,
                    education = education,
                    state = state,
                    country = country,
                    address=address,
                    pin_number = pin,
                    )
                messages.success(request, "Registered successfully wait for admin action ")
                return redirect('login')
        

    else:
        
        return render(request, 'aspirant/aspirants-register.html')

def aspirant_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password'] 
        print(email)
        print(password)

    
        try:
            aspirant = AspirantsModel.objects.get(email=email,password=password)
            
            if aspirant.status == 'Accept':
                request.session['aspirant_id'] = aspirant.aspirant_id
                messages.success(request, 'logined successfully')
                return redirect('dashboard')
            else:
                messages.info(request, 'Your account is not approved yet!!')
                return redirect('login')
        except:
            messages.warning(request, 'Invalid Email and password')
            return redirect('login')
  
    return render(request,'aspirant/aspirants-login.html')


def materials(request):
    # aspirant_id = request.session['aspirant_id']
    # aspirant= AspirantsModel.objects.get(pk=aspirant_id)
    materials = UpscStudyMaterial.objects.all()
  
    return render(request,'aspirant/study-material.html', {'materials':materials})

def materials_details_page(request,id):
    details = UpscStudyMaterial.objects.get(material_id=id)
    return render(request, 'aspirant/study-material-details-page.html',{'details':details})

def videos(request):
    video = UpscInterviewVideos.objects.all().order_by('-video_id')
    return render(request,'aspirant/aspirant-upsc-videos.html',{'video':video})


def videos_details(request,id):
    videos = UpscInterviewVideos.objects.get(pk=id)
    return render(request,'aspirant/videos-details.html',{'videos':videos})

def mock(request):
    mock = UpscMockTest.objects.all()
    return render(request, 'aspirant/mock-test.html',{'mocktests':mock})
    

def mock_details(request,id):
    md = UpscMockTest.objects.get(mock_test_id=id)
    return render(request,'aspirant/mock-test-details-page.html',{'moc':md})


def feadback(request):
    aspirant_id = request.session['aspirant_id']
    aspirant= AspirantsModel.objects.get(pk=aspirant_id)
   
    if request.method=='POST':

        if not request.POST.get('a'):
            messages.info(request,"Please rate for study material")
            return redirect('feadback')
        a = request.POST.get('a')

        if not request.POST.get('b'):
            messages.info(request,"Please rate for videos")
            return redirect('feadback')
        b = request.POST.get('b')

        if not request.POST.get('c'):
            messages.info(request,"Please rate for mock")
            return redirect('feadback')
        c = request.POST.get('c')

        
        if request.POST.get('feedback'):
            messages.success(request,"Feedback submited successfully")
        feedback = request.POST.get('feedback')
           
        # feedback = request.POST.get('feedback')
        analysis = TextBlob(feedback)
        print(analysis)
        print(analysis.sentiment)
        sentiment = ""
        if analysis.polarity>=0.5:
            sentiment='very Positive'
        elif analysis.polarity > 0  and analysis.polarity < 0.5:
            sentiment='Positive'
        elif analysis.polarity < 0  and analysis.polarity > -0.5:
            sentiment='Negative' 
        elif analysis.polarity <= -0.5:
            sentiment='very Negative'       
        else:
            sentiment='Neutral'
        
        AspirantFeadbackModel.objects.create(
            feedback_message=feedback,
            feedback_sentiment=sentiment,
            rating1=a,
            rating2=b,
            rating3=c,
            aspirant=aspirant)

        print(sentiment)
    feedbacks=AspirantFeadbackModel.objects.all().order_by('-feadback_id')[0:4]
    return render(request, 'aspirant/aspirant-feadback.html',{'feedback':feedbacks})


def profile(request):
    persion_id=request.session['aspirant_id']
    persion = AspirantsModel.objects.get(pk=persion_id)
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        number = request.POST.get('number')
        education = request.POST.get('education')
        password  = request.POST.get('password')
        state = request.POST.get('state')
        country = request.POST.get('country')
        address = request.POST.get('address')
        pin = request.POST.get('pin')

        if not request.FILES.get('profile_photo',False):
            persion.full_Name=name
            persion.email=email
            persion.phone_Number=number
            persion.education=education
            persion.password=password
            persion.state=state
            persion.country=country
            persion.address=address
            persion.pin_number=pin

        elif request.FILES.get('profile_photo',False):
            photo = request.FILES['profile_photo']
            persion.full_Name=name
            persion.email=email
            persion.phone_Number=number
            persion.education=education
            persion.password=password
            persion.state=state
            persion.country=country
            persion.address=address
            persion.pin_number=pin
            persion.profile=photo

        persion.save()
        return redirect('profile')

    return render(request, 'aspirant/profile.html',{'persion':persion})

def logout(request):
    messages.success(request,'Aspirant log out successfully return to home page')
    return redirect('home')