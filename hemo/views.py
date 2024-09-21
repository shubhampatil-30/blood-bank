from django.shortcuts import render,redirect,get_object_or_404
from .models import user,donor,bank,blooddonate,recipient,bloodrequest,hospital,stock,cart,order,payment,orderdetail
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from django.db.models import Sum,Q
from datetime import date
from django.conf import settings
import razorpay


# Create your views here.
# class homeview(ListView):
#     model = blooddonate
#     template_name = 'home.html'
#     context_object_name = "dobj"

def homeviews(request):
    bobj=donor.objects.all()
    dobj=blooddonate.objects.values('donorid').distinct()
    list1 = list(dobj)
    print(list1[0])
    list2 = list()
    for i in list1:
        print(i)
        for j in i:
            list2.append(i[j])
            print(i[j])
    ddobj = donor.objects.filter(id__in=list2)
    print(ddobj)
    # doobj=donor.objects.all()
  
    return render(request,'carousel.html',{'dobj':ddobj})


def login(request):
    if request.method =='GET':
        return render(request,'login.html')
    elif request.method == 'POST': 
        uname = request.POST.get('uname')
        password=request.POST.get('pwd')

        userobj=user.objects.filter(name=uname)
        if userobj:
            uobj = user.objects.get(name=uname)
            flag=check_password(password,uobj.password)
            if flag:
                request.session['sessionvalue']=uobj.name
                return redirect('../home')
            else:
                return render(request,'login.html',{'msg':'Incorrect Username or Password'})
        else:
            return render(request,'login.html',{'msg':'Incorrect Username or Password'})

def register(request):
    if request.method=="GET":
        return render(request,'register.html')
    elif request.method=="POST":
        name=request.POST.get('fullname')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        phoneno=request.POST.get('phoneno')
        address=request.POST.get('address')
        state=request.POST.get('state')
        district=request.POST.get('district')
        pincode=request.POST.get('pincode')
        email=request.POST.get('email')
        password=request.POST.get('password')
        epassword= make_password(password)
        userobj=user(name=name,age=age,gender=gender,phoneno=phoneno,address=address,state=state,district=district,pincode=pincode,email=email,password=epassword)
        userobj.save()
        return redirect('../login')
    

def donor_register(request):
    if request.method=="GET":
        return render(request,'donor.html')
    elif request.method=="POST":
        dname=request.POST.get('donorname')
        image=request.FILES.get('donorimg')
        
        gender=request.POST.get('gender')
        bloodgroup=request.POST.get('bloodgroup')
        address=request.POST.get('address')
        phoneno=request.POST.get('phoneno')
        state=request.POST.get('state')
        age=request.POST.get('age')
        city=request.POST.get('city')
        password=request.POST.get('password')
        epassword= make_password(password)


        donorobj=donor(name=dname,img=image,age=age,gender=gender,bloodgroup=bloodgroup,address=address,phoneno=phoneno,state=state,city=city,password=epassword)
        donorobj.save()
        return redirect('../donor_login')
    
def donor_login(request):
    if request.method =='GET':
        return render(request,'donor_login.html')
    elif request.method == 'POST':
        dname = request.POST.get('dname')
        password=request.POST.get('dpassword')

        donorobj=donor.objects.filter(name=dname)
        if donorobj:
            dobj = donor.objects.get(name=dname)
            flag=check_password(password,dobj.password)
            if flag:
                request.session['donorsession']=dobj.name
                return redirect('../donorhome')
            else:
                return render(request,'donor_login.html',{'msg':'Incorrect Username or Password'})
        else:
            return render(request,'donor_login.html',{'msg':'Incorrect Username or Password'})
    

def bank_register(request):
        if request.method=='GET':
           return render(request, 'bloodbank.html')
        elif request.method=="POST":
            name=request.POST.get('uname')
            phoneno=request.POST.get('number')
            address=request.POST.get('address')
            state=request.POST.get('state')
            city=request.POST.get('city')
            username=request.POST.get('bankuser')
            password=request.POST.get('password')
            epassword=make_password(password)
            

            bankobj=bank(name=name,phoneno=phoneno,address=address,state=state,city=city,username=username,password=epassword)
            bankobj.save()
            return redirect('../bank_login')
        
