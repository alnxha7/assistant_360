from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from .models import login as log,state as st,district as dt,locations as loc
from .models import staff as stf,user as usr,feedback as fd, complaint as cm,labour as lb,taxibooking as taxibk, hotel as hot
from .models import bank as bnk, menutype as typ, bill as bl, menu as mnu, menustock as mst, Labour_complaint
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.db.models import Count
# Create your views here.

def index(request):
    role=request.session.get("role")
    if role == "admin":
        return redirect("/adminhome") 
    elif role == "staff":
        return redirect("/staffhome") 
    elif role == "user":
        return redirect("/userhome") 
    elif role== "taxi":
        return redirect("/taxihome")
    elif role== "hotel":
        return redirect("/hotelhome")
    

    datast=st.objects.all()
    return render(request,"index.html",{"datast":datast})

def admin(request):
    role=request.session.get("role")
    if role == "admin":
        return redirect("/adminhome") 
    elif role == "staff":
        return redirect("/staffhome") 
    elif role == "user":
        return redirect("/userhome") 
    elif role== "taxi":
        return redirect("/taxihome")
    elif role== "hotel":
        return redirect("/hotelhome")
    if request.POST:
        user = request.POST["username"]
        password = request.POST["password"]
        
        datac = log.objects.filter(username=user, password=password,role="admin").count()
        if datac==1:
                data=log.objects.get(username=user, password=password,role="admin")
                request.session['username'] = data.username
                request.session['role'] = data.role
                request.session['id'] = data.logid
                response = redirect('/adminhome')
                return response
        else:
                 return render(request,"adminlog.html",{"msg":"invalid username or password"})
    else:
        return render(request,"adminlog.html",{"msg":""})

def adminhome(request):
    role=request.session.get("role")
    if role != "admin":
        return redirect("/index")  

    return render(request,"adminhome.html")

def privacy(request):
    msg=""
    if request.POST:
        t1=request.POST["t1"]
        t2=request.POST["t2"]
        id=request.session['id']

        log.objects.filter(logid=id).update(password=t2)


    returnpage="adminhead.html"
    pg="Privacy.html"
    if(request.session.get('role', ' ')=="staff"):
        returnpage="staffhead.html"
    elif(request.session.get('role', ' ')=="user"):
        returnpage="userhead.html"
    elif(request.session.get('role', ' ')=="taxi"):
        returnpage="taxihead.html"
    elif(request.session.get('role', ' ')=="hotel"):
        returnpage="hotelhead.html"
        pg="Privacy1.html"
    return render(request,pg,{"role":returnpage,"msg":msg})

def getDistrict(request):
    id=request.GET["id"]
    datast=st.objects.get(state_id=id)
    datadt=dt.objects.filter(state=datast).all()
    res="<option value=''>-select-</option>"
    for d in datadt:
        res+="<option value='"+str(d.district_id)+"'>"+d.district+"</option>"
    return HttpResponse(res)

def Logout(request):
    try:
        del request.session['id']
        del request.session['role']
        del request.session['username']
        response = redirect("/index?id=logout")
        return response
    except:
        response = redirect("/index?id=logout")
        return response

def stafflogin(request):
    if request.POST:
        user = request.POST["username"]
        password = request.POST["password"]
        try:
            datac = log.objects.filter(username=user, password=password).count()
            if datac==1:
                data=log.objects.get(username=user, password=password)
                if data.role=="staff":
                    request.session['username'] = data.username
                    request.session['role'] = data.role
                    request.session['id'] = data.logid
                    response = redirect('/staffhome')
                    return response
                elif data.role=="user":
                    request.session['username'] = data.username
                    request.session['role'] = data.role
                    request.session['id'] = data.logid
                    response = redirect('/userhome')
                    return response
                elif data.role=="taxi":
                    request.session['username'] = data.username
                    request.session['role'] = data.role
                    request.session['id'] = data.logid
                    response = redirect('/taxihome')
                    return response
                elif data.role=="hotel":
                    request.session['username'] = data.username
                    request.session['role'] = data.role
                    request.session['id'] = data.logid
                    response = redirect('/hotelhome')
                    return response
                
                else :
                    response = redirect('/index?msg=invalid access')
                    return response


            else:
                response = redirect('/index?msg=invalid username or password')
                return response
               
        except:
            response = redirect('/index?msg=something went wrong')
            return response
    else:
        response = redirect('/index')
        return response

def staffreg(request):
    name=request.POST["name"]
    addr=request.POST["addr"]
    aadhar=request.POST["aadhar"]
    category=request.POST["category"]
    Experience=request.POST["Experience"]
    salary=request.POST["salary"]
    state=request.POST["state"]
    district=request.POST["district"]
  
    phone=request.POST["phone"]
    mail=request.POST["mail"]
    files=request.FILES["files"]
    username=request.POST["username"]
    password=request.POST["password"]
    datast=st.objects.get(state_id=state)
    datadt=dt.objects.get(district_id=district)
    
    log.objects.create(username=username,password=password,role="staff")
    datal=log.objects.last()
    stf.objects.create(login=datal,name=name,address=addr,aadhaar_no=aadhar,phone_no=phone,email=mail,state=datast,district=datadt,category=category,exp=Experience,basic_salary=salary,photo=files,status="waiting")
    response = redirect('/index')
    return response

