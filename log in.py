import tkinter as tk
root=tk.Tk()
root.geometry("460x150")
root.title('LOGIN')
root.configure(bg='lavender')

def close():
    root2.destroy()

def register(): 
    username_text = nama.get()
    password_text = sandi.get()
    listi=[]
    a='0123456789'
    b='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    x=0
    y=0
    z=0
    cek=True
    for i in username_text:
        if i in a:
            x+=1
        elif i in b:
            y+=1
        else:
            z+=1
    if x==0 and y==0:
        cek=False
    elif x == 0 and y != 0:
        cek=False
    elif x != 0 and y == 0:
        cek=False
    else:
        if z != 0:
            cek=False
    cekcek=True
    
    if cekcek==True and cek==False:
        label_3=tk.Label(root,text='Username harus kombinasi angka dan huruf', fg='red',bg='lavender')
        label_3.grid(column=2,row=1)
    elif cekcek == True:
        label_4=tk.Label(root,bg='lavender',width=35)
        label_4.grid(column=2,row=1)
  
    for i in (password_text):
        listi.append(i)
    if len(listi) >= 8:
        label_5=tk.Label(root,bg='lavender',width=35)
        label_5.grid(column=2,row=2)
    else:
        label_6=tk.Label(root,text='Password minimal berisi 8 karakter', fg='red',bg='lavender')
        label_6.grid(column=2,row=2)

    if cekcek == True and len(listi) >= 8:
        global root2
        root2=tk.Toplevel(root)
        root2.geometry('250x290')
        root2.title('success')
        label_7=tk.Label(root2, text='BERHASIL',font='Times 10')
        label_7.pack()
        label_8=tk.Label(root2,text=nama.get())
        label_8.pack()
        label_9=tk.Label(root2,text=sandi.get())
        label_9.pack()
        button=tk.Button(root2, text='OK',bg="snow3",fg="white",width=5,command=close).place(x=55,y=80)

    
    
label_0=tk.Label(root, text=' ',bg='lavender')
label_0.grid(column=0,row=0)

label_1=tk.Label(root, text='Username',bg='lavender',font='Times')
label_1.grid(column=0,row=1)
nama=tk.StringVar()
username=tk.Entry(root, width=20,textvariable=nama)
username.grid(column=1,row=1)

label_2=tk.Label(root, text='Password',bg='lavender',font='Times')
label_2.grid(column=0,row=2)
sandi=tk.StringVar()
password=tk.Entry(root, width=20,textvariable=sandi,show="*")
password.grid(column=1,row=2)
           
login=tk.Button(root, text='Login',width=6,bg='snow3',command=register)
login.grid(column=1,row=4)

root.mainloop()


    