def bank_login(request):
    if request.method =='GET':
        return render(request,'bank_login.html')
    elif request.method == 'POST':
        bname = request.POST.get('bname')
        password=request.POST.get('bpassword')

        bankobj=bank.objects.filter(username=bname)
        if bankobj:
            bobj = bank.objects.get(username=bname)
            flag=check_password(password,bobj.password)
            if flag:
                request.session['banksession']=bobj.username
                return redirect('../bankhome')
            else:
                return render(request,'bank_login.html',{'msg':'Incorrect Username or Password'})
        else:
            return render(request,'bank_login.html',{'msg':'Incorrect Username or Password'})
    
# def donordashboard(request):
#     return render(request,'donor_dashboard.html')

def donorhome(request):
    # did = request.POST.get('did')
    dsession=request.session['donorsession']
    dobj=donor.objects.get(name=dsession)
    d1={
        'requestmade': blooddonate.objects.filter(donorid=dobj).count(),
        'pendingrequest': blooddonate.objects.filter(donorid=dobj,status='Pending').count(),
        'approverequest': blooddonate.objects.filter(donorid=dobj,status='Approved').count(),
        'rejectedrequest': blooddonate.objects.filter(donorid=dobj,status='Rejected').count()
        }
    return render(request,'donorhome.html',{'dobj':d1,'session':dsession})

def donate(request,pk):
    if request.method=="GET":
        return render(request,'donate.html')
    
    elif request.method=="POST":
        dsession=request.session['donorsession']
        if dsession:
            dobj=donor.objects.get(name=dsession)
            
        bankid=bank.objects.get(id=pk)
        age=request.POST.get('age')
        disease=request.POST.get('disease')
        unit=request.POST.get('unit')
        donateobj=blooddonate(donorid=dobj,bankid=bankid,age=age,disease=disease,unit=unit,status='pending')
        donateobj.save()
        
        return redirect('../donorhome',{'session':dsession})
        # return render(request,'donorhome.html',{'session':dsession})

def donorhistory(request):
    dsession=request.session['donorsession']
    if dsession:
        dobj=donor.objects.get(name=dsession)
        bobj=blooddonate.objects.filter(donorid=dobj)    
        return render(request,'donorhistory.html',{'dobj':bobj,'session':dsession})


# def donorrequest(request):
#     return render(request,'donorrequest.html')

# def requesthistory(request):
#     return render(request,'requesthistory.html')

def recipient_register(request):
    if request.method=="GET":
        return render(request,'recipientregistration.html')
    elif request.method=="POST":
        rname=request.POST.get('rname')
        image=request.FILES.get('rimg')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        bloodgroup=request.POST.get('bloodgroup')
        address=request.POST.get('address')
        phoneno=request.POST.get('phoneno')
        state=request.POST.get('state')
        city=request.POST.get('city')
        password=request.POST.get('password')
        epassword= make_password(password)

        recipientobj=recipient(name=rname,img=image,age=age,gender=gender,bloodgroup=bloodgroup,address=address,phoneno=phoneno,state=state,city=city,password=epassword)
        recipientobj.save()
        return redirect('../recipient_login')

def recipient_login(request):
    if request.method =='GET':
        return render(request,'recipient_login.html')
    elif request.method == 'POST':
        rname = request.POST.get('rname')
        password=request.POST.get('rpassword')

        resobj=recipient.objects.filter(name=rname)
        if resobj:
            robj = recipient.objects.get(name=rname)
            flag=check_password(password,robj.password)
            if flag:
                request.session['recipientsession']=robj.name
                return redirect('../recipienthome')
            else:
                return render(request,'recipient_login.html',{'msg':'Incorrect Username or Password'})
        else:
            return render(request,'recipient_login.html',{'msg':'Incorrect Username or Password'})

def recipienthome(request):
    rsession=request.session['recipientsession']
    robj=recipient.objects.get(name=rsession)
    d1={
        'requestmade': bloodrequest.objects.filter(recipientid=robj).count(),
        'pendingrequest': bloodrequest.objects.filter(recipientid=robj,status='Pending').count(),
        'approverequest': bloodrequest.objects.filter(recipientid=robj,status='Approved').count(),
        'rejectedrequest': bloodrequest.objects.filter(recipientid=robj,status='Rejected').count()
        }
    return render(request,'recipienthome.html',{'robj':d1})