def taxireg(request):
    name=request.POST["name"]
    addr=request.POST["addr"]
    aadhar=request.POST["aadhar"]
    category=request.POST["category"]
    Experience=request.POST["Experience"]
    salary=request.POST["salary"]
    state=request.POST["state"]
    district=request.POST["district"]
  
    phone=request.POST["phone"]
    mail=request.POST["mail"]
    files=request.FILES["files"]
    username=request.POST["username"]
    password=request.POST["password"]
    datast=st.objects.get(state_id=state)
    datadt=dt.objects.get(district_id=district)
    
    log.objects.create(username=username,password=password,role="0")
    datal=log.objects.last()
    stf.objects.create(login=datal,name=name,address=addr,aadhaar_no=aadhar,phone_no=phone,email=mail,state=datast,district=datadt,category=category,exp=Experience,basic_salary=salary,photo=files,status="waiting")
    response = redirect('/index')
    return response

def hotelreg(request):
    name=request.POST["name"]
    addr=request.POST["addr"]
    aadhar=request.POST["aadhar"]
    category=request.POST["category"]
    #Experience=request.POST["Experience"]
    #salary=request.POST["salary"]
    state=request.POST["state"]
    district=request.POST["district"]
   
  
    phone=request.POST["phone"]
    mail=request.POST["mail"]
    files=request.FILES["files"]
    username=request.POST["username"]
    password=request.POST["password"]
    datast=st.objects.get(state_id=state)
    datadt=dt.objects.get(district_id=district)
   
    
    log.objects.create(username=username,password=password,role="0")
    datal=log.objects.last()
    hot.objects.create(login=datal,hotel_name=name,hotel_address=addr,hotel_licence=aadhar,hotel_contact=phone,hotel_mail=mail,state=datast,district=datadt,category=category,photo=files,status="waiting")
    response = redirect('/index')
    return response

def userreg(request):
    name=request.POST["name"]
    addr=request.POST["addr"]
    state=request.POST["state"]
    district=request.POST["district"]
   
    phone=request.POST["phone"]
    mail=request.POST["mail"]
    files=request.FILES["file"]
    username=request.POST["username"]
    password=request.POST["password"]
    datast=st.objects.get(state_id=state)
    datadt=dt.objects.get(district_id=district)
    
    log.objects.create(username=username,password=password,role="user")
    datal=log.objects.last()
    usr.objects.create(login=datal,username=name,useraddress=addr,phoneno=phone,useremail=mail,
    state=datast,district=datadt,Photo=files,status="waiting")

    response = redirect('/index')
    return response

def staffhome(request):
    role=request.session.get("role")
    if role != "staff":
        return redirect("/index") 
    return render(request,"staffhome.html")
def userhome(request):
    role=request.session.get("role")
    if role != "user":
        return redirect("/index") 
    return render(request,"userhome.html")
def taxihome(request):
    role=request.session.get("role")
    if role != "taxi":
        return redirect("/index") 
    return render(request,"taxihome.html")
def hotelhome(request):
    role=request.session.get("role")
    if role != "hotel":
        return redirect("/index") 
    return render(request,"hotelhome.html")

def Add_state(request):
    msg=""
    if request.POST:
        t1=request.POST["state"]
        st.objects.create(state=t1)
        msg="inserted successfully"
    return render(request,"add_state.html",{"msg":msg})
    
def delete_state(request):
    id=request.POST["s_id"]
    st.objects.filter(state_id=id).delete()
    response = redirect("/list_state")
    return response
def edit_state(request):
    id=request.POST["s_id"]
    state=request.POST["state"]
    st.objects.filter(state_id=id).update(state=state)
    response = redirect("/list_state")
    return response
def list_state(request):
    datalst=st.objects.all()
    return render(request,"state_list.html",{"data":datalst})


def user_feed(request):
    if request.POST:
        t1= request.POST["t1"]
        t2= request.POST["t2"]
        fd.objects.filter(feedback_id=t1).update(reply=t2)
    data=fd.objects.all()
    return render(request,"user_feed.html",{"data":data})
def staff_complaints(request):
    if request.POST:
        t1= request.POST["t1"]
        t2= request.POST["t2"]
        cm.objects.filter(complaint_id=t1).update(reply=t2)
    data=cm.objects.all()
    return render(request,"staff_feed.html",{"data":data})

