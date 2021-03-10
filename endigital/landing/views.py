from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView
from landing.models  import UserDetails,Services,ServicesContent,Blogs

# Create your views here.



def index(request):
    services = Services.objects.all()
    servicesContent = ServicesContent.objects.all()
    context = {
    'services': services,
    'servicesContent':servicesContent
    }
    return render(request, 'landing/home.html',context)

def about(request):
    return render(request, 'landing/about.html')

def form_req(request):
   
    if request.method == 'POST':
        
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        phone = request.POST.get('phone', None)
        subject = request.POST.get('subject', None)
        message = request.POST.get('message', None)
        result = UserDetails.objects.create(name=name,email=email,phone=phone,subject=subject,message=message)
        
        
        return render(request, 'landing/thankyou.html')

    else:
        return render(request, 'landing/home.html')

def blogs(request):
    blogs = Blogs.objects.all()
    context = {
    'blogs':blogs,
    }
    return render(request, 'landing/page-blog.html', context)

class BlogDetailView(DetailView):
        model = Blogs
        context_object_name = 'blog_detail'
        template_name = 'landing/page-blog-single.html'