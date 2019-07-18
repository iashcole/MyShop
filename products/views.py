from django.shortcuts import render, redirect
from .models import Product
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'products/index.html/'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()


class DetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html/'


class ProductCreate(generic.CreateView):
    model = Product
    fields = ['name', 'price', 'stock', 'image_url']

# class UserFormView(TemplateView):
#     form_class = UserForm
#     template_name = 'products/register.html'
#
#     # display blank form
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})
#
#     # process form data
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             user = form.save(commit=False)
#
#             # cleaned (normalized) data
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#
#             user = authenticate(username=username, password=password)\
#
#             if user is not None:
#
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('products:index')