def complaints(request):
    id=request.session['id']
    datal=log.objects.get(logid=id)
    datas=stf.objects.get(login=datal)
    if request.POST:
        t1=request.POST["subject"]
        t2=request.POST["msg"]
        cm.objects.create(staff=datas,sub=t1,msg=t2,reply="not yet Seen")
    data=cm.objects.filter(staff=datas).all()
    return render(request,"complaints.html",{"data":data})

def feedback(request):
    id=request.session['id']
    datal=log.objects.get(logid=id)
    datau=usr.objects.get(login=datal)
    if request.POST:
        t1=request.POST["feedback"]
        fd.objects.create(userid=datau,feedback=t1,reply="not yet Seen")
    data=fd.objects.filter(userid=datau).all()
    return render(request,"feedback.html",{"data":data})

##########################################   taxi   #############################################################

def taxiRegister(request):
    msg = ""
    return render(request,"taxiRegister.html",{"msg":msg})

def newtaxistf(request):
    data=stf.objects.filter(status="waiting").all()
    return render(request,"newtaxistf.html",{"data":data})

def approve_taxistf(request):
    data=stf.objects.filter(status="waiting").all()
    return render(request,"approve_taxistf.html",{"data":data})
    
def approved_taxistf(request):
    id=request.POST["staff_id"]
    lid=request.POST["lid"]
    
    stf.objects.filter(staff_id=id).update(status="approved")
    log.objects.filter(login=lid).update(role="taxi")
    response = redirect("/approve_taxistf")
    return response


def reject_staff(request):
    id=request.POST["staff_id"]
    stf.objects.filter(staff_id=id).delete()
    response = redirect("/approve_taxistf")
    return response

def taxibook(request):
    
    if request.POST:
        pickup_point=request.POST["pickup_point"]
        destination_point=request.POST["destination_point"]
        travel_time=request.POST["travel_time"]
        travel_date=request.POST["travel_date"]
        booking_date=request.POST["booking_date"]
        amount=request.POST["amount"]
        km=request.POST["km"]
        logid = request.session['id']
        logdata =stf.objects.get(login=logid)
        taxibk.objects.create(taxiid=logdata,pickup_point=pickup_point,destination_point=destination_point,travel_time=travel_time,travel_date=travel_date,
        booking_date=booking_date,amount=amount,km=km,status="waiting")
    
    response = redirect('/taxiRegister')
    return response
    
def newtaxi(request):
    data=taxibk.objects.filter(status="waiting").all()
    return render(request,"newtaxi.html",{"data":data})

def taxibookDelete(request):
    booking_id=request.POST["booking_id"]
    taxibk.objects.filter(booking_id=booking_id).delete()
    response = redirect('/newtaxi')
    return response

def approve_taxi(request):
    datatour=taxibk.objects.filter(status="waiting").all()
    return render(request,"newtaxi.html",{"data":datatour})

def approved_taxi(request):
    booking_id=request.POST["booking_id"]
    taxibk.objects.filter(booking_id=booking_id).update(status="alloted")
    response = redirect("/newtaxi")
    return response

def taxi_approvelist(request):
    data=taxibk.objects.filter(status="alloted").all()
    return render(request,"allotedtaxi.html",{"data":data})

def edit_amt(request):
    booking_id=request.POST["booking_id"]
    amount=request.POST["amount"]
    km=request.POST["km"]
    taxibk.objects.filter(booking_id=booking_id).update(amount=amount,km=km)
    response = redirect("/taxi_approvelist")
    return response
def edit_km(request):
    booking_id=request.POST["booking_id"]
   
    km=request.POST["km"]
    taxibk.objects.filter(booking_id=booking_id).update(km=km)
    response = redirect("/taxi_approvelist")
    return response

def texibookingreject(request):
    booking_id=request.POST["booking_id"]
    taxibk.objects.filter(booking_id=booking_id).delete()
    response = redirect('/taxi_approvelist')
    return response

def taxi_rejected(request):
    datag=taxibk.objects.filter(status="rejected").all()
    return render(request,"taxi_rejected.html",{"data":datag})

def approve_taxibook(request):
    datatour=taxibk.objects.filter(status="alloted").exclude(reject="rejected").all()
    return render(request,"allotedtaxi.html",{"data":datatour})

def approved_taxibook(request):
    booking_id=request.POST["booking_id"]
    taxibk.objects.filter(booking_id=booking_id).update(status="confirmed")
    response = redirect("/taxi_approvelist")
    return response



def taxi_confirm(request):
    dataff=taxibk.objects.filter(status="confirmed").all()
    return render(request,"taxi_confirm.html",{"data":dataff})

def request_taxipayment(request):
    lid=request.POST["lid"]
    taxibk.objects.filter(booking_id=lid).update(status="paymentrequested")
    return redirect("/taxi_confirm")

def waiting_taxipayment(request):
    datag=taxibk.objects.filter(status="paymentrequested").all()
    return render(request,"taxiwaiting_payment.html",{"data":datag})

