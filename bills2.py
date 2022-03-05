from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()

root.title("Burger king ordering system")

def cerrom():
    global w2
    w2.destroy() 
def errormessage(t,p):
    global w2
    w2=Toplevel()
    w2.title(str(t))
    (Label(w2,text=p)).grid(row=0,column=0,columnspan=2,padx=(15,15),pady=(20,50))
    (Button(w2,text="OK",command=cerrom)).grid(row=1,column=0,columnspan=2,pady=(10,10))

#REPETITION OF ------ LOGIN PAGE, MECHANISM ------ PRODUCTS, MECHANISM ------
def backbutton(tkindex,delframe):
    #tkindex is 0 for login page, 1 for product_categories page, 2 for products_list page
    delframe.grid_forget()
    h.grid_forget()
    h1.grid_forget()
    h2.grid_forget()
    if tkindex==1:
        products()
    elif tkindex==2:
        products()
    elif tkindex==3:
        listproduct(argscat)
def logout(delframe):
    delframe.grid_forget()
    h.grid_forget()
    h1.grid_forget()
    h2.grid_forget()
    start()

#ADD TO CART LOGIC ----- CART DETAILS - AND - BILLING
def addtocart(poids,names,costs):
    newc=sqlite3.connect('products.db')
    newcr=newc.cursor()
    newc.execute("""INSERT INTO incart VALUES(:puserp,:prnamep,:proidp,:prcostp)""",
                 {
                     'puserp':u1,
                     'prnamep':names,
                     'proidp':poids,
                     'prcostp':costs
                     })
    newc.commit()
    newc.close()
def updatedelivery():
    conn=sqlite3.connect('products.db')
    c=conn.cursor()
    c.execute("SELECT * from incart")
    recdeliv=c.fetchall()
    for i in recdeliv:
        if i[0]==str(u1):
            c.execute("""INSERT INTO paidorder VALUES(:popuser,:popname,:popcost,:popoid)""",
                      {
                           'popuser':i[0],
                           'popname':i[1],
                           'popcost':i[3],
                           'popoid':i[2]
                      })
            conn.commit()
    conn.close()           
def refreshorder():
    conn=sqlite3.connect('products.db')
    c=conn.cursor()
    c.execute("SELECT *,oid FROM incart")
    recforref=c.fetchall()
    updatedelivery()
    for i in recforref:
        if i[0]==str(u1):
            c.execute("DELETE FROM incart WHERE oid="+str(i[4]))
    conn.commit()
    conn.close()
def conforder(flag,sum1):
    errormessage("Your Total","Your Bill Total is "+str(sum1))
    refreshorder()
    cartdetails(3,frame12)
def cartdetails(tkindex,delframe):
    delframe.grid_forget()
    global h
    global h1
    global h2
    global frame12
    h.grid_forget()
    h1.grid_forget()
    h2.grid_forget()
    h=Button(root,text="<<--back",command=lambda: backbutton(tkindex,frame12))
    h.grid(row=0,column=0)
    h1=Button(root,text="LOG OUT",command=lambda: logout(frame12))
    h1.grid(row=0,column=2)
    h2=Button(root,text="My Cart",state=DISABLED)
    h2.grid(row=0,column=1)
    frame12=LabelFrame(root,text="MY ORDERS")
    frame12.grid(row=1,column=0,columnspan=3,padx=(15,15),pady=(20,40))
    newc=sqlite3.connect('products.db')
    newcr=newc.cursor()
    newcr.execute("SELECT * FROM incart")
    recordcart=newcr.fetchall()
    l=0
    m=0
    flag=-1
    total=0
    for i in recordcart:
        if str(i[0])==u1:
            flag=1
            m=0
            (Label(frame12,text=str(i[1]))).grid(row=l,column=m)
            m=m+1
            (Label(frame12,text="   ")).grid(row=l,column=m)
            m=m+1
            (Label(frame12,text=str(i[3]))).grid(row=l,column=m)
            total=total+int(i[3])
            m=m+1
            (Label(frame12,text="   ")).grid(row=l,column=m)
            m=m+1
            l=l+1
    l=l+1
    (Button(frame12,text="pay for the order",command=lambda: conforder(flag,total))).grid(row=l,column=0,columnspan=m+1,pady=(15,5))
    newc.commit()
    newc.close()

