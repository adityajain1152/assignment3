from django.views import generic
from .models import Machine
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
class IndexView(generic.ListView):
 
    template_name = 'inventory/index.html'
    queryset= Machine.objects.all()
    context_object_name='all_machines'
    

@method_decorator(login_required(login_url='/logout/'), name='dispatch')
class MachineCreate(CreateView):
  
    model = Machine
    fields = ['Name','Description','Availability','Price']

@method_decorator(login_required(login_url='/logout/'), name='dispatch')
class MachineUpdate(UpdateView):
  
    model = Machine
    fields = ['Name','Description','Availability','Price']


@method_decorator(login_required(login_url='/logout/'), name='dispatch')
class MachineDelete(DeleteView):

    model = Machine
    success_url = reverse_lazy('index')
    template_name='inventory/delete_template.html'


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = RegistrationForm()
		if request.method == 'POST':
			form = RegistrationForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'inventory/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username/Password is incorrect')

		context = {}
		return render(request, 'inventory/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')



class RegisterFormView(View):
    form_class = RegistrationForm
    template_name = 'inventory/register.html'
    
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

        else:
            return render(request,'inventory/register.html',{'form':self.form_class})