def payment_taxicompleted(request):
    datag=taxibk.objects.filter(status="completed").all()
    return render(request,"taxipayment_completed.html",{"data":datag})

def payment_taxirequest(request):
    id=request.session['id']
    datal=log.objects.get(logid=id)
    datau=usr.objects.get(login=datal)
    msg=""
    if request.POST:
        t1=request.POST["t1"] #card
        t2=request.POST["t2"] #holder
        t3=request.POST["t3"] #cvv
        t4=int(request.POST["t4"]) #amt
        t5=request.POST["t5"] #userid
        t6=request.POST["t6"] #lab
        bcc=bnk.objects.filter(holder=t2,card=t1,cvv=t3).count()
        if bcc==1:
            datb=bnk.objects.get(holder=t2,card=t1,cvv=t3)
            bal=int(datb.bal)
            if bal < t4 :
                msg="insufficient Balance"
            else:
                bmt=bal-t6
                bnk.objects.filter(holder=t2,card=t3,cvv=t4).update(bal=bmt)
                taxibk.objects.filter(booking_id=t1).update(status="completed")
                msg="payment successfull"
        else :
            msg="invalid account details"


    datag=taxibk.objects.filter(status="paymentrequested",userid=datau).all()
    datac=taxibk.objects.filter(status="paymentrequested",userid=datau).count()
    return render(request,"taxipayment_request.html",{"data":datag,"datac":datac,"msg":msg})

def payment_taxihistory(request):
    datag=taxibk.objects.filter(status="completed").all()
    return render(request,"taxipayment_history.html",{"data":datag})

#################################################   hotel   #############################################

def newhotel(request):
    data=hot.objects.filter(status="waiting").all()
    return render(request,"newhotel.html",{"data":data})

def approve_hotel(request):
    data=hot.objects.filter(status="waiting").all()
    return render(request,"newhotel.html",{"data":data})
    
def approved_hotel(request):
    id=request.POST["hotel_id"]
    lid=request.POST["lid"]
    
    hot.objects.filter(staff_id=id).update(status="approved")
    log.objects.filter(login=lid).update(role="hotel")
    response = redirect("/approve_hotel")
    return response


def reject_hotel(request):
    id=request.POST["hotel_id"]
    hot.objects.filter(hotel_id=id).delete()
    response = redirect("/approve_hotel")
    return response

    
def Manage_Menutype(request):
    msg=""
    if request.POST:
        t1 = request.POST["t1"]
        msg="posted sucessfully"
        typ.objects.create(type_name=t1)
    data=typ.objects.all()
    return render(request, "Add_type.html",{"msg":msg,"data":data})

def Manage_Menu(request):
    msg=""
    if request.POST:
        t1 = request.POST["t1"]
        t2 = request.POST["t2"]
        t3 = request.POST["t3"]
        t4 = request.FILES["t4"]
        fs = FileSystemStorage()
        fnm=fs.save(t4.name, t4)
        dataty= typ.objects.get(type_id=t1)
        msg="posted sucessfully"
        mnu.objects.create(menu_type=dataty,menu_name=t2,menu_price=t3,menu_photo=t4)

        
    data=mnu.objects.all()
    data1=typ.objects.all()
    return render(request, "Add_menu.html",{"msg":msg,"data":data,"data1":data1})

def delete_type(request):
    typ.objects.filter(type_id=request.GET["id"]).delete()
    response = redirect('/Manage_Menutype')
    return response

def delete_menu(request):
    mnu.objects.filter(menu_id=request.GET["id"]).delete()
    response = redirect('/Manage_Menu')
    return response

def getmenu(request):
    st="<option value=''>-select-</option>"
    data=mnu.objects.filter(menu_type=request.GET["id"]).all()
    for datas in data:
        st+="<option value='"+str(datas.menu_id)+"'>"+datas.menu_name+"</option>"
    
    return HttpResponse(st)
def getdt(request):
    st="0"
    data=mnu.objects.get(menu_id=request.GET["t2"])
    dat=request.GET["id"]
    dc=mst.objects.filter(date=dat,menu_id=data).count()
    if dc > 0:
        dr=mst.objects.get(date=dat,menu_id=data)
        st=dr.qty
    return HttpResponse(st)
def Manage_Stock(request):
    msg=""
    if request.POST:
        t1 = request.POST["t1"]
        t2 = request.POST["t2"]
        t3 = request.POST["t3"]
        t4 = request.POST["t4"]
        data=mnu.objects.get(menu_id=t2)
        dc=mst.objects.filter(date=t3,menu_id=data).count()
        if dc > 0:
            mst.objects.filter(date=t3,menu_id=data).update(qty=t4)
            msg="stock updated"
        else:
            msg="stock Added"
            mst.objects.create(menu_id=data,qty=t4,date=t3)
    data1=typ.objects.all()
    data=mst.objects.all()
    return render(request, "Add_menustock.html",{"msg":msg,"data1":data1,"data":data})

