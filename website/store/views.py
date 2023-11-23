from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from .models import Product
from .form import UserForm
from django.contrib.auth import login, authenticate, logout


class List_view(View):
    templates_name = 'product_list.html'
    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        item_name = request.GET.get('item_name')
        if item_name != "" and item_name is not None:
            queryset = Product.objects.filter(name__icontains=item_name)
        return render(request, self.templates_name, {'object_list': queryset})


class Detail_view(View):
    template_name = 'product_detail.html'
    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug is not None:
            product = get_object_or_404(Product, slug=slug)
        return render(request, self.template_name, {'product': product})


class Create_user(View):
    form = UserForm
    template_name = 'create_user.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')

        return render(request, self.template_name, {'form': form})



class SignUp(View):
    template_name = 'login_user.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('product_list')
            else:
                mes = "mauvaise authentication"
                return render(request, self.template_name, {'mes': mes} )
        return render(request, self.template_name)


def signout(request):
    logout(request)
    return redirect('product_list')