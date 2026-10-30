from django.shortcuts import render,redirect,get_object_or_404
from userapp.models import *
from django.conf import settings
from django.contrib import messages
# Create your views here.
from django.contrib import messages
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

def user_registration(request):
    if request.method == "POST" and request.FILES['myfile']:
        user_name=request.POST['name']
        user_email=request.POST['email']
        user_number=request.POST['phone']
        user_password=request.POST['password']
        user_photo=request.FILES['myfile']
        print(user_email)
        try:
            UserDetailsModel.objects.get(user_email=user_email)
            messages.error(request, "User Email Already Exit.")
            return redirect('user_registration')
        except:
            UserDetailsModel.objects.create(user_name=user_name, user_email=user_email, user_number=user_number,
                                             user_password=user_password, user_pic=user_photo)
            messages.info(request, "Registration Successfully.")
            return redirect('user_login')
    else:
        return render(request, 'main/user-registration.html')

def user_login(request):
    if request.method=="POST":
        email=request.POST["email"]
        password= request.POST["password"] 
        try: 
            user = UserDetailsModel.objects.get(user_email=email, user_password=password)
            if user.user_status == 'Active':
                request.session['user_id'] = user.user_id
                messages.info(request, "Login Successfull.")
                return redirect("user_dashboard")   
            else:
                messages.error(request,'User Authorization pending') 
                return redirect("user_login")    
        except:
            print('error')
            messages.error(request,"Invalid EmailID or Password")
    return render(request, 'main/user-login.html')

def user_dashboard(request):
    user = request.session['user_id']
    profile = UserDetailsModel.objects.get(user_id=user)
    d = MedibotviewedModel.objects.filter(user=profile).count
    # e =d.viewed.count()
    a = UserDetailsModel.objects.all().count()
    b = FeedbackModel.objects.all().count()
   
    return render(request, 'user/user-dashboard.html',{'profile':profile,'a':a,'b':b,'e':d})

def user_myprofile(request):
    user = request.session['user_id']
    profile = UserDetailsModel.objects.get(user_id=user)
    obj = get_object_or_404(UserDetailsModel, user_id=user)
    if request.method == 'POST':
        user_name=request.POST['name']
        user_email=request.POST['email']
        user_number=request.POST['phonenumber']
        user_password=request.POST['password']
        # user_password = request.POST['password']
       
        if not request.FILES.get("uplaodpicture",False):
            # print("yes efffeg jfkdftjhkt")
            obj.user_name=user_name
            obj.user_email=user_email
            obj.user_number=user_number
            obj.user_password=user_password
            obj.save(update_fields=['user_name', 'user_email', 'user_number',
                                     'user_password'])
            obj.save()
             
        elif request.FILES.get("uplaodpicture",False):
            user_pic = request.FILES['uplaodpicture']
            obj.user_name=user_name
            obj.user_email=user_email
            obj.user_number=user_number
            obj.user_password=user_password
            obj.user_pic = user_pic
            obj.save(update_fields=['user_name', 'user_email', 'user_number',
                                         'user_password', 'user_pic'])
            obj.save()
           
           
        messages.info(request, 'Profile Updated Successfully.')       
        return redirect(user_myprofile)
    else:
    # return render(request, 'user/user-myprofile.html',{'i':j})
        return render(request, 'user/user-myprofile.html',{'user':profile})

def user_feedback(request):
    user_id = request.session["user_id"]
    user = UserDetailsModel.objects.get(user_id=user_id)
    if request.method =="POST":
        if not request.POST.get('a'):
            messages.error(request, "Feeback not Sent Please give the star Rating")
            return redirect('user_feedback')
            
        star = request.POST.get('a')
        comment = request.POST.get('comment')
        # text analysis
        analysis = TextBlob(comment,analyzer=NaiveBayesAnalyzer())
        print(analysis.sentiment)
        
        sentiment = ''
        if analysis.polarity >= 0.5:
            sentiment = 'Very Positive'
        elif analysis.polarity > 0 and analysis.polarity < 0.5:
            sentiment = 'Positive'
        elif analysis.polarity < 0 and analysis.polarity >= -0.5:
            sentiment = 'Negitive'
        elif analysis.polarity <= -0.5:
            sentiment = 'Very Negitive'
        else:
            sentiment = 'Neutral'
            
        FeedbackModel.objects.create(comment=comment,rating=star,sentiment=sentiment,user=user)
        messages.info(request,"Feedback Sent Successfully")
        return redirect(user_feedback)
    else:
        return render(request, 'user/user-feedback.html')

def user_medibot(request):
    return render(request, 'user/user-medibot.html')

def user_logout(request):
    return redirect('index')

def viewed(request):
    user_id = request.session["user_id"]
    user = UserDetailsModel.objects.get(user_id=user_id)
    try:
        MedibotviewedModel.objects.create(user=user)
        # a.viewed+=1
        # a.save()
        # return render(request, 'user/user-medibot.html')
    except:
        print('')
        
    return redirect('user_medibot')