def recipientrequest(request,pk):
    if request.method=="GET":
        return render(request,'recipientrequest.html')
    
    elif request.method=="POST":
        rsession=request.session['recipientsession']
        if rsession:
            robj=recipient.objects.get(name=rsession)
            
        bankid=bank.objects.get(id=pk)
        age=request.POST.get('age')
        reason=request.POST.get('reason')
        unit=request.POST.get('unit')
        requestobj=bloodrequest(recipientid=robj,bankid=bankid,age=age,reason=reason,unit=unit,status='pending')
        requestobj.save()
        return redirect('../recipienthome')

def recipienthistory(request):
    rsession=request.session['recipientsession']
    if rsession:
        robj=recipient.objects.get(name=rsession)
        bobj=bloodrequest.objects.filter(recipientid=robj)
        return render(request,'recipienthistory.html',{'robj':bobj})

# def adminhome(request):
#     return render(request,'adminhome.html')

# def admindonor(request):
#     doobj=donor.objects.all()
#     return render(request,'admindonor.html',{'doobj':doobj})

# def admindonation(request):
#     dobj=blooddonate.objects.all()    
#     return render(request,'admindonation.html',{'dobj':dobj})

def donor_approvr_status(request,pk):
    req=blooddonate.objects.get(id=pk)
    donation_blood_group=req.donorid.bloodgroup
    donation_blood_unit=req.unit

    bstock=stock.objects.get(bloodgroup=donation_blood_group)
    bstock.unit=bstock.unit+donation_blood_unit
    bstock.save()

    req.status="Approved"
    req.save()
    return redirect('../bankhome')

def donor_reject_status(request,pk):
    req=blooddonate.objects.get(id=pk)
    req.status="Rejected"
    req.save()
    return redirect('../bankhome')

def delete_donor(request,pk):
    donorobj=blooddonate.objects.get(donorid=pk)
    donorobj.delete()
    return redirect('../bankhome')

def recipient_approvr_status(request,pk):
    req=bloodrequest.objects.get(id=pk)

    message=None
    bloodgroup=req.recipientid.bloodgroup
    unit=req.unit
    rstock=stock.objects.get(bloodgroup=bloodgroup)
    if rstock.unit > unit:
        rstock.unit=rstock.unit-unit
        rstock.save()
        req.status="Approved"
        
    else:
        message="Stock Doest Not Have Enough Blood To Approve This Request, Only "+str(rstock.unit)+" Unit Available"

    req.save()
    requests=bloodrequest.objects.all()
    return render(request,'bankrequest.html',{'robj':requests,'message':message})

def recipient_reject_status(request,pk):
    req=bloodrequest.objects.get(id=pk)
    req.status="Rejected"
    req.save()
    return redirect('../bankhome')

def delete_recipient(request,pk):
    donorobj=recipient.objects.get(id=pk)
    donorobj.delete()
    return redirect('../bankhome')

def bankhome(request):
    dsession = request.session.get('banksession')
    
    if dsession:
        try:
            dobj = bank.objects.get(username=dsession)
        except bank.DoesNotExist:
            # Handle case where bank does not exist
            return render(request, 'bankhome.html', context={ 'error': 'Bank not found' })
        
        totalunit = stock.objects.filter(bankid=dobj).aggregate(Sum('unit'))
        total_units = totalunit['unit__sum'] or 0

        context = {
            'totaldonors': blooddonate.objects.filter(bankid=dobj).count(),
            'totalbloodunit': total_units,
            'totalrequest': blooddonate.objects.filter(bankid=dobj).count(),
            'totalapprovedrequest': blooddonate.objects.filter(bankid=dobj, status='Approved').count()
        }

        bloodgroups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        for bg in bloodgroups:
            context[bg.replace("+", "1").replace("-", "2")] = stock.objects.filter(bankid=dobj, bloodgroup=bg).first()
    else:
        context = { 'error': 'Session not found' }
    
    # rsession=request.session['banksession']
    # robj=bank.objects.get(username=rsession)
    # totalunit=stock.objects.aggregate(Sum('unit'))
    # dict={

    #     'A1':stock.objects.get(bankid=robj.id,bloodgroup='A+'),
    #     'A2':stock.objects.get(bankid=robj.id,bloodgroup="A-"),
    #     'B1':stock.objects.get(bankid=robj.id,bloodgroup="B+"),
    #     'B2':stock.objects.get(bankid=robj.id,bloodgroup="B-"),
    #     'AB1':stock.objects.get(bankid=robj.id,bloodgroup="AB+"),
    #     'AB2':stock.objects.get(bankid=robj.id,bloodgroup="AB-"),
    #     'O1':stock.objects.get(bankid=robj.id,bloodgroup="O+"),
    #     'O2':stock.objects.get(bankid=robj.id,bloodgroup="O-"),
    #     'totaldonors':donor.objects.all().count(),
    #     'totalbloodunit':totalunit['unit__sum'],
    #     'totalrequest':blooddonate.objects.all().count(),
    #     'totalapprovedrequest':blooddonate.objects.all().filter(status='Approved').count()
    # }

    return render(request,'bankhome.html',context=context)
    # return render(request,'bankhome.html')