def delete_stock(request):
    mst.objects.filter(stock_id=request.GET["id"]).delete()
    response = redirect('/Manage_Stock')
    return response

def getlist(request):
    st=""
    data=mst.objects.filter(date=request.GET["id"]).all()
    i=1
    for datas in data:
        st+='''<tr>
            <td>'''+ str(i) +'''</td>
            <td><img src="/media/'''+str(datas.menu_id.menu_photo)+'''" width="50px" height="50px"/></td>
            <td>'''+datas.menu_id.menu_type.type_name+'''</td>
            <td>'''+datas.menu_id.menu_name+'''</td>
            <td>'''+str(datas.menu_id.menu_price)+'''</td>
            <td>'''+datas.date+'''</td>
            <td>'''+str(datas.qty)+'''</td>
    
            <td><a class="btn-danger btn" href="delete_stock/?id='''+str(datas.stock_id)+'''">Remove</a></td>
    

            </tr>'''
        i+=1
    
    return HttpResponse(st)
def myorder2(request):
    msg=""
    
   
    data=bl.objects.filter().all()
    return render(request,"myorder2.html",{"msg":msg,"data":data})



##########################################################################################################


def find_labour(request):
    datas=st.objects.all()
    data=stf.objects.filter(blacklisted=False)
    datc=stf.objects.count()
    
    if request.POST:
        t1=request.POST["state"]
        t2=request.POST["district"]
        #t3=request.POST["location"]
        t4=request.POST["category"]
        datast=st.objects.get(state_id=t1)
        datadt=dt.objects.get(district_id=t2)
        #datalc=loc.objects.get(location_id=t3)
        # data=stf.objects.filter(state=datast,district=datadt,location=datalc).all()
        # datc=stf.objects.filter(state=datast,district=datadt,location=datalc).count()
        data=stf.objects.filter(state=datast,district=datadt,category=t4).all()
        datc=stf.objects.filter(state=datast,district=datadt,category=t4).count()
    return render(request,"find_labour.html",{"datas":datas,"data":data,"datc":datc})

def book_labour(request):
    staff = request.GET["staff"]
    state = request.GET["state"]
    district = request.GET["district"]
    location = request.GET["location"]
    category = request.GET["category"]
    datastf = stf.objects.get(staff_id=staff)

    if request.POST:
        t1 = request.POST["fdate"]
        t2 = request.POST["todate"]
        t3 = request.POST["category"]
        t4 = request.POST["staff"]
        t5 = request.POST["aboutjob"]
        t6 = request.POST["amt"]
        id = request.session['id']
        datal = log.objects.get(logid=id)
        datau = usr.objects.get(login=datal)

        # Check if the staff is already engaged during the selected dates
        is_engaged = lb.objects.filter(staff_id=t4, from_date__lte=t2, to_date__gte=t1).exists()

        if is_engaged:
            messages.error(request, "Cannot book; this staff is already engaged.")
        else:
            datas=stf.objects.get(staff_id=t4)
            lb.objects.create(userid=datau,staff=datas,from_date=t1,to_date=t2,category=t3,desc=t5,amount=t6,reject="",status="waiting")
            messages.success(request, "Booking request sent successfully.")
        
    return render(request,"book_labour.html",{"datastf":datastf,"staff":staff,"state":state,"district":district,"location":location,"category":category})


def staff_ongoing(request):
    datag=lb.objects.filter(status="approved").exclude(reject="rejected").all()
    return render(request,"staff_ongoing.html",{"data":datag})

def staff_rejected(request):
    datag=lb.objects.filter(reject="rejected").all()
    return render(request,"staff_rejected.html",{"data":datag})

def staff_completed(request):
    datag=lb.objects.filter(status="stfcompleted").all()
    return render(request,"staff_completed.html",{"data":datag})

def payment_completed(request):
    datag=lb.objects.filter(status="completed").all()
    return render(request,"payment_completed.html",{"data":datag})

def request_payment(request):
    lid=request.POST["lid"]
    lb.objects.filter(labour_id=lid).update(status="paymentrequested")
    return redirect("/staff_completed")

def waiting_payment(request):
    datag=lb.objects.filter(status="paymentrequested").all()
    return render(request,"waiting_payment.html",{"data":datag})

def payment_request(request):
    id=request.session['id']
    datal=log.objects.get(logid=id)
    datau=usr.objects.get(login=datal)
    msg=""
    if request.POST:
        t1=request.POST["card"] #cardnumber
        t2=request.POST["holder"] #holdername
        t3=request.POST["cvv"] #cvv
        t4=int(request.POST["amt"]) #amt to pay
        t5=request.POST["lid"] #labourid
        #t6=request.POST["t6"] #lab

        try:
            bnk.objects.create(holder=t2,
                               card=t1,
                               cvv=t3,
                               amount=t4

            )
            lb.objects.filter(labour_id=t5).update(status="completed")
            return redirect('success')
        except bnk.DoesNotExist:
            msg= 'invalid account details'
            
    datag=lb.objects.filter(status="paymentrequested",userid=datau).all()
    datac=lb.objects.filter(status="paymentrequested",userid=datau).count()
    return render(request,"payment_request.html",{"data":datag,"datac":datac,"msg":msg})

