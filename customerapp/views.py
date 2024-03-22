from django.shortcuts import render,redirect
from django.http import HttpResponse
import mysql.connector
#from .models import Branch
import smtplib
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
from .models import *
from django.core.files.storage import FileSystemStorage
from datetime import date
#print(random.randint(0,9))

# Create your views here.
def index(request):
   # return HttpResponse("<h3>Welcome hnc</h3>")
   return render(request,"index.html")

def login_user(request):
    if request.method == 'POST':
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        
        )
        mycursor = conn.cursor()
        #retrive post details       
        
        uname=request.POST['uname']
        pwd=request.POST['u_password']     
        mycursor.execute("select * from registration where name='"+uname+"' and u_password='"+pwd+"'")
        result=mycursor.fetchone()
        if(result!=None):
            request.session['username'] = uname
            return redirect('menu_user')       
        else:
            return render(request,'login_user.html',{'status':'Invalid Credentials'})    
    else:
        return render(request,'login_user.html')


def login_admin(request):
    if request.method == 'POST':
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        )
        mycursor = conn.cursor()
        #retrive post details         
        username=request.POST['username']
        pwd=request.POST['password']
        mycursor.execute("select * from admin where username='"+username+"' and password='"+pwd+"'")
        result=mycursor.fetchone()
        if(result!=None):
            request.session['username'] = username
            return render(request, 'admin_dashboard.html', {'username':'username'})
            #redirect('studenthome')
        else:
            return render(request,'login_admin.html',{'status':'Invalid Credentials'})    
    else:
        return render(request,'login_admin.html')    

        
def registration(request):
    if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        ) 
        mycursor =conn.cursor()
        #retrive post details       
        name=request.POST['name']
        email=request.POST['email']
        phonenumber=request.POST['phoneNumber']
        address=request.POST['address']
        password=request.POST['u_password']     
        #branch=request.POST['branch']
        
        
        #address=request.POST['address']       
        mycursor.execute("insert into registration(name,email,phoneNumber,address,u_password) values('"+name+"','"+email+"','"+phonenumber+"','"+address+"','"+password+"')")
        conn.commit()
        return redirect('login_user')
    else:
        return render(request,'registration.html')

        
def menu(request):
   # return HttpResponse("<h3>Welcome hnc</h3>")
   return render(request,"menu.html")

def franchies(request):
   # return HttpResponse("<h3>Welcome hnc</h3>")
   return render(request,"franchies.html")

def contact(request):
    if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        ) 
        mycursor =conn.cursor()
        #retrive post details       
        name=request.POST['name']
        email=request.POST['email']
        phonenumber=request.POST['phonenumber']
        message=request.POST['message']
        #password=request.POST['password']     
        #branch=request.POST['branch']
        #address=request.POST['address']       
        mycursor.execute("insert into contact(name,email,phonenumber,message) values('"+name+"','"+email+"','"+str(phonenumber)+"','"+message+"')")
        conn.commit()
        return redirect('index')
    else:
        return render(request,'contact.html')


def about(request):
   # return HttpResponse("<h3>Welcome hnc</h3>")
   return render(request,"about.html")

'''def storelocator(request):
   # return HttpResponse("<h3>Welcome hnc</h3>")
   return render(request,"storelocator.html")'''

def admin_dashboard(request):
   # return HttpResponse("<h3>Welcome hnc</h3>")
   return render(request,"admin_dashboard.html")

def menu_admin(request):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        ) 
    mycursor = conn.cursor()
    #retrive post details       
    mycursor.execute("select * from item")
    result=mycursor.fetchall()
    item1=[]
    for x in result:
        items=item()
        items.item_id=x[0]
        items.item_image=x[1]
        items.item_name=x[2]
        items.item_desc=x[3]
        items.item_cost=x[4]
        item1.append(items)
    return render(request,'menu_admin.html',{'itemsinfo':item1})


