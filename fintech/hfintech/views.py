from django.shortcuts import render,redirect,HttpResponse

from hfintech.models import UserProfile,Company, StockPrice, Investment,Transactions,BitsTransaction

from json import dumps
import random
import string

# Create your views here.


def index(request):
    '''dataDictionary = {'Passing Data': 'From Python to JS', 
    'geeks': 'forgeeks', 'ABC': 123, 456: 'abc', 
    14000605: 1, 'list': ['geeks', 4, 'geeks'], 
     }
    # dump data 
    dataJSON = dumps(dataDictionary)
    return render(request,'index.html',{'data':dataJSON})'''
    return render(request,'index.html')


def login(request):
    if request.method == 'POST':
        email_id = request.POST.get('username')
        password = request.POST.get('password')

        try:
            username = UserDetails.objects.filter(email=email_id)[0].username
        except:
            return redirect('/index')
        print('YOUR USERNAME is', username, 'YOUR PWD IS: ',password)
        user = authenticate(username = username,password = password)

        if user:
            print('user try1  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', user.get_username)
            if user.is_active:
                print('user try2 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', user)
                auth_login(request, user)
                #return HttpResponseRedirect(request.GET.get('next',settings.LOGIN_REDIRECT_URL))
                print('AUTH_SUCCESS')
                return render(request,'index.html')
        else:
            return HttpResponse("Auth Failed !")
    return render(request,'login_new.html')

def register(request):

    if request.method == 'POST':
        print('REGISTER-CALL POST_1')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        phone = request.POST.get('phone')
        

        user_id = ''.join(random.choices(string.ascii_uppercase + string.digits,k= 10))
        #password_enc = pbkdf2_sha256.hash(password,rounds = 12000,salt_size = 32)
        print('USER PASSWORD IS : ',password)
        userobject = UserProfile(username = user_id, user_id=user_id, contact_number = phone, email_id = email, bpoints_balance = 0)
        userobject.set_password(password)
        userobject.save()
        print('USER OBJECT SAVED. CHECK DB')
        return redirect('/login')
    else:
        return render(request,'register.html')
    
