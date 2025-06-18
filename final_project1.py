from tkinter import *
from tkinter import messagebox
import webbrowser
import pyautogui
import time
import pyttsx3
import speech_recognition as sr
from PIL import ImageTk,Image

d={' ':-1,'a': 0, 'b': 1, 'c': 2, 'd': 3, 'A': 4, 'B': 5, 'C': 6, 'D': 7, 'e': 8, 'f': 9, 'g': 10, 'h': 11, 'E': 12, 'F': 13, 'G': 14,
   'H': 15, 'i': 16, 'j': 17, 'k': 18, 'l': 19, 'I': 20, 'J': 21, 'K': 22, 'L': 23, 'm': 24, 'n': 25, 'o': 26, 'p': 27, 'M': 28,
   'N': 29, 'O': 30, 'P': 31, 'q': 32, 'r': 33, 's': 34, 't': 35, 'Q': 36, 'R': 37, 'S': 38, 'T': 39, 'u': 40, 'v': 41, 'w': 42,
    'x': 43, 'U': 44, 'V': 45, 'W': 46, 'X': 47, 'y': 48, 'z': 49, 'Y': 50, 'Z':51,'0':52,'1':53,'2':54,'3':55,'4':56,'5':57,
    '6':58,'7':59,'8':60,'9':61,'$':62,'&':63,'@':64,'#':65,'%':66,'^':67,'!':68,'~':69,'`':70,'*':71,'+':72,'-':73,'/':74,'.':75,
    ',':76,'?':77,'=':78,'<':79,'>':80}

def tlg1():
    person_name =msgEntry.get()
    msg= MessageEntry.get()
    webbrowser.open('https://web.telegram.org/')
    time.sleep(10)
    print(pyautogui.position())
    x=list(pyautogui.position())

    #click on searchbar
    pyautogui.click(x[0],x[1])
    pyautogui.typewrite((person_name))

    #click on that person
    time.sleep(5)
    pyautogui.click(355,388)
    time.sleep(5)
    pyautogui.typewrite((msg))

    #click on send button
    time.sleep(2)
    pyautogui.click(1633,977)

def mail1():
    person_name =msgEntry.get()
    msg= MessageEntry.get()
    webbrowser.open('https://mail.google.com/')
    time.sleep(10)
    print(pyautogui.position())

    #click on searchbar
    pyautogui.click(68,220)
    time.sleep(5)
    pyautogui.click(1200,427)
    pyautogui.typewrite((person_name))

    #click on the subject
    time.sleep(3)
    pyautogui.click(1200,479)
    pyautogui.typewrite("")
    #click on that person

    time.sleep(5)
    pyautogui.click(1200,534)
    pyautogui.typewrite(msg)

    #click on send button
    time.sleep(2)
    pyautogui.click(1200,1000)

def whatapp1():
    person_name =msgEntry.get()
    msg= MessageEntry.get()
    webbrowser.open('https://web.whatsapp.com/')

    time.sleep(10)
    print(pyautogui.position())
    x=list(pyautogui.position())

    #click on searchbar
    pyautogui.click(x[0],x[1])
    pyautogui.typewrite((person_name))

    time.sleep(5)
    #click on that personmou
    x=list(pyautogui.position())
    pyautogui.click(263,381)

    time.sleep(5)

    pyautogui.typewrite(msg)

    time.sleep(2)
    #click on send button
    x=list(pyautogui.position())
    pyautogui.click(1842,965)



def recordtext():
    r=sr.Recognizer()
    messagebox.showwarning('warning:',"start recording")

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something...")
        audio= r.listen(source)
        try:
            t=r.recognize_google(audio)
            print("You have said: \n" +t)
            MessageEntry.delete(0,END)                                
            MessageEntry.insert(0,t)

        except Exception as e:
            print("Error:"+str(e))
            messagebox.showwarning('warning:',"Sorry..run again...")

def play():
    engine = pyttsx3.init()
    text=MessageEntry.get()

    engine.say(text)
    engine.runAndWait()
    engine.stop()
    


def click(*args):
    keyEntry.delete(0,'end')

def leave(*args):
    n=int(rotEntry.get())
    t="Enter a string with length "+str(n)+"and whose each character greater than '"+max(MessageEntry.get())+"'"
    keyEntry.insert(0,t)
    root.focus()

def makekey(mch,n):
    pr="Enter a string with length "+str(n)+" and whose each character greater than '"+mch+"'"
    while(1):
        k=keyEntry.get()
        if(len(k)!=n):
            continue
        else:
            for i in k:
                if(d[i]<d[mch]):
                    break
            else:
                messagebox.showwarning('NOTE:',"success")
                return(k)
            continue


def complement(key,pt): 
    new_text=''  
    i=0 
    for j in pt:
        p=d[j]
        m=d[key[i%len(key)]]-p
        for cmp in d.keys():
            if(d[cmp]==m):
                new_text=new_text+cmp
                break
        i=i+1    
    return(new_text) 

def sum(key):
    s=0  
    for i in key:
        s=s+d[i]
    return(s)

def rotation(key,com_text):
    s=sum(key)
    n=len(key)
    str=com_text
    if (s%2==0):
        left_first=str[0:n]
        left_remains=str[n:]
        msg=left_remains+left_first
    else:
        right_remains=str[-n:]
        right_first=str[0:-n]
        msg=right_remains+right_first
    return(msg)