def additem_admin(request):
    if request.method == 'POST' and request.FILES['myfile']:        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        ) 
        mycursor =conn.cursor()
        #retrive post details       
        #i_img=request.POST['item_image']
        iname=request.POST['item_name']
        idesc=request.POST['item_desc']
        icost=request.POST['item_cost']  
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename) 
        mycursor.execute("insert into item(item_image,item_name,item_desc,item_cost) values('"+filename+"','"+iname+"','"+idesc+"','"+icost+"')")
        conn.commit()
        return redirect('additem_admin')
    else:
        return render(request,"additem_admin.html")


def curdoperations(request):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studentdb"
    )
    mycursor = conns.cursor()
    #retrive post details       
    mycursor.execute("select * from items")
    result=mycursor.fetchall()
    items=[]
    for x in result:
        items=item()
        items.item_id=x[0]
        items.item_image=x[1]
        items.item_name=x[2]
        items.item_desc=x[3]
        items.item_cost=x[4]
        items.append(items)
    return render(request,'curdoperations.html',{'itemsinfo':s})


def message_admin(request):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        ) 
    mycursor = conn.cursor()
    #retrive post details       
    mycursor.execute("select * from messages")
    result=mycursor.fetchall()
    msg=[]
    messages=None
    for x in result:
        messages=msgs()
        messages.id=x[0]
        messages.username=x[1]
        messages.email=x[2]
        messages.message=x[3]
        msg.append(messages)
    return render(request,'message_admin.html',{'messageinfo':msg})


def total_admin(request):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        ) 
    mycursor = conn.cursor()
    #retrive post details       
    mycursor.execute("select * from paydetails")
    result=mycursor.fetchall()
    order1=[]
    for x in result:
        orders=order()
        orders.id=x[0]
        orders.name=x[1]
        orders.email=x[2]
        orders.phonenumber=x[3]
        orders.baddress=x[4]
        orders.saddress=x[5]
        orders.cardnumber=x[6]
        orders.cvv=x[7]
        orders.deliverystatus=x[8]
        order1.append(orders)
    return render(request,'total_admin.html',{'ordersinfo':order1})

def edit_menu(request,item_id):
   return render(request,"edit_menu.html")
def change_password(request):
   # return HttpResponse("<h3>Welcome hnc</h3>")
    if request.method == 'POST':
        if('uname' in request.session):
            usernmae=request.session['uname']

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hnc"
        )
        mycursor = conn.cursor()
        # retrive post details
        otp = request.POST['otp-code']
        npwd = request.POST['new-password']
        mycursor.execute("select email from forget where otp='"+otp+"'")
        result=mycursor.fetchone()
        em=result[0]
        #mail='thanveer@gmail.com'
        if(result!=None):
            mycursor = conn.cursor()
            mycursor.execute("UPDATE registration SET u_password='"+npwd+"' WHERE email='"+em+"'")
            conn.commit()
            return render(request, 'login_user.html', {'status':'success'})
            
        else:
            return render(request,'change_password.html',{'status':'invalid otp'})  
    else:
        return render(request,'change_password.html')

def forget_password(request): 
    if request.method == 'POST':
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hnc"
        )
        mycursor = conn.cursor()
        # retrive post details
        email = request.POST['user_email']
        #for otp in range(0,4):
        otp=str(random.randint(1000,9999))

        mycursor.execute("insert into forget(email,otp) values('"+email+"','"+otp+"')")
        conn.commit()
        #result = mycursor.fetchone()
        #pwd=str(result)
        #if (result != None):
            # SMTP server configuration
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'gaderohith2002@gmail.com'
# for App Password enable 2-step verification then u can create app password
        smtp_password = 'hcbswjqcnuzxblqj'

# Email content
        subject = 'Password recovery'
        body = 'This is a Password recovery email sent from kits.'+'One time Password '+ otp
        sender_email = 'gaderohith2002@gmail.com'
        receiver_email = email

# Create a message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            return render(request, 'change_password.html', {'status': 'Password sent to given mail ID'})
        
    else:
        return render(request, 'forget_password.html')


def menu_user(request):
    username=''
    if('username' not in request.session):
        return redirect("login_user")
    else:
        username=request.session['username']
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        ) 
    mycursor = conn.cursor()
    #retrive post details       
    mycursor.execute("select * from item")
    result=mycursor.fetchall()
    item1=[]
    for x in result:
        items=item()
        items.item_id=x[0]
        items.item_image=x[1] 
        items.item_name=x[2]
        items.item_desc=x[3]
        items.item_cost=x[4]
        item1.append(items)
    return render(request,'menu_user.html',{'itemsinfo':item1,'uname':username})

    