def payment_history(request):
    datag=lb.objects.filter(status="completed").all()
    return render(request,"payment_history.html",{"data":datag})


def payment_history(request):
    datag=lb.objects.filter(status="completed").all()
    return render(request,"payment_history.html",{"data":datag})

def ongoing(request):
    id=request.session['id']
    datal=log.objects.get(logid=id)
    datau=stf.objects.get(login=datal)
    datag=lb.objects.filter(status="approved",reject="confirm",staff=datau).all()
    return render(request,"ongoing.html",{"data":datag})

def schedule(request):
    datasb=lb.objects.exclude(status="completed").exclude(status="paymentrequested").exclude(reject="rejected").all()
    return render(request,"schedule.html",{"datakk":datasb})

def delete_labour(request):
    id=request.POST["labour_id"]
    lb.objects.filter(labour_id=id).delete()
    response = redirect("/schedule")
    return response

def complete(request):
     dataty=lb.objects.filter(status="completed").all()
     return render(request,"complete.html",{"datatt":dataty})

def rejected(request):
     datatm=lb.objects.filter(reject="rejected").all()
     return render(request,"rejected.html",{"datamm":datatm})


#/* amitha */
def add_district(request):
    msg=""
    data=st.objects.all()
    if request.POST:
        t1=request.POST["state"]
        t2=request.POST["district"]
        datast=st.objects.get(state_id=t1)
        dt.objects.create(state=datast,district=t2)
        msg="inserted successfully"
    return render(request,"add_district.html",{"msg":msg,"data":data})

def list_district(request):
    data=dt.objects.all()
    dataldt=st.objects.all()
    return render(request,"list_district.html",{"data":data,"datas":dataldt})

def edit_district(request):
    id=request.POST["d_id"]
    state=request.POST["district"]
    sid=request.POST["state"]
    state=st.objects.get(state_id=sid)
    dt.objects.filter(district_id=id).update(district=state)
    response = redirect("/list_district")
    return response

def delete_district(request):
    id=request.POST["d_id"]
    st.objects.filter(district_id=id).delete()
    response = redirect("/list_district")
    return response

def list_user(request):
    datausr=usr.objects.filter(status="approved").all()
    if request.POST:
        t1=request.POST["ser_user"]
        datausr=usr.objects.filter(status="approved",username=t1).all()

    
    return render(request,"list_user.html",{"data":datausr})
def delete_user(request):
    id=request.POST["user_id"]
    usr.objects.filter(user_id=id).delete()
    response = redirect("/list_user")
    return response

def list_staff(request):
    datast=stf.objects.filter(status="approved").all()
    if request.POST:
        t1=request.POST["search_cat"]
        datast=stf.objects.filter(status="approved",category=t1).all()

    return render(request,"list_staff.html",{"data":datast})
def delete_staff(request):
    id=request.POST["staff_id"]
    stf.objects.filter(staff_id=id).delete()
    response = redirect("/list_staff")
    return response
def approve_staff(request):
    datastf=stf.objects.filter(status="waiting").all()
    return render(request,"approve_staff.html",{"data":datastf})
    
def approved_staff(request):
    id=request.POST["staff_id"]
    stf.objects.filter(staff_id=id).update(status="approved")
    response = redirect("/approve_staff")
    return response
def reject_staff(request):
    id=request.POST["staff_id"]
    stf.objects.filter(staff_id=id).delete()
    response = redirect("/approve_staff")
    return response
def approve_user(request):
    datauser=usr.objects.filter(status="waiting").all()
    return render(request,"approve_user.html",{"data":datauser})

def approved_user(request):
    id=request.POST["user_id"]
    usr.objects.filter(user_id=id).update(status="approved")
    response = redirect("/approve_user")
    return response

def reject_user(request):
    id=request.POST["user_id"]
    usr.objects.filter(user_id=id).delete()
    response = redirect("/approve_user")
    return response

def newjob(request):
    data=lb.objects.filter(status="waiting").all()
    return render(request,"newjob.html",{"data":data})

def job_confirm(request):
    dataff=lb.objects.filter(status="approved",reject="").all()
    return render(request,"job_confirm.html",{"datavb":dataff})

def confirm_labour(request):
    id=request.POST["labour_id"]
    lb.objects.filter(labour_id=id).update(reject="confirm")
    return redirect("/job_confirm")
    