def bankdonation(request):
    bsession=request.session['banksession']
    bobj=bank.objects.get(username=bsession)
    dobj=blooddonate.objects.filter(bankid=bobj.id)
    return render(request,'bankdonation.html',{'dobj':dobj})

def bankrequest(request):
    bsession=request.session['banksession']
    bobj=bank.objects.get(username=bsession)
    robj=bloodrequest.objects.filter(bankid=bobj.id)
    return render(request,'bankrequest.html',{'robj':robj})

def bankdonor(request):
    bsession=request.session['banksession']
    bobj=bank.objects.get(username=bsession)
    dobj=blooddonate.objects.filter(bankid=bobj).values('donorid').distinct()
    list1 = list(dobj)
    print(list1[0])
    list2 = list()
    for i in list1:
        print(i)
        for j in i:
            list2.append(i[j])
            print(i[j])
    ddobj = donor.objects.filter(id__in=list2)
    print(ddobj)
    # doobj=donor.objects.all()
  
    return render(request,'bankdonor.html',{'dobj':ddobj})

def bankrecipient(request):
    bsession=request.session['banksession']
    bobj=bank.objects.get(username=bsession)
    dobj=bloodrequest.objects.filter(bankid=bobj).values('recipientid').distinct()
    list1 = list(dobj)
    print(list1[0])
    list2 = list()
    for i in list1:
        print(i)
        for j in i:
            list2.append(i[j])
            print(i[j])
    ddobj = recipient.objects.filter(id__in=list2)
    print(ddobj)

    return render(request,'bankrecipient.html',{'dobj':ddobj})

def banklist(request):
    bobj=bank.objects.all()
    return render(request,'banklist.html',{'bobj':bobj})

def recipientbanklist(request):
    rbobj=bank.objects.all()
    return render(request,'recipientbanklist.html',{'rbobj':rbobj})

def hospitalbanklist(request):
    rbobj=bank.objects.all()
    return render(request,'hospitalbanklist.html',{'rbobj':rbobj})



def hospitaldash(request):
    return render(request,'hospital_dash.html')

def hospitalhome(request):
    return render(request,'hospitalhome.html')

def hospital_register(request):
        if request.method=='GET':
           return render(request, 'hospitalregister.html')
        elif request.method=="POST":
            name=request.POST.get('uname')
            phoneno=request.POST.get('number')
            address=request.POST.get('address')
            state=request.POST.get('state')
            city=request.POST.get('city')
            username=request.POST.get('bankuser')
            password=request.POST.get('password')
            epassword=make_password(password)
            

            hosobj=hospital(name=name,phoneno=phoneno,address=address,state=state,city=city,username=username,password=epassword)
            hosobj.save()
            return redirect('../hospital_login')
        
def hospital_login(request):
    if request.method =='GET':
        return render(request,'hospital_login.html')
    elif request.method == 'POST':
        bname = request.POST.get('bname')
        password=request.POST.get('bpassword')

        bankobj=hospital.objects.filter(username=bname)
        if bankobj:
            bobj = hospital.objects.get(username=bname)
            flag=check_password(password,bobj.password)
            if flag:
                request.session['hospitalsession']=bobj.username
                return redirect('../hospitalbanklist')
            else:
                return render(request,'hospital_login.html',{'msg':'Incorrect Username or Password'})
        else:
            return render(request,'hospital_login.html',{'msg':'Incorrect Username or Password'})