def messages_user(request):
    username=""
    if('username' not in request.session):
        return render(request,"messages_user.html")
    else:
        username=request.session['username']
        return render(request,"messages_user.html",{'username':username})
    if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        ) 
        mycursor =conn.cursor()
        #retrive post details       
        uname=request.POST['username'] 
        email=request.POST['email']
        msg=request.POST['message']      
        mycursor.execute("insert into messages(username,email,message) values('"+uname+"','"+email+"','"+msg+"')")
        conn.commit()
        return redirect('messages_user')
    else:
        return render(request,"messages_user.html")


def orders_user(request):
    username=""
    if('username' not in request.session):
        return render(request,"menu_user.html")
    else:
        username=request.session['username']
        #return render(request,"orders_user.html",{'uname':username})
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        ) 
    mycursor = conn.cursor()
    #retrive post details       
    mycursor.execute("select * from orders where username='"+username+"'")
    result=mycursor.fetchall()
    order1=[]
    for x in result:
        orders=order()
        orders.order_id=x[0]
        orders.username=x[1]
        #orders.cust_id=x[2]
        orders.ordered_date=x[2]
        orders.deliverystatus=x[3]
        orders.totalamount=x[4]
        order1.append(orders)
    return render(request,'orders_user.html',{'ordersinfo':order1,'username':username})


def updateprofile_user(request):
    username=''
    if('username' in request.session):
        username=request.session['username']
    if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        ) 
        mycursor =conn.cursor()
        #retrive post details       
        name=request.POST['name']
        email=request.POST['email']
        phonenumber=request.POST['phoneNumber']
        address=request.POST['address']
        mycursor.execute("update registration set name='"+name+"',email='"+email+"',address='"+address+"',phoneNumber='"+phonenumber+"' where name='"+username+"'")
        conn.commit()
        return redirect('menu_user')
    else:
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        )     
        mycursor =conn.cursor()   
        mycursor.execute("select * from registration where name='"+username+"'")
        result=mycursor.fetchall()
        users=[]
        for y in result:
            x=Profile()
            x.name=y[1]
            x.email=y[2]
            x.phonenumber=y[4]
            x.address=y[3]  
            users.append(x)          
        return render(request,"updateprofile_user.html",{'user':users[0],'username':username})

def ee(request, item_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        )
    mycursor =conn.cursor()   
    mycursor.execute("select * from item where item_id='"+item_id+"'")
    result=mycursor.fetchall()
    item1=[]
    for x in result:
        items=item()
        items.item_id=x[0]
        items.item_image=x[1] 
        items.item_name=x[2]
        items.item_desc=x[3]
        items.item_cost=x[4]
        item1.append(items)
    print(result)
    return render(request,"ee.html",{'i':item1})
def logout(request):
    del request.session['uname']
    request.session.modified = True
    return render(request, 'login_user.html')


def admin_logout(request):
    del request.session['username']
    request.session.modified = True
    return render(request, 'login_admin.html')

    
def checkout(request):
    if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        ) 
        username=''    
        if "username" in request.session:
            username= request.session['username']
        order_id=''    
        if "order_id" in request.session:
            order_id= request.session['order_id']
        mycursor =conn.cursor()
        #retrive post details       
        uname=request.POST['name'] 
        email=request.POST['email']
        phone=request.POST['phonenumber']
        #quantity=request.POST['quantity']
        baddress=request.POST['baddress'] 
        saddress=request.POST['saddress']
        cardnumber=request.POST['cardnumber']  
        cvv=request.POST['cvv']
        
        
        delivery=0
        mycursor.execute("insert into paydetails(name,email,phonenumber,baddress,saddress,cardnumber,cvv,deliverystatus,username,order_id) values('"+uname+"','"+email+"','"+str(phone)+"','"+baddress+"','"+saddress+"','"+cardnumber+"','"+cvv+"','"+str(delivery)+"','"+username+"','"+str(order_id)+"')")
        conn.commit()
        del request.session['cartlist']
        del request.session['order_id']
        return redirect("menu_user")
    else:
       return render(request,"checkout.html")
    