def reject_labour(request):
    id=request.POST["labour_id"]
    lb.objects.filter(labour_id=id).update(reject="rejected")
    return redirect("/job_confirm")

def newjob_approve(request):
    id=request.POST["lid"]
    lb.objects.filter(labour_id=id).update(status="approved")
    return redirect("/newjob")

def task_complete(request):
    id=request.POST["lid"]
    lb.objects.filter(labour_id=id).update(status="stfcompleted")
    return redirect("/ongoing")





##########################################################################
##########################################################################
##########################################################################

from django.http import HttpResponse,JsonResponse
import os 
import json


def app_login(request):
    t1=request.POST["t1"]
    t2=request.POST["t2"]
    msg="try again later"
    
    try:
        dat=log.objects.get(username=t1,password=t2)
        if(dat.role == "user"):
            
            msg="ok:"+str(dat.logid)
        else:
            msg="invalid account Details"
    except:
         msg="invalid user name or password"
    data=[{'result': msg}]
    return JsonResponse(data, safe=False)

def app_profile(request):
    t1=request.POST["t1"]
    glg=log.objects.get(logid=t1)
    datar=usr.objects.filter(login=glg).all()
    data=[]
    for d in datar:
        dv={"user_id":d.user_id,"username":d.username,"useraddress":d.useraddress,"phoneno":d.phoneno,"useremail":d.useremail,"state":d.state.state,"district":d.district.district,"location":d.location.location,"Photo":str(d.Photo),"status":d.status}
        data.append(dv)
    return JsonResponse(data, safe=False)
def app_register(request):
    t1=request.POST["t1"]
    t2=request.POST["t2"]
    t3=request.POST["t3"]
    t4=request.POST["t4"]
    t5=request.POST["t5"]
    t6=request.POST["t6"]
    t7=request.POST["t7"]
    dat=log.objects.create(username=t6,password=t7,role="user")
    data=log.objects.last()
    usr.objects.create(User_name=t1,User_address=t2,User_email=t3,User_phone=t4,User_alt_No=t5,Log_id=data,User_status="approved")
    msg="ok"
    data=[{'result': msg}]
    return JsonResponse(data, safe=False)

def app_editPassword(request):
    t1=request.POST["t1"]
    t2=request.POST["t2"]
    t3=request.POST["t3"]
    data=log.objects.get(logid=t3)
    if data.password==t1:
        msg="ok"
        log.objects.filter(logid=t3).update(password=t2)
    else:
        msg="invalid current password"
    
    data=[{'result': msg}]
    return JsonResponse(data, safe=False)

def app_listservices(request):
    datar={"as":"as"}
    data=json.dumps(list(datar))
    return HttpResponse(data, content_type="application/json")

def app_getstate(request):
    datar=st.objects.all().values("state_id","state")
    data=json.dumps(list(datar))
    return HttpResponse(data, content_type="application/json")

def app_getdist(request):
    id=request.POST["t1"]
    dts=st.objects.get(state_id=id)
    datar=dt.objects.filter(state=dts).values("district_id","district")
    data=json.dumps(list(datar))
    return HttpResponse(data, content_type="application/json")   

def app_getloc(request):
    id=request.POST["t1"]
    lcs=dt.objects.get(district_id=id)
    datar=loc.objects.filter(distict=lcs).values("location_id","location")
    data=json.dumps(list(datar))
    return HttpResponse(data, content_type="application/json")

def app_getstaff(request):
    t1=request.POST["t1"]
    loct=loc.objects.get(location_id=t1)
    t2=request.POST["t2"]
    datar=stf.objects.filter(location=loct,category=t2).values("staff_id","name","address","aadhaar_no","phone_no","email","state","district","location","category","exp","basic_salary","photo","status")
    data=json.dumps(list(datar))
    return HttpResponse(data, content_type="application/json")

def app_Booking(request):
    t1=request.POST["t1"]
    t2=request.POST["t2"]
    t3=request.POST["t3"]
    t4=request.POST["t4"]
    t5=request.POST["t5"]
    t6=request.POST["t6"]#userid
    t7=request.POST["t7"]#staffid
    datal=log.objects.get(logid=t6)
    datau=usr.objects.get(login=datal)
        
    datas=stf.objects.get(staff_id=t7)

    lb.objects.create(userid=datau,staff=datas,from_date=t1,to_date=t2,category=t3,desc=t4,amount=t5,reject="",status="waiting")
    data=[{'result': "ok"}]
    return JsonResponse(data, safe=False)

def app_myBooking(request):
    t1=request.POST["t1"]
    datal=log.objects.get(logid=t1)
    datau=usr.objects.get(login=datal)
    dtr=lb.objects.filter(userid=datau).all()
    data=[]
    for dt in dtr:
        dv={"labour_id":dt.labour_id,"staff":dt.staff.name,"phone":dt.staff.phone_no,"email":dt.staff.email,"from_date":dt.from_date,
        "to_date":dt.to_date,"category":dt.category,"desc":dt.desc,"amount":dt.amount,"reject":dt.reject,"status":dt.status}
        data.append(dv)
    print(data)
    #labour_id,staff,phone,email,from_date,to_date,category,desc,amount,reject,status
    return JsonResponse(data, safe=False)

