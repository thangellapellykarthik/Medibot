from django.shortcuts import render,redirect,get_object_or_404
from userapp.models import *
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
def admin_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        print(email)
        password = request.POST["password"]
        print(password)
        if email == "admin" and password == "admin" :
            messages.info(request, "Login Successfully.")
            return redirect("admin_dashboard")
            
        else:
            messages.error(request,"Invalid EmailID or Password")
            return redirect("admin_login")
    return render(request, 'main/admin-login.html') 

def admin_all_user(request):
    a = UserDetailsModel.objects.all().order_by('-user_id')
    p = Paginator(a,6)
    page_number = request.GET.get('page')
    ServiceDatafinal=p.get_page(page_number)
    return render(request, 'admin/admin-all-user.html',{'a':ServiceDatafinal})
   

def admin_dashboard(request):
    a = UserDetailsModel.objects.all().count()
    b = UserDetailsModel.objects.filter(user_status='Pending').count()
    c = FeedbackModel.objects.all().count()
    d = MedibotviewedModel.objects.all().count()
    return render(request, 'admin/admin-dashboard.html',{'a':a,'b':b,'c':c,'d':d})

def admin_interaction(request):
    a = MedibotviewedModel.objects.all().order_by('-view_id')
    p = Paginator(a,6)
    page_number = request.GET.get('page')
    ServiceDatafinal=p.get_page(page_number)
    return render(request, 'admin/admin-interaction.html',{'a':ServiceDatafinal})

def admin_pending_user(request):
    user = UserDetailsModel.objects.filter(user_status='Pending').order_by('-user_id')
    return render(request, 'admin/admin-pending-user.html',{'i':user})

def update(request,id):
    data = get_object_or_404(UserDetailsModel,user_id=id)
    data.user_status='Active'
    data.save(update_fields=['user_status'])
    data.save()
    messages.info(request,"Accepted Successfully")
    return redirect('admin_dashboard')

def reject(request,id):
    data = get_object_or_404(UserDetailsModel,user_id=id)
    data.user_status='Pending'
    data.save(update_fields=['user_status'])
    data.save()
    messages.info(request,"Rejected Successfully")
    return redirect('admin_dashboard')

def admin_sentiment_analysis(request):
    vpositive= FeedbackModel.objects.filter(sentiment='Very Positive').count()
    vnegitive = FeedbackModel.objects.filter(sentiment='Very Negitive').count()
    positive = FeedbackModel.objects.filter(sentiment='Positive').count()
    negitive = FeedbackModel.objects.filter(sentiment='Negitive').count()
    neutral = FeedbackModel.objects.filter(sentiment='Neutral').count()
    return render(request, 'admin/admin-sentiment-analysis.html',{'vpositive':vpositive,'vnegitive':vnegitive,'positive':positive,'negitive':negitive,'neutral':neutral})

def admin_user_feedback(request):
    a = FeedbackModel.objects.all().order_by('-feedback_id')
    p = Paginator(a,6)
    page_number = request.GET.get('page')
    ServiceDatafinal=p.get_page(page_number)
    return render(request, 'admin/admin-user-feedback.html',{'a':ServiceDatafinal})

def admin_logout(request):
    return redirect('index')

def search(request):
    print('hi')
    search = request.GET.get('search')
    print(search)
    # print('jj')
    a = MedibotviewedModel.objects.filter(Q(user__user_name__contains=search)|Q(user__user_email__contains=search)|Q(date__contains=search))
    return render(request, 'admin/admin-interaction.html',{'a':a})

def searcha(request):
    print('hello')
    search = request.GET.get('searcha')
    print(search)
    # print('jj')
    a = UserDetailsModel.objects.filter(Q(user_name__contains=search)|Q(user_email__contains=search)|Q(user_number__contains=search)|Q(user_status__contains=search))
    return render(request, 'admin/admin-all-user.html',{'a':a})