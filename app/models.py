from django.db import models

# Create your models here.

class login(models.Model):
    logid = models.AutoField(primary_key=True)
    username = models.CharField("username",max_length=100)
    password =  models.CharField("password",max_length=100)
    role=models.CharField('role',max_length=10)
    #logid,username,password,role

class state(models.Model):
    state_id = models.AutoField(primary_key=True)
    state=models.CharField("state",max_length=100)
#state_id,state

class district(models.Model):
    district_id=models.AutoField(primary_key=True)
    district=models.CharField("district",max_length=100)
    state=models.ForeignKey(state, on_delete=models.CASCADE, null=True)
#district_id,district,state

class locations(models.Model):
    location_id=models.AutoField(primary_key=True)
    location=models.CharField("location",max_length=100)
    distict=models.ForeignKey(district, on_delete=models.CASCADE, null=True)
    @property
    def getalldist(self):
        data=district.objects.filter(state=self.distict.state).all()
        return data
#location_id,location

class staff(models.Model):
    staff_id= models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
    name=models.CharField("staffname",max_length=100)
    address=models.CharField("address",max_length=500)
    aadhaar_no=models.CharField("aadhaar",max_length=100)
    phone_no=models.CharField("phone_no",max_length=100)
    email=models.CharField("email",max_length=100)
    state=models.ForeignKey(state,on_delete=models.CASCADE, null=True)
    district=models.ForeignKey(district, on_delete=models.CASCADE, null=True)
    location=models.ForeignKey(locations, on_delete=models.CASCADE, null=True)
    category=models.CharField("category",max_length=100)
    
    exp=models.CharField("experience",max_length=100)
    basic_salary=models.CharField("basic_salary",max_length=100)
    photo=models.FileField("photo:",max_length=100,upload_to="images/")
    status=models.CharField("status:",max_length=100)
    #staff_id,login,name,address,aadhaar_no,phone_no,email,state,district,location,category,exp,basic_salary,photo,status

class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
    username=models.CharField("username",max_length=100)
    useraddress=models.CharField("address",max_length=500)
    phoneno=models.CharField("Phone_no",max_length=100)
    useremail=models.CharField("email",max_length=100)
    state=models.ForeignKey(state,on_delete=models.CASCADE, null=True)
    district=models.ForeignKey(district, on_delete=models.CASCADE, null=True)
    location=models.ForeignKey(locations, on_delete=models.CASCADE, null=True)
    Photo=models.FileField("photo:",max_length=100,upload_to="images/")
    status=models.CharField("status:",max_length=100)
    #user_id,login,username,useraddress,phoneno,useremail,state,district,location,Photo,status

class taxibooking(models.Model):
    booking_id=models.AutoField(primary_key=True)
    pickup_point=models.CharField("pickup_point",max_length=100)
    destination_point=models.CharField("destination_point",max_length=100)
    travel_time=models.CharField("travel_time",max_length=100)
    travel_date=models.CharField("travel_date",max_length=100)
    booking_date=models.CharField("travel_date",max_length=100)
    userid=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    taxiid=models.ForeignKey(staff,on_delete=models.CASCADE,null=True)
    amount=models.CharField("amount",max_length=100)
    km=models.CharField("km",max_length=100)
    status=models.CharField("status",max_length=100)

class hotel(models.Model):
    hotel_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
    hotel_name=models.CharField("hotel_name",max_length=100)
    hotel_licence=models.CharField("hotel_licence",max_length=100)
    hotel_address=models.CharField("hotel_address",max_length=500)
    state=models.ForeignKey(state,on_delete=models.CASCADE, null=True)
    district=models.ForeignKey(district, on_delete=models.CASCADE, null=True)
    location=models.ForeignKey(locations, on_delete=models.CASCADE, null=True)
    category=models.CharField("category",max_length=100)
    hotel_contact=models.CharField("hotel_contact",max_length=100)
    hotel_mail=models.CharField("hotel_mail",max_length=100)
    photo=models.FileField("photo:",max_length=100,upload_to="images/")
    status=models.CharField("status",max_length=100)

class menutype(models.Model):
    type_id= models.AutoField(primary_key=True)
    type_name = models.CharField("type_name", max_length=100)
    hotel =models.ForeignKey(hotel, on_delete=models.CASCADE, null=True)

class menu(models.Model):
    menu_id= models.AutoField(primary_key=True)
    menu_name = models.CharField("menu_name", max_length=100)
    menu_price = models.CharField("menu_price", max_length=100)
    menu_type =models.ForeignKey(menutype, on_delete=models.CASCADE, null=True)
    hotel =models.ForeignKey(hotel, on_delete=models.CASCADE, null=True)
    menu_photo = models.FileField("menu_photo", max_length=1000,upload_to='images/')

class menustock(models.Model):
    stock_id= models.AutoField(primary_key=True)
    menu_id=models.ForeignKey(menu, on_delete=models.CASCADE, null=True)
    hotel =models.ForeignKey(hotel, on_delete=models.CASCADE, null=True)
    qty = models.CharField("qty", max_length=100)
    date = models.CharField("date", max_length=100)

class cart(models.Model):
    cart_id= models.AutoField(primary_key=True)
    stock_id=models.ForeignKey(menustock, on_delete=models.CASCADE, null=True)
    menu_id=models.ForeignKey(menu, on_delete=models.CASCADE, null=True)
    hotel =models.ForeignKey(hotel, on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    pqty = models.CharField("pqty", max_length=100)
    cart_date=models.CharField("date", max_length=100)
    cart_status = models.CharField("cart_status", max_length=100)

class bill(models.Model):
    billno= models.AutoField(primary_key=True)
    date=models.CharField("date", max_length=100)
    user=models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    total=models.CharField("date", max_length=100)
    order_status = models.CharField("order_status", max_length=100)

class orderlist(models.Model):
    orderno= models.AutoField(primary_key=True)
    cart_id=models.ForeignKey(cart, on_delete=models.CASCADE, null=True)
    billno=models.ForeignKey(bill, on_delete=models.CASCADE, null=True)

class labour(models.Model):
    labour_id=models.AutoField(primary_key=True)
    userid=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    staff=models.ForeignKey(staff,on_delete=models.CASCADE,null=True)
    from_date=models.CharField("from date",max_length=100)
    to_date=models.CharField("to date",max_length=100)
    category=models.CharField("category",max_length=100)
    desc=models.CharField("description",max_length=500)
    amount=models.CharField("amount",max_length=100)
    reject=models.CharField("reject",max_length=100)
    status=models.CharField("status",max_length=100)
    #userid,staff,from_date,to_date,category,desc,amount,reject,status

class feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    userid=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    feedback=models.CharField("feedback",max_length=500)
    reply=models.CharField("reply",max_length=500)
    #feedback_id,userid,feedback,reply

class complaint(models.Model):
    complaint_id=models.AutoField(primary_key=True)
    staff=models.ForeignKey(staff,on_delete=models.CASCADE,null=True)
    sub=models.CharField("sublect",max_length=200)
    msg=models.CharField("message",max_length=500)
    reply=models.CharField("reply",max_length=500)
    #staff,sub,msg,reply
    
class bank(models.Model):
    bank_id=models.AutoField(primary_key=True)
    holder=models.CharField("holder",max_length=100)
    card=models.CharField("card",max_length=100)
    cvv=models.CharField("cvv",max_length=100)
    amount=models.IntegerField("amount", default=0)
    

#bank_id,holder,card,cvv,exp,bal

