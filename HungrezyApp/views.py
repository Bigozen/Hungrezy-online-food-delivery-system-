from django.shortcuts import render, redirect
from django.contrib import messages
# from django.core import validators
# from HungrezyApp.forms import customersignupform
# from HungrezyApp.models import customer
# from HungrezyApp.models import rider
from HungrezyApp.models import customer_account
from HungrezyApp.models import rider_account
from HungrezyApp.models import business_account
from django.contrib.auth.models import User



# Create your views here.

from django.shortcuts import render, HttpResponse


def home(request):
    # return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our homepage</h1>")
    return render(request, 'home.html')


def restaurants(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our restatrants page</h1>")


def menu(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our menu page</h1>")


def homemadefoodoptions(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our home made food options page</h1>")


def category(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our category page</h1>")


def aboutus(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our about us page</h1>")


def contact(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our contact info page</h1>")


def login(request):
    # return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our login page</h1>")
    
    if(request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        users = request.POST['users']
        
        user_objs = User.objects.all()
        # get_user = user_objs.get(email=email, password = password)
        get_user = user_objs.filter(email=email, password = password)
        # if user_objs.get(email=email, password = password) is Exception:
        #     get_user = user_objs.get(email=email, password = password)
        #     print(get_user)
        # if get_user:
        #     print("id", get_user[0].id)
        # else :
        #     print("GGEZ")
        # print(get_user.DoesNotExist)
        
        
        # print(get_user[0].id)
        if get_user:
            if(users == "customer"):
                cus = customer_account.objects.all()
                get_cus = cus.filter(user=get_user[0].id)
                if get_cus:
                    context = {'nametext' : get_cus[0].name}
                    # print("Successfully logged in")
                    # return render(request,'customer_login.html', context)
                    return render(request,'customer_login.html', context)

                    
                else:
                    messages.error(request, "Please select correct type")
            
            elif(users == "rider"):
                rid = rider_account.objects.all()
                get_rid = rid.filter(user=get_user[0].id)
                if get_rid:
                    # print("Successfully logged in")
                    context = {'nametext' : get_rid[0].name}
                    # return render(request,'business_login.html', context)
                else:
                    messages.error(request, "Please select correct type")
                    
            elif(users == "business"):
                bus = business_account.objects.all()
                get_bus = bus.filter(user=get_user[0].id)
                if get_bus:
                    # print("Successfully logged in")
                    context = {'nametext' : get_bus[0].name}
                    return render(request,'bussiness_login.html', context)
                else:
                    messages.error(request, "Please select correct type")
                    
            else:
                messages.error(request, "Please select your account type and try again")
        else :
            messages.error(request, 'incorrect email or password')
            
            # ValidationError(_('Invalid value'), code='invalid')

        # if(users == "customer"):
        #     # print(get_user)
        #     cus = customer_account.objects.all()
        #     get_cus = cus.get(user=get_user.id)
            
        #     print(get_cus.address)
        
        
        
    
    
    return render(request, 'login.html')


def admin(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our admin page</h1>")


def updaterestaurant(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our update restaurant page</h1>")


def updaterider(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our update rider page</h1>")


def updatecustomer(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our update customer page</h1>")


def updateriderstatus(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update rider status page</h1>")


def updateadminprifile(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update admin profile page</h1>")


def rider(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our rider page</h1>")


def updateriderprofile(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update rider profile page</h1>")


def ridersalary(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our rider salary</h1>")


def riderhistory(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our rider history page</h1>")


def restaurantowner(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our restaurant owner page</h1>")


def updateownerprofile(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update owner profile page</h1>")


def ownerupdaterestaurant(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update restaurant as owner page</h1>")


def updateprice(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our update price page</h1>")


def updatemenu(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our update menu page</h1>")


def customer(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our customer page</h1>")


def updatecustomerprofile(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update customer profile page</h1>")


def order(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our order page</h1>")


def rating(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our rating page</h1>")


def review(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our review page</h1>")


def homemadefoodsuppiler(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our homemade food supplier page</h1>")


def updatesuppilerprofile(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update supplier profile page</h1>")


def updatehomemadefoodprice(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update homemade food price page</h1>")


def updatehomemadefoodoptions(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update homemade food options page</h1>")


def signup(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our signup page</h1>")


def signupas(request):
    # return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our signup as page</h1>")
    return render(request, 'signupas.html')


def customeraccountsignup(request):
    # return HttpResponse(
    #     "<style>h1{text-align: center;}</style><h1>Welcome... This is our customer account signup page</h1>")
    
    # if(request.method == 'POST'):
    #     form = customersignupform(request.POST)
    #     form.save()
        
    # form = customersignupform()
        
    # context = {
    #     'customer_signup_form' : form
    # }
    
    if(request.method == 'POST'):
        # cus_id = request.POST['cus_id']
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        contact_no = request.POST['contact_no']
        gender = request.POST['gender']
        password = request.POST['password']
        c_password = request.POST['confirm_password']

        if password == c_password:
            userT = User(username=name, email=email, password=password)
            userT.save()
            
            userObjs = User.objects.all()
            get_user = userObjs.get(username=name)
        
        
            casu = customer_account(name=name, email=email, address=address,contact_number=contact_no, gender=gender, password=password, user = get_user)
            casu.save()
    
            return redirect ('/home')
        else:
            messages.error(request, "Check password and try again")
        
        # getU = User.objects.all().get(id=15)
        # getU.username = name
        # getU.email = email
        # getU.save()
        
        
        # getCustomer = customer_account.objects.all().get(user=15)
        # getCustomer.name = name
        # getCustomer.email = email
        # getCustomer.address = address
        # getCustomer.contact_number = contact_no
        # getCustomer.gender = gender
        # getCustomer.save()
        
        
    
    return render(request, 'customer_acc_signup.html')


def businessaccountsignup(request):
    # return HttpResponse(
    #     "<style>h1{text-align: center;}</style><h1>Welcome... This is our business account signup page</h1>")
    
    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        restaurant_name = request.POST['restaurant_name']
        service = request.POST['service']
        # food = request.POST['food']
        address = request.POST['address']
        contact_no = request.POST['contact_no']
        # gender = request.POST['gender']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if confirm_password == password:
            userT = User(username=name, email=email, password=password)
            userT.save()

            userObjs = User.objects.all()
            get_user = userObjs.get(username=name)
            
            bsu = business_account(name=name, email=email, res_name = restaurant_name, service = service, address=address, contact_no=contact_no, password=password, user=get_user)
            bsu.save()

            return redirect('/home')
        
        else:
            messages.error(request, "Check confirm password and try again")
        
    
    return render(request, 'business_acc_signup.html')


def rideraccountsignup(request):
    # return HttpResponse(
    #     "<style>h1{text-align: center;}</style><h1>Welcome... This is our rider account signup page</h1>")
    
    if(request.method == 'POST'):
        name =  request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        delivary_method = request.POST['delivary_method']
        contact_no = request.POST['contact_no']
        gender = request.POST['gender']
        password = request.POST['password']
        
        userT = User(username=name, email=email, password=password)
        userT.save()
        
        userObjs = User.objects.all()
        get_user = userObjs.get(username=name)
        
        # rsu = rider(u_name=name, email=email, address=address, delivary_method=delivary_method, gender=gender, contact_number=contact_no, password=password, user=get_user)
        # rsu.save()
        
        rasu = rider_account(user_name = name, email = email, address = address, delivary_method = delivary_method, gender = gender, contact_number = contact_no, password = password, user = get_user)
        rasu.save()
        
        
    return render(request, 'rider_acc_signup.html')

def customerupdateinfo(request):
    
    if(request.method == 'POST'):
        name = request.POST['name']
        address = request.POST['address']
        contact_no = request.POST['contact_no']
        new_pass = request.POST['new_pass']
        c_new_pass = request.POST['c_new_pass']
        password = request.POST['password']
        
        user_objs = customer_account.objects.all()
        get_user = user_objs.filter(name=name)
        
        if get_user:
            get_pass = get_user[0].password
            
            if get_pass == password:
                
                if address: 
                    get_user[0].address = address
                if contact_no:
                    get_user[0].contact_number = contact_no
                if new_pass:
                    if new_pass == c_new_pass:
                        get_user[0].password = new_pass
                    else:
                        messages.error(request, "Check new password and try again")
                
                get_user[0].save()
                messages.error(request, "Successfully updated!")
                
            else:
                # print("wrong password")
                messages.error(request, "Wrong password")
            
        else:
            # print("Check your username")
            messages.error(request, "Please check your usernmane and try again")
            
    return render(request, 'customer_update_info.html')


def businessaccinfoupdate(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        address = request.POST['address']
        restu_name = request.POST['restaurant_name']
        contact_no = request.POST['contact_no']
        new_pass = request.POST['new_pass']
        c_new_pass = request.POST['c_new_pass']
        password = request.POST['password']
        
        user_objs = business_account.objects.all()
        get_user = user_objs.filter(name=name)
        
        if get_user:
            get_pass = get_user[0].password
            
            if get_pass == password:
                
                if address: 
                    get_user[0].address = address
                if contact_no:
                    get_user[0].contact_no = contact_no
                if restu_name:
                    get_user[0].res_name = restu_name
                
                if new_pass:
                    if new_pass == c_new_pass:
                        get_user[0].password = new_pass
                    else:
                        messages.error(request, "Check new password nad try again")
                
                get_user[0].save()
                messages.error(request, "Successfully updated!")
            else:
                # print("wrong password")
                messages.error(request, "Wrong password")
            
        else:
            # print("Check your username")
            messages.error(request, "Please check your usernmane and try again")
            
    return render(request, 'Business_acc_update_info.html')


def rideraccountinfoupdate(request):
    
    if(request.method == 'POST'):
        name = request.POST['name']
        address = request.POST['address']
        contact_no = request.POST['contact_no']
        delivary = request.POST['delivary_method']
        password = request.POST['password']
        
        user_objs = rider_account.objects.all()
        get_user = user_objs.filter(user_name=name)
        
        if get_user:
            get_pass = get_user[0].password
            
            if get_pass == password:
                
                if address: 
                    get_user[0].address = address
                if contact_no:
                    get_user[0].contact_number = contact_no
                if delivary:
                    get_user[0].delivary_method = delivary
                
                get_user[0].save()
                
            else:
                # print("wrong password")
                messages.error(request, "Wrong password")
            
        else:
            # print("Check your username")
            messages.error(request, "Please check your usernmane and try again")
            
    return render(request, 'rider_update_info.html')

def customerlogin(request):
    
    return render(request, 'customer_login.html')


def menucart(request):
    return render(request, 'menucart.html')