def checkout_main(request):
    #return render(request,"checkout.html")
    if request.method == 'POST':      
       
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        ) 
        mycursor =conn.cursor()      
        uname=request.POST['name'] 
        email=request.POST['email']
        phone=request.POST['phonenumber']
        baddress=request.POST['baddress'] 
        saddress=request.POST['saddress']
        cardnumber=request.POST['cardnumber']  
        cvv=request.POST['cvv']
        delivery=0
        mycursor.execute("insert into paydetails(name,email,phonenumber,baddress,saddress,cardnumber,cvv,deliverystatus) values('"+uname+"','"+email+"','"+str(phone)+"','"+baddress+"','"+saddress+"','"+cardnumber+"','"+cvv+"','"+str(delivery)+"')")
        conn.commit()
        return redirect("menu_user")
    else:
        x=request.POST['finalsub']
        print(x)  
        return render(request,"checkout.html");
def addtocart(request,item_id):
    
    x=[]
    if('cartlist' not in request.session):
        print('in if')
        x.append(item_id)
        request.session['cartlist']=x                
    else:
        print('in else')
        x=list(request.session['cartlist'])
        #print('in add cart ',x)
        if(item_id not in x):
            x.append(item_id) 
            request.session['cartlist']=x
        #print(x)
    return redirect('menu_user')
    


def remove(request,item_id):
    if "username" in request.session:
        uname= request.session['username']
        x=list(request.session['cartlist'])
        if(item_id in x):
            x.remove(item_id)
            request.session['cartlist']=x
        return redirect('see_cart')
    else:
        return redirect('login_user')
    
def see_cart(request):
    username=''    
    if "username" in request.session:
        username= request.session['username']
    if(request.method=='POST'):
        x=request.POST["finalsub"]
        data=x.split('@')
        print(data[0],":",data[1],":",data[2])
        itemids=data[0].split(',')
        quantities=data[1].split(',')
        total=data[2]
        # insert into orders
        #if request.method == 'POST':        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        ) 
        ordereddate = date.today()
        mycursor =conn.cursor()
        mycursor.execute("insert into orders(username,ordereddate,deliverystatus,totalamount) values (%s,%s,%s,%s)",(username,ordereddate,0,total))
        # end insert into orders
        # retrive order id of newly inserted
        conn.commit()
        mycursor.execute("select order_id from orders order by order_id desc limit 1")
        result= mycursor.fetchone()
        order_id = result[0]
        request.session["order_id"]=order_id
        # end retrive order id of newly inserted
       # loop through all items and insert into orderdetails based on order id
        for i in range(0,len(itemids)):
            mycursor.execute("insert into orderdetails(order_id,itemid,quantity) values (%s,%s,%s)",(order_id,itemids[i],quantities[i]))
        # end loop through all items and insert into orderdetails based on order id
        conn.commit()
        return redirect('checkout')
    else:
        print('in else')
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        ) 
        mycursor =conn.cursor()  
        p=[]
        if('cartlist' in request.session):
            p=list(request.session['cartlist'])
        d=[]
        if p:
            for aa in p:
                mycursor.execute("select * from item where item_id='"+str(aa)+"'")
                result=mycursor.fetchall()
                for row in result:
                    obj=item()
                    obj.item_id=str(row[0])
                    obj.item_image=row[1]
                    obj.item_name=row[2]
                    obj.item_desc=row[3]
                    obj.item_cost=row[4]                    
                    d.append(obj)                
        return render(request,"see_cart.html",{'itemsinfo':d,'uname':username})