def stockupdate(request):
    dsession = request.session.get('banksession')
    if request.method == 'GET':
       
        if dsession:
            dobj = bank.objects.get(username=dsession)
        dictbg = {}
        bloodgroups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        for bg in bloodgroups:
            try:
                dictbg[bg.replace("+", "1").replace("-", "2")] = stock.objects.get(bankid=dobj, bloodgroup=bg)
            except stock.DoesNotExist:
                dictbg[bg.replace("+", "1").replace("-", "2")] = None

        return render(request, 'stock.html',context=dictbg)
    
    elif request.method == 'POST':
        # dsession = request.session.get('banksession')
        if dsession:
            dobj = bank.objects.get(username=dsession)
            bloodgroup = request.POST.get('bg')
            unit = request.POST.get('unit')
            price=request.POST.get('price')

            try:
                # Check if the stock entry exists, update it if it does
                sobj = stock.objects.get(bankid=dobj, bloodgroup=bloodgroup)
                sobj.unit = unit
                sobj.price = price
            except stock.DoesNotExist:
                # Create a new stock entry if it does not exist
                sobj = stock(bankid=dobj, bloodgroup=bloodgroup, unit=unit, price=price)

            # sobj = stock(bankid=dobj, bloodgroup=bloodgroup, unit=unit)
            sobj.save()
            return redirect('../stock')

class totalbloodview(ListView):
    model=stock
    template_name='hositalbloodview.html'
    context_object_name='pobj'


def addcart(request):
    sid=request.POST.get('pid')
    print(sid)
    custsession=request.session['hospitalsession']#email of customer
    custobj=hospital.objects.get(username=custsession)#fetch all record from database table using email
    pobj=stock.objects.get(id=sid)
    print(custsession)
    
    
    flag=cart.objects.filter(hid=custobj.id,sid=pobj.id)
    if flag:
        cartobj=cart.objects.get(hid=custobj.id,sid=pobj.id)
        cartobj.quantity=cartobj.quantity+1
        cartobj.total=pobj.price*cartobj.quantity
        cartobj.save()
        
    else:
        cartobj=cart(hid=custobj,sid=pobj,quantity=1,total=pobj.price*1)
        cartobj.save()
    return redirect('../totalbloodview')

def viewcart(request):
    custsession=request.session['hospitalsession']
    custobj=hospital.objects.get(username=custsession)
    cartobj=cart.objects.filter(hid=custobj.id)

    return render(request,'viewcart.html',{'cartobj':cartobj,'session':custsession})

def changequantity(request):
    cemail = request.session['hospitalsession']
    pid = request.POST.get('pid')
    print(pid)
    custobj = hospital.objects.get(username = cemail)
    pobj = stock.objects.get(id = pid)
    cartobj = cart.objects.get(hid = custobj.id,sid=pobj.id)

    if request.POST.get('changequantitybutton')=='+':
        cartobj.quantity = cartobj.quantity + 1
        cartobj.total = cartobj.quantity * pobj.price
        cartobj.save()

    elif request.POST.get('changequantitybutton')=='-':
        if cartobj.quantity == 1:
            cartobj.delete()
        else :
            cartobj.quantity = cartobj.quantity - 1
            cartobj.total = cartobj.quantity * pobj.price
            print(cartobj.total)
            cartobj.save()

    return redirect('../viewcart')

def summary(request):
    custsession=request.session['hospitalsession']
    custobj=hospital.objects.get(username=custsession)
    cartobj=cart.objects.filter(hid=custobj.id)
    totalbill=0
    for i in cartobj:
        totalbill = i.total + totalbill 

    return render(request,'summary.html',{'session':custsession,'cartobj':cartobj,'totalbill':totalbill})

def placeorder(request):
    name=request.POST.get('fn')
    address=request.POST.get('address')
    city=request.POST.get('city')
    state=request.POST.get('state')
    pincode=request.POST.get('pincode')
    phoneno=request.POST.get('phoneno')

    datev= date.today()
    print(datev)
    orderobj=order(name=name, phoneno=phoneno, address=address, city=city, state=state, pincode=pincode, orderdate=datev, orderstatus='pending')
    orderobj.save()
    ono=str(orderobj.id) + str(datev).replace('-','')
    orderobj.ordernumber=ono
    orderobj.save()

    custsession=request.session['hospitalsession']
    custobj=hospital.objects.get(username=custsession)
    cartobj=cart.objects.filter(hid=custobj.id)
    

    totalbill=0
    for i in cartobj:
        totalbill=totalbill + i.total
    from django.core.mail import EmailMessage
    sm=EmailMessage('Order placed','order placed from pet store application.total bill for your order is'+str(totalbill),to=['Kushwahaaryan068@gmail.com'])
    sm.send()

       # authorize razorpay client with API Keys.
    razorpay_client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
 
 

    currency = 'INR'
    amount = 20000  # Rs. 200
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = '../petview'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZORPAY_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url

    return render(request,'payment.html',{'orderobj':orderobj,'session':custsession,'cartobj':cartobj,'totalbill':totalbill,'context':context})

