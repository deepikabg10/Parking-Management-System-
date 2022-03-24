import tkinter as t
root=t.Tk()
root.title("Simple Calculator")
e1=t.Entry(root,borderwidth=5,width=50)
e1.grid(columnspan=4)
def click(inp):
    cur=e1.get()
    global l
    l=len(cur)
    e1.delete(first=0,last=l)
    fin=cur+str(inp)
    e1.insert(0,fin)
def clear():
    e1.get()
    leng=len(e1.get())
    e1.delete(first=0,last=leng)
def add():
    global fnum
    global flag
    fnum=float(e1.get())
    leng=len(e1.get())
    e1.delete(0,leng)
    flag=1
def diff():
    global fnum
    global flag
    fnum=float(e1.get())
    leng=len(e1.get())
    e1.delete(0,leng)
    flag=2
def pro():
    global fnum
    global flag
    fnum=float(e1.get())
    leng=len(e1.get())
    e1.delete(0,leng)
    flag=3
def div():
    global fnum
    global flag
    fnum=float(e1.get())
    leng=len(e1.get())
    e1.delete(0,leng)
    flag=4
def equal():
    global final
    b=e1.get()
    leng=len(b)
    snum=float(b)
    if(flag==1):
        final=fnum+snum
    elif(flag==2):
        final=fnum-snum
    elif(flag==3):
        final=fnum*snum
    elif(flag==4):
        if snum==0:
            final="ERROR"
        else:
            final=fnum/snum
    e1.delete(0,leng)
    e1.insert(0,final)
b0=t.Button(root,text="0",padx=30,pady=30,command=lambda: click("0")).grid(row=4,column=2)
b1=t.Button(root,text="1",padx=30,pady=30,command=lambda: click("1")).grid(row=1,column=0)
b2=t.Button(root,text="2",padx=30,pady=30,command=lambda: click("2")).grid(row=1,column=1)
b3=t.Button(root,text="3",padx=30,pady=30,command=lambda: click("3")).grid(row=1,column=2)
b4=t.Button(root,text="4",padx=30,pady=30,command=lambda: click("4")).grid(row=2,column=0)
b5=t.Button(root,text="5",padx=30,pady=30,command=lambda: click("5")).grid(row=2,column=1)
b6=t.Button(root,text="6",padx=30,pady=30,command=lambda: click("6")).grid(row=2,column=2)
b7=t.Button(root,text="7",padx=30,pady=30,command=lambda: click("7")).grid(row=3,column=0)
b8=t.Button(root,text="8",padx=30,pady=30,command=lambda: click("8")).grid(row=3,column=1)
b9=t.Button(root,text="9",padx=30,pady=30,command=lambda: click("9")).grid(row=3,column=2)
bclear=t.Button(root,text="clear",padx=20,pady=30,command=clear).grid(row=4,column=3)
bsum=t.Button(root,text="+",padx=30,pady=30,command=add).grid(row=4,column=0)
bdiff=t.Button(root,text="-",padx=30,pady=30,command=diff).grid(row=4,column=1)
bpro=t.Button(root,text="*",padx=30,pady=30,command=pro).grid(row=1,column=3)
bdiv=t.Button(root,text="/",padx=30,pady=30,command=div).grid(row=2,column=3)
beq=t.Button(root,text="=",padx=30,pady=30,command=equal).grid(row=3,column=3)
root.mainloop()