'''def see_cart(request):
    if "username" in request.session:
        uname = request.session['username']
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hnc"
        )
        mycursor = conn.cursor()
        p = []
        print(request.POST['finalsub'])
        if 'cartlist' in request.session:
            p = list(request.session['cartlist'])
        if p:
            mycursor.execute("SELECT user_id FROM orders WHERE username='" + uname + "'")
            user_id = mycursor.fetchone()[0]
            d = []
            total_price = 0
            grand_total = 0
            shipping_charge = '10'
            finalsub = str(request.POST['finalsub'])
            print(finalsub)
            finalsubparts = finalsub.split('@')
            pids = finalsubparts[0]
            qs = finalsubparts[1]
            total=finalsubparts[2]
            stotal=str(total)
            print(pids, qs, total)
            qssplit = qs.split(',')
            u = 0
            today=datetime.now()
            print(today)
            b=str(today)
            print(b)
            mycursor.execute("INSERT INTO orders_list (cust_id, total_amount,order_date) VALUES (%s, %s,%s)", (cust_id, 0,b))
            mycursor.execute("SELECT LAST_INSERT_ID()")
            order_id = mycursor.fetchone()[0]
            for aa in pids:
                mycursor.execute("SELECT * FROM product_details WHERE product_id='" + str(aa) + "'")
                result = mycursor.fetchone()
                if result:
                    obj = Products()
                    obj.product_id = result[0]
                    obj.product_name = result[1]
                    obj.price = result[2]
                    obj.cust_id = cust_id
                    obj.order_id = order_id
                    obj.quantity = int(qssplit[u])
                    u += 1
                    obj.total_price = obj.price * obj.quantity
                    #shipping_charge = 10
                    grand_total = int(stotal) + int(shipping_charge)
                    #grand_total += obj.grand_total
                    print(grand_total)
                    d.append(obj)
                    # Insert the cart item with quantity
                    mycursor.execute("INSERT INTO order_details (cust_id,order_id, product_id, quantity, total) VALUES (%s, %s, %s, %s, %s)", (cust_id, order_id, obj.product_id, obj.quantity, obj.total_price ))
            #conn.commit()
            mycursor.execute("UPDATE orders_list SET total_amount=%s WHERE order_id=%s", (grand_total, order_id))
            conn.commit()
            del request.session['cartlist']
            context = {
                'pro': d,
                'total':total,
                'total_price': total_price,
                'shipping_charge': shipping_charge,
                'grand_total': grand_total
            }
            return render(request, 'checkout.html', context)
        else:
            return render(request, 'cart.html', {'pro': [], 'total_price': 0, 'grand_total':0})
        mycursor.execute(" SELECT order_id from orders_list order by order_id desc limit 1")
        order_id=mycursor.fetchone()[0]
        mycursor.execute("SELECT cust_id FROM customer_reg WHERE username='" + uname + "'")
        cust_id = mycursor.fetchone()[0]
        mycursor.execute(" SELECT ship_id from shippingaddress where cust_id='"+cust_id+"' order by ship_id desc limit 1")
        ship_id = mycursor.fetchone()[0]
        mycursor.execute("UPDATE orders_list SET ship_id=%s WHERE order_id=%s", (ship_id, order_id)) 
        conn.commit()          
    else:
        return render(request, 'cust_login.html')'''

def user_logout(request):
    try:
        del request.session['username']
        request.session.modified = True
        return render(request,'login_user.html') 
    except KeyError:
        return redirect('login_customer') 

def changetopending(request,id):
     conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        )
     mycursor = conn.cursor()    
     mycursor.execute("update orders set deliverystatus=0 where id='"+id+"'")
     conn.commit()
     return redirect('total_admin')

def changetodelivered(request,id):
     conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hnc"
        )
     mycursor = conn.cursor()      
     mycursor.execute("update orders set deliverystatus=1 where order_id='"+id+"'")
     #mycursor.execute("update paydetails set deliverystatus=1 where id='"+id+"'")
     conn.commit()
     return redirect('total_admin')

def delete_menu(request,item_id):        
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hnc"
    ) 
    mycursor =conn.cursor()
    mycursor.execute("delete from item where item_id='"+item_id+"'")
    conn.commit()
    return redirect("login_admin")

def removeitem(request,item_id):
    print('in remove item ',item_id)
    if('uname' not in request.session):
        return render(request,"login_user.html")
    else:
        username=request.session['uname']
        p=[]
        if('cartlist' in request.session):
            p=list(request.session['cartlist'])
            p.remove(item_id)
            request.session['cartlist']=p
    return redirect("see_cart")