#PRODUCTS PAGE AND MECHANISM
def listproduct(categories):
    global argscat
    argscat=categories
    global frame200
    frame100.grid_forget()
    frame200=LabelFrame(root,text="Product List")
    frame200.grid(row=1,column=0,columnspan=3,padx=(15,15),pady=(20,40))
    global im_list
    global pname_list
    global pcost_list
    global duperec2
    global h
    global h1
    global h2
    h.grid_forget()
    h1.grid_forget()
    h2.grid_forget()
    h=Button(root,text="<<--back",command=lambda: backbutton(2,frame200))
    h.grid(row=0,column=0)
    h1=Button(root,text="LOG OUT",command=lambda: logout(frame200))
    h1.grid(row=0,column=2)
    h2=Button(root,text="My Cart",command=lambda: cartdetails(3,frame200))
    h2.grid(row=0,column=1)
    q=0
    im_list=[]
    pname_list=[]
    pcost_list=[]
    poid_list=[]
    tenn=sqlite3.connect('products.db')
    mouse=tenn.cursor()
    mouse.execute("SELECT *,oid FROM product")
    records=mouse.fetchall()
    tenn.commit()
    tenn.close()
    count=0
    for i in records:
        if str(i[0])==categories:
            img=ImageTk.PhotoImage(Image.open(str(i[2])))
            im_list=im_list+[img]
            pname_list=pname_list+[str(i[1])]
            pcost_list=pcost_list+[str(i[3])]
            poid_list=poid_list+[str(i[6])]
    for z in im_list:
        count=count+1
    for j in range(count):    
        r=0
        (Label(frame200,image=im_list[j])).grid(row=q,column=r,pady=(0,10))
        r=r+1
        (Label(frame200,text="   ")).grid(row=q,column=r)
        r=r+1
        (Label(frame200,text=pname_list[j])).grid(row=q,column=r,pady=(0,10))
        r=r+1
        (Label(frame200,text="   ")).grid(row=q,column=r)
        r=r+1
        (Label(frame200,text="$."+str(pcost_list[j]))).grid(row=q,column=r,pady=(0,10))
        r=r+1
        (Label(frame200,text="   ")).grid(row=q,column=r)
        r=r+1
        (Button(frame200,text="Add to Cart",command=lambda j=j: addtocart(str(poid_list[j]),pname_list[j],str(pcost_list[j])))).grid(row=q,column=r,pady=(10,50))
        r=r+1
        q=q+1
def products():
    global frame100
    global h1
    global h
    global h2
    global duperec2
    frame.grid_forget()
    frame100=LabelFrame(root,text="Product categories")
    frame100.grid(row=1,column=0,columnspan=3,padx=(15,15),pady=(20,40))
    h=Button(root,text="<<--back",state=DISABLED)
    h.grid(row=0,column=0)
    h1=Button(root,text="LOG OUT",command=lambda: logout(frame100))
    h1.grid(row=0,column=2)
    h2=Button(root,text="My Cart",command=lambda: cartdetails(1,frame100))
    h2.grid(row=0,column=1)
    (Label(frame100,text="Welcome to the products page")).grid(row=1,column=0,columnspan=3,pady=(15,15))
    tenn=sqlite3.connect('products.db')
    mouse=tenn.cursor()
    mouse.execute("SELECT * FROM product")
    records=mouse.fetchall()
    duperec=records
    duperec1=[]
    duperec2=[]
    for i in duperec:
        categ=i[0]
        duperec1.append(categ)
    for j in duperec1:
        if j not in duperec2:
            duperec2.append(j)
    incrm=2
    catbuttons=[]
    for i in duperec2:
        b=Button(frame100,text=i,command=lambda i=i: listproduct(i))
        catbuttons.append(b)
    for j in catbuttons:
        j.grid(row=incrm,column=0,columnspan=3,pady=(0,15))
        incrm=incrm+1
    tenn.commit()
    tenn.close()

