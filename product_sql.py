from tkinter import *
from PIL import ImageTk,Image
import sqlite3

conn=sqlite3.connect('products.db')
cur=conn.cursor()
'''cur.execute("""CREATE TABLE product(
                pcategory text,
                pname text,
                pimage text,
                pcost decimal,
                pavailable integer,
                totalgoods integer
              )""")'''
'''cur.execute("""CREATE TABLE incart(
                puserp text,
                prnamep text,
                proidp integer,
                prcostp decimal
                    )""")'''
'''cur.execute("""CREATE TABLE paidorder(
                popuser text,
                popname text,
                popcost decimal,
                popoid integer
             )""")'''
conn.commit()
conn.close()

win3=Tk()

f3=LabelFrame(win3,text="Edit Product Details")
f3.grid(row=0,column=0,padx=(30,30),pady=(30,60))

def submit():
    global cat
    global name
    global img
    global cost
    global avl
    global qun
    conn=sqlite3.connect('products.db')
    cur=conn.cursor()
    conn.execute("""INSERT INTO product VALUES(:cat,:name,:img,:cost,:avl,:qun)""",
                 {
                     'cat':cat.get(),
                     'name':name.get(),
                     'img':img.get(),
                     'cost':cost.get(),
                     'avl':avl.get(),
                     'qun':qun.get()
                     })
    conn.commit()
    conn.close()
    cat.delete(0,END)
    name.delete(0,END)
    img.delete(0,END)
    cost.delete(0,END)
    avl.delete(0,END)
    qun.delete(0,END)

def addp():
    global bf
    global cat
    global name
    global img
    global avl
    global qun
    global cost
    bf.grid_forget()
    bsec.grid_forget()
    bth.grid_forget()
    bfr.grid_forget()
    (Label(f3,text="category")).grid(row=0,column=0,sticky="w",pady=(10,0))
    (Label(f3,text="Name")).grid(row=1,column=0,sticky="w",pady=(10,0))
    (Label(f3,text="Image Name")).grid(row=2,column=0,sticky="w",pady=(10,0))
    (Label(f3,text="Cost")).grid(row=3,column=0,sticky="w",pady=(10,0))
    (Label(f3,text="Availability (bool)")).grid(row=4,column=0,sticky="w",pady=(10,0))
    (Label(f3,text="Quantity Available")).grid(row=5,column=0,sticky="w",pady=(10,0))
    cat=Entry(f3)
    name=Entry(f3)
    img=Entry(f3)
    cost=Entry(f3)
    avl=Entry(f3)
    qun=Entry(f3)
    for h in range(6):
        (Label(f3,text=":")).grid(row=h,column=1,pady=(5,0))
    cat.grid(row=0,column=2)
    name.grid(row=1,column=2)
    img.grid(row=2,column=2)
    cost.grid(row=3,column=2)
    avl.grid(row=4,column=2)
    qun.grid(row=5,column=2)
    bs=Button(f3,text="submit to database",command=submit)
    bs.grid(row=6,column=0,columnspan=3)

def deld():
    global de
    global l
    conn=sqlite3.connect('products.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM product WHERE oid="+de.get())
    de.delete(0,END)
    cur.execute("SELECT *,oid FROM product")
    records=cur.fetchall()
    for i in records:
        (Label(f3,text=str(i))).grid(row=l+2,column=0,columnspan=3)
        l=l+1
    conn.commit()
    conn.close()

def remd():
    global de
    global l
    k=1
    conn=sqlite3.connect('products.db')
    cur=conn.cursor()
    cur.execute("SELECT *,oid FROM product")
    records=cur.fetchall()
    for i in records:
        (Label(f3,text=str(i))).grid(row=k,column=0,columnspan=3)
        k=k+1
    l=k+1
    (Label(f3,text="Enter_oid")).grid(row=l,column=0,sticky="w")
    (Label(f3,text=":")).grid(row=l,column=1)
    de=Entry(f3)
    de.grid(row=l,column=2)
    brem=Button(f3,text="Remove from database",command=deld)
    brem.grid(row=l+1,column=0,columnspan=3)
    conn.commit()
    conn.close()
    #return

def delp():
    #global c
    bf.grid_forget()
    bsec.grid_forget()
    bth.grid_forget()
    bfr.grid_forget()
    #(Label(f3,text="category")).grid(row=0,column=0,sticky="w",pady=(10,0))
    #(Label(f3,text="Name")).grid(row=1,column=0,sticky="w",pady=(10,0))
    #(Label(f3,text="Image Name")).grid(row=2,column=0,sticky="w",pady=(10,0))
    #(Label(f3,text="Cost")).grid(row=3,column=0,sticky="w",pady=(10,0))
    #(Label(f3,text="Availability (bool)")).grid(row=4,column=0,sticky="w",pady=(10,0))
    #(Label(f3,text="Quantity Available")).grid(row=5,column=0,sticky="w",pady=(10,0))
    #c=Entry(f3)
    #n=Entry(f3)
    #i=Entry(f3)
    #co=Entry(f3)
    #av=Entry(f3)
    #qn=Entry(f3)
    #for h in range(1):
     #   (Label(f3,text=":")).grid(row=h,column=1,pady=(5,0))
    #c.grid(row=0,column=2)
    #n.grid(row=1,column=2)
    #i.grid(row=2,column=2)
    #co.grid(row=3,column=2)
    #av.grid(row=4,column=2)
    #qn.grid(row=5,column=2)
    bs=Button(f3,text="display from database",command=remd)
    bs.grid(row=0,column=0,columnspan=3)

def displayit():
    bf.grid_forget()
    bsec.grid_forget()
    bth.grid_forget()
    bfr.grid_forget()
    k=0
    conn=sqlite3.connect('products.db')
    cur=conn.cursor()
    cur.execute("SELECT *,oid FROM product")
    records=cur.fetchall()
    for i in records:
        (Label(f3,text=str(i))).grid(row=k,column=0,columnspan=3)
        k=k+1

def paidord():
    bf.grid_forget()
    bsec.grid_forget()
    bth.grid_forget()
    bfr.grid_forget()
    k=0
    conn=sqlite3.connect('products.db')
    cur=conn.cursor()
    cur.execute("SELECT *,oid FROM paidorder")
    records=cur.fetchall()
    for i in records:
        (Label(f3,text=str(i))).grid(row=k,column=0,columnspan=3)
        k=k+1
    
bf=Button(f3,text="Add a Product",command=addp)
bf.grid(row=0,column=0,pady=(0,10))
bsec=Button(f3,text="Remove a Product",command=delp)
bsec.grid(row=1,column=0,pady=(0,10))
bth=Button(f3,text="Display Products",command=displayit)
bth.grid(row=2,column=0,pady=(0,10))
bfr=Button(f3,text="Paid Orders",command=paidord)
bfr.grid(row=3,column=0,pady=(0,10))

win3.mainloop()