def paymentsuccess(request):
    orderid=request.GET.get('order_id')
    tid = request.GET.get('payment_id')
    
    print(orderid)
    print(tid)

    request.session['hospitalsession']=request.GET.get('session')
    usersession=request.session['hospitalsession']
    print(usersession)      
    custobj=hospital.objects.get(username=usersession)
    cartobj=cart.objects.filter(hid=custobj.id)
    orderobj = order.objects.get(ordernumber = orderid)
    paymentobj=payment(hid=custobj,oid=orderobj,paymentstatus='complete',transactionid=tid,paymentmode='Razorpay')
    paymentobj.save()
    oobj=order.objects.filter(ordernumber=orderid).update(orderstatus='order placed')
    
    
    
    for i in cartobj:
        cartqnt=i.quantity
        prdqnt=stock.objects.get(id=i.sid.id)
        prdqnt.unit=prdqnt.unit-cartqnt
        prdqnt.save()     
            
    
        orderdetailobj=orderdetail(ordernumber=orderobj.ordernumber,hid=custobj,sid=i.sid,quantity=i.quantity,totalprice=i.total,paymentid=paymentobj)
        orderdetailobj.save()
        

        i.delete()
        
    return render(request,'paymentsuccess.html',{'session':usersession,'payobj':paymentobj})


def search(request):
    if request.method =="POST":
        searchdata=request.POST.get('searchquery')
        pobj=bank.objects.filter(Q(name__icontains = searchdata)|Q(city__icontains = searchdata)|Q(address__icontains = searchdata)|Q(state__icontains = searchdata))
        return render(request,'banklist.html',{'bobj':pobj})
    
def rsearch(request):
    if request.method =="POST":
        searchdata=request.POST.get('rsearchquery')
        pobj=bank.objects.filter(Q(name__icontains = searchdata)|Q(city__icontains = searchdata)|Q(address__icontains = searchdata)|Q(state__icontains = searchdata))
        return render(request,'recipientbanklist.html',{'rbobj':pobj})

def logout(request):
    del(request.session['donorsession'])
    return redirect('../donor_login')

def recipientlogout(request):
    del(request.session['recipientsession'])
    return redirect('../recipient_login')

def banklogout(request):
    del(request.session['banksession'])
    return redirect('../bank_login')

def donorprofile(request):
    dorsess=request.session['donorsession']
    dorr=donor.objects.filter(name=dorsess)
    if dorr:
        dorobj=donor.objects.get(name=dorsess)
    return render(request,'donorprofile.html',{'session':dorsess,'dorobj':dorobj})

def recipientprofile(request):
    dorsess=request.session['recipientsession']
    dorr=recipient.objects.filter(name=dorsess)
    if dorr:
        dorobj=recipient.objects.get(name=dorsess)
    return render(request,'recipientprofile.html',{'session':dorsess,'dorobj':dorobj})

def donoreditprofile(request):
    if request.method == 'GET':
        vendorsess=request.session['donorsession']
        vendorr=donor.objects.get(name=vendorsess)
        return render(request,'editdonor.html',{'context':vendorr})
    if request.method == 'POST':
        dname=request.POST.get('donorname')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        bloodgroup=request.POST.get('bloodgroup')
        address=request.POST.get('address')
        phoneno=request.POST.get('phoneno')
        state=request.POST.get('state')
        city=request.POST.get('city')
            
        vendorsess=request.session['donorsession']
        vendorr=donor.objects.filter(name=vendorsess).update(name=dname,age=age,gender=gender,bloodgroup=bloodgroup,address=address,phoneno=phoneno,state=state,city=city)
        return render(request,'donorprofile.html')
    
def recipienteditprofile(request):
    if request.method == 'GET':
        vendorsess=request.session['recipientsession']
        vendorr=recipient.objects.get(name=vendorsess)
        return render(request,'editrecipient.html',{'context':vendorr})
    if request.method == 'POST':
        rname=request.POST.get('rname')
        age=request.POST.get('age')
        address=request.POST.get('address')
        phoneno=request.POST.get('phoneno')
        state=request.POST.get('state')
        city=request.POST.get('city')
            
        vendorsess=request.session['recipientsession']
        vendorr=recipient.objects.filter(name=vendorsess).update(name=rname,age=age,address=address,phoneno=phoneno,state=state,city=city)
        return render(request,'recipientprofile.html')