#LOG IN INTERFACE AND MECHANISM
def login():
    global user1
    global password1
    global u1
    u1=user1.get()
    p1=password1.get()
    user1.delete(0,END)
    password1.delete(0,END)            
    conn=sqlite3.connect('users.db')
    c=conn.cursor()
    c.execute("SELECT *,oid FROM user")
    records=c.fetchall()
    ans=-1
    flag=-1
    for i in records:
        if i[3]==u1:
            ans=i[4]
            if ans==p1:
                flag=1
    if flag==1:
        products()
    else:
        errormessage("Log In Error","Wrong Credentials!!!")
def start():
    global user1
    global password1
    global frame
    frame=LabelFrame(root,text="Log In Frame",padx=50,pady=50)
    frame.grid(row=0,column=0,padx=100,pady=(30,100))
    p=Label(frame,text="Welcome to Burger king ordering system System")
    p.grid(row=0,column=0)
    p1=Label(frame,text="Username : ")
    p1.grid(row=1,column=0,pady=(25,0))
    user1=Entry(frame)
    user1.grid(row=1,column=1,pady=(25,0))
    p3=Label(frame,text="Password :")
    p3.grid(row=2,column=0,pady=(10,0))
    password1=Entry(frame)
    password1.grid(row=2,column=1,pady=(10,0))
    signin=Button(frame,text="Log In",command=login)
    signin.grid(row=3,column=0,columnspan=2,pady=(20,0))
    p2=Label(frame,text="Haven't created an account yet?")
    p2.grid(row=4,column=0,pady=(30,0))
    signup=Button(frame,text="Sign Up",command=sign)
    signup.grid(row=4,column=1,sticky="w",pady=(30,0))

conn=sqlite3.connect('users.db')
c=conn.cursor()
'''c.execute("""CREATE TABLE user(
               fname text,
               lname text,
               email text,
               username text,
               password text,
               repassword text,
               phone integer
          )""")'''
conn.commit()


#SIGN-IN PAGE AND BUTTON
def submit():
    conn=sqlite3.connect('users.db')
    c=conn.cursor()
    if e5.get()==e6.get():
        conn.execute("""INSERT INTO user VALUES(:fname,:lname,:email,:username,:password,:repassword,:phone)""",
              {
                   'fname':e.get(),
                   'lname':e1.get(),
                   'email':e3.get(),
                   'username':e4.get(),
                   'password':e5.get(),
                   'repassword':e6.get(),
                   'phone':e4.get()})
        conn.commit()
        conn.close()
    
        e.delete(0,END)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
    else:
        errormessage("Sign Up error","Passwords Mismatch!!!!")    
def sign():
    global e
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    win=Toplevel()
    f=LabelFrame(win,text="Sign Up Frame",padx=100,pady=100)
    f.grid(row=0,column=0,padx=50,pady=(30,50))
    (Label(f,text="First Name")).grid(row=0,column=0,sticky="w")
    (Label(f,text="Last Name")).grid(row=1,column=0,sticky="w",pady=(10,0))
    (Label(f,text="E-Mail ID")).grid(row=2,column=0,sticky="w",pady=(10,0))
    (Label(f,text="Phone Number")).grid(row=3,column=0,sticky="w",pady=(10,0))
    (Label(f,text="Username")).grid(row=4,column=0,sticky="w",pady=(10,0))
    (Label(f,text="Password")).grid(row=5,column=0,sticky="w",pady=(10,0))
    (Label(f,text="Re-enter Password")).grid(row=6,column=0,sticky="w",pady=(10,0))
    for i in range(7):
        if i==0:
            (Label(f,text=":")).grid(row=i,column=1,sticky="e")
        else:
            (Label(f,text=":")).grid(row=i,column=1,sticky="e",pady=(5,0))
    e=Entry(f)
    e.grid(row=0,column=2)
    e1=Entry(f)
    e1.grid(row=1,column=2)
    e2=Entry(f)
    e2.grid(row=2,column=2)
    e3=Entry(f)
    e3.grid(row=3,column=2)
    e4=Entry(f)
    e4.grid(row=4,column=2)
    e5=Entry(f)
    e5.grid(row=5,column=2)
    e6=Entry(f)
    e6.grid(row=6,column=2)
    sb=Button(f,text="create account!",command=submit)
    sb.grid(row=7,column=0,columnspan=3,pady=25)    

start()
conn.close()



root.mainloop()
