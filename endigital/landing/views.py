from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from landing.models import UserDetails, HomePageContent, Blogs, ServicesOfferedContent1, ServicesOfferedContent2, ServicesDetail
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    homepage = HomePageContent.objects.all()
    services_off_content1 = ServicesOfferedContent1.objects.all()
    services_off_content2 = ServicesOfferedContent2.objects.all()
    context = {
        'home': homepage,
        'services_off_content1': services_off_content1,
        'services_off_content2': services_off_content2
    }
    return render(request, 'landing/home.html', context)


def about(request):
    return render(request, 'landing/about.html')


def form_req(request):

    if request.method == 'POST':

        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        phone = request.POST.get('phone', None)
        subject = request.POST.get('subject', None)
        message = request.POST.get('message', None)
        result = UserDetails.objects.create(
            name=name, email=email, phone=phone, subject=subject, message=message)

        return render(request, 'landing/thankyou.html')

    else:
        return render(request, 'landing/home.html')


def blogs(request):
    blogs = Blogs.objects.all().order_by('-id')
    context = {
        'blogs': blogs,
    }
    return render(request, 'landing/page-blog.html', context)


class BlogDetailView(DetailView):
    model = Blogs
    context_object_name = 'blog_detail'
    template_name = 'landing/page-blog-single.html'


class ServiceDetailView(DetailView):
    model = ServicesDetail
    queryset = ServicesDetail.objects.all()

    context_object_name = 'service_detail'
    template_name = 'landing/service-detail.html'

    def get_object(self):
        UserName = self.kwargs.get("name")
        return get_object_or_404(ServicesDetail, name=UserName)