def encrypt27():
    n=int(rotEntry.get())
    key=keyEntry.get()
    pt=MessageEntry.get()
    mch=max(pt)
    print(mch)
    print("key=",key)
    com_text=complement(key,pt)
    print("complement text:",com_text)
    cipher_text=rotation(key,com_text)
    print("Cipher text:",cipher_text)
    MessageEntry.delete(0,END)                                
    MessageEntry.insert(0,cipher_text)


def rotation_back(key,ct):
    s=sum(key)
    n=len(key)
    str=ct
    if (s%2==0):
        right_remains=str[-n:]
        right_first=str[0:-n]
        msg=right_remains+right_first
    else:
        left_first=str[0:n]
        left_remains=str[n:]
        msg=left_remains+left_first
    return(msg)

def complement_back(key,ciphertext_back): 
    new_text1=''  
    i=0 
    for j in ciphertext_back:
        p=d[j]
        m=d[key[i%len(key)]]-p
        for cmp in d.keys():
            if(d[cmp]==m):
                new_text1=new_text1-cmp
                break
        i=i+1
    return(new_text1)                


def decrypt30():
    key=keyEntry.get()
    ct=MessageEntry.get()
    ciphertext_back=rotation_back(key,ct)
    print("cipher text decryption:",ciphertext_back)
    com_text1=complement(key,ciphertext_back)
    print("complement text decryption:",com_text1)
    MessageEntry.delete(0,END)                                
    MessageEntry.insert(0,com_text1)


root=Tk()
root.title("Project Design")
root.geometry("1250x750")

image_0=Image.open("E:\\Project\\background.jpg")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.place(x=0,y=0)

Wp_img=PhotoImage(file="E:\\Project\\whatsapp.png")
gm_img=PhotoImage(file="E:\\Project\\gmail.png")
te_img=PhotoImage(file="E:\\Project\\telegram.png")
speak_img=PhotoImage(file="E:\\Project\\speaker-icon-png.png")
record_img=PhotoImage(file="E:\\Project\\record.png")
key_img=PhotoImage(file="E:\\Project\\key.png")
msg_img=PhotoImage(file="E:\\Project\\message-icon-png-1.png")
lock_img=PhotoImage(file="E:\\Project\\lock.png")
unlock_img=PhotoImage(file="E:\\Project\\unlock.png")
user_img=PhotoImage(file="E:\\Project\\user.png")
length_img=PhotoImage(file="E:\\Project\\length.png")
privacy_img=PhotoImage(file="E:\\Project\\privacy-logo.png")



Label(root,text="Secure Chatting",font="arial 25",image=privacy_img,compound='left',borderwidth=0).pack(pady=50)

Label(text="Message:",font=("Helvetica,16"),image=msg_img,compound='left',borderwidth=0).place(x=250,y=145)
Label(text="Enter length of key:",font=("Helvetica,16"),image=length_img,compound='left',borderwidth=0).place(x=250,y=185)
Label(text="Key:",font=("Helvetica,16"),image=key_img,compound='left',borderwidth=0).place(x=270,y=235)
Label(text="User Id:",font=("Helvetica,16"),image=user_img,compound='left',borderwidth=0).place(x=270,y=490)

MessageValue=StringVar()
keyValue=StringVar()
rotValue=IntVar()
MsgValue=StringVar()

MessageEntry=Entry(root,textvariable=MessageValue,width=35,bd=3,font=18)
rotEntry=Entry(root,textvariable=rotValue,width=15,bd=3,font=18)
keyEntry=Entry(root,textvariable=keyValue,width=70,bd=3,font=18)
msgEntry=Entry(root,textvariable=MsgValue,width=35,bd=3,font=18)

keyEntry.bind("<Button-1>",click)
rotEntry.bind("<Leave>",leave)

MessageEntry.place(x=400,y=150)
Button(text="Listen",font=("Helvetica,35"),image=record_img,compound='top',borderwidth=0,command=recordtext).place(x=800,y=125)
Button(text="Play",font=("Helvetica,35"),image=speak_img,compound='top',borderwidth=0,command=play).place(x=900,y=123)

rotEntry.place(x=490,y=200)
keyEntry.place(x=400,y=250)
msgEntry.place(x=400,y=500)
    
Label(image=lock_img).place(x=440,y=325)
Label(image=unlock_img).place(x=885,y=325)
Button(text="ENCRYPT",font=20,width=11,height=2,fg="white",bg="#ed3833",borderwidth=0,command=encrypt27).place(x=400,y=400)
Button(text="DECRYPT",font=20,width=11,height=2,fg="white",bg="#00bd56",borderwidth=0,command=decrypt30).place(x=850,y=400)



gm_btn=Button(text="Email",font=("Helvetica,35"),image=gm_img,compound='top',borderwidth=0,command=mail1).place(x=400,y=550)
Wp_btn=Button(text='Whatsapp',font=("Helvetica,32"),image=Wp_img,compound='top',borderwidth=0,command=whatapp1).place(x=600,y=550)
te_btn=Button(text="Telegram",font=("Helvetica,32"),image=te_img,compound='top',borderwidth=0,command=tlg1).place(x=800,y=550)
root.mainloop()