from django.shortcuts import render, reverse

from django.views import generic

from BLOG.models import Blog_Post
from BLOG.forms import CreateBlogForm

# Create your views here.


class AboutView(generic.TemplateView):
    template_name = "test.html"



# class CreateBlog(generic.CreateView):
#     template_name = "test.html"
#     form_class = CreateBlogForm

#     def get_success_url(self):
#         return reverse("core:home")


    


class CreateBlog(generic.CreateView):
    template_name = "createBlog.html"
    form_class = CreateBlogForm


    def get_success_url(self):
        return reverse("core:home")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.AuthorName = self.request.user
        instance.save()
        self.product = instance
        return super(CreateBlog, self).form_valid(form)





class Bloglist(generic.ListView):
    template_name = "Blogdisplay.html"
    context_object_name = "blogs"

    def get_queryset(self):
        queryset = Blog_Post.objects.all()

        return queryset