def app_pay(request):
        msg=""
        t1=request.POST["t1"] #card
        t2=request.POST["t2"] #holder
        t3=request.POST["t3"] #cvv
        t4=int(request.POST["t4"]) #amt
        t5=request.POST["t5"] #userid
        t6=request.POST["t6"] #lab
        bcc=bnk.objects.filter(holder=t2,card=t1,cvv=t3).count()
        if bcc==1:
            datb=bnk.objects.get(holder=t2,card=t1,cvv=t3)
            bal=int(datb.bal)
            if bal < t4 :
                msg="insufficient Balance"
            else:
                bmt=bal-t4
                bnk.objects.filter(holder=t2,card=t1,cvv=t3).update(bal=bmt)
                lb.objects.filter(labour_id=t6).update(status="completed")
                msg="ok"
        else :
            msg="invalid account details"


        data=[{'result': msg}]
        return JsonResponse(data, safe=False)

def app_regComplaint(request):

    t2 = request.POST["t2"]
    t3 = request.POST["t3"]
    #today = date.today()
    datax=usr.objects.get(login=t3)
                
    msg="ok"
    fd.objects.create(userid=datax,feedback=t2,reply="not yet Seen")
    data=[{'result': msg}]
    return JsonResponse(data, safe=False)

def app_getComplaint(request):
    t1 = request.POST["t1"]
    datax=usr.objects.get(login=t1)
    datar=fd.objects.filter(userid=datax).values("feedback_id","userid","feedback","reply")
    #feedback_id,userid,feedback,reply
    data=json.dumps(list(datar))
    return HttpResponse(data, content_type="application/json")

def success(request):
    return render(request, "success.html")

def labour_complaint(request):
    id = request.session['id']
    datal = log.objects.get(logid=id)
    datau = usr.objects.get(login=datal)

    # Filter labours with status 'completed'
    labours = lb.objects.filter(userid=datau, status='completed')
    complaints = Labour_complaint.objects.filter(userid=datau)

    if request.method == 'POST':
        staff_id = request.POST['staff']
        complaint_text = request.POST['complaint']

        # Get the selected staff and user
        selected_staff = stf.objects.get(staff_id=staff_id)

        # Create and save the complaint
        Labour_complaint.objects.create(userid=datau, staff=selected_staff, complaint=complaint_text)

        # Count the number of complaints against this staff
        complaint_count = Labour_complaint.objects.filter(staff=selected_staff).count()

        # Blacklist the staff if complaints exceed 3
        if complaint_count > 3:
            selected_staff.blacklisted = True
            selected_staff.save()

    return render(request, 'labour_complaint.html', {'labours': labours, 'complaints': complaints})

def delete_complaint(request, complaint_id):
    if request.method == 'POST':
        complaint = get_object_or_404(Labour_complaint, labour_id=complaint_id)
        complaint.delete()
    return redirect('labour_complaint')

def edit_booking(request):
    if request.method == 'POST':
        labour_id = request.POST['labour_id']
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']

        # Get the labour instance being edited
        labour = lb.objects.get(labour_id=labour_id)

        # Check if the staff is engaged on the new dates
        staff_engaged = lb.objects.filter(
            staff=labour.staff,
            from_date__lte=to_date,
            to_date__gte=from_date
        ).exclude(labour_id=labour_id).exists()

        if staff_engaged:
            # Display alert message if staff is engaged
            messages.error(request, 'Cannot book; this staff is already engaged on the selected dates.')
            return redirect('schedule')  # Replace with your actual URL name for the schedule page
        else:
            # If not engaged, update the booking
            labour.from_date = from_date
            labour.to_date = to_date
            labour.save()
            messages.success(request, 'Booking updated successfully.')
            return redirect('schedule')  # Replace with your actual URL name for the schedule page
    return redirect('schedule')

def staff_complaints(request):
    staff_data = stf.objects.annotate(
        num_complaints=Count('labour_complaint')
    ).values(
        'staff_id', 'photo', 'name', 'category', 'phone_no', 'email', 'blacklisted', 'num_complaints'
    )
    return render(request, 'staff_complaints.html', {'staff_data': staff_data})

def remove_blacklist(request, staff_id):
    staff_member = get_object_or_404(stf, pk=staff_id)
    staff_member.blacklisted = False
    staff_member.save()
    return redirect('staff_complaints')

def make_blacklist(request, staff_id):
    staff_member = get_object_or_404(stf, pk=staff_id)
    staff_member.blacklisted = True
    staff_member.save()
    return redirect('staff_complaints')
