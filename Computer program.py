#project
import pickle

def create():
   f=open("D:\\timetable.dat","wb")
   c="y"
   while c=="y":
     Sr=int(input("enter serial no."))
     d=input("enter day")
     l=input("enter date")
     t=input("Enter time from-to")
     todo=input("enter what work is to be done")
     l=[Sr,d,l,t,todo]
     pickle.dump(l,f)
     c=input("y/n?")
   f.close()

def read():
    f=open("D:\\timetable.dat","rb")
    try:
      while True:
        s=pickle.load(f)
        print(s)
    except EOFError:
     f.close()

def search():
    f=open("D:\\timetable.dat","rb")
    temp=int(input("enter the no. to be searched"))
    try:
        while True:
            s=pickle.load(f)
            if temp==s[0]:
                print(s)
    except EOFError:
        f.close()

def append():
    f=open("D:\\timetable.dat","ab")
    c="y"
    while c=="y":
     Sr=int(input("enter serial no."))
     d=input("enter day")
     l=input("enter date")
     t=input("enter time from-to")
     todo=input("enter what work is to be done")
     l=[Sr,d,l,t,todo]
     pickle.dump(l,f)
     c=input("y/n?")
    f.close()

def update():
   f=open("D:\\timetable.dat","rb+")
   temp=int(input("enter serial no. of which you want to change"))
   flag=0
   try:
      while True:
         p=f.tell()
         s=pickle.load(f)
         if s[0]==temp:
            x=input("enter the work to be updated")
            s[4]==x
            f.seek(p)
            pickle.dump(s,f)
            flag=1
   except EOFError:
         if flag==0:
           print("record not found")
         else:
            print("Record updated")
   f.close()

while True:
    print("1.Create timetable")
    print("2.Read all data")
    print("3.Search")
    print("4.add record")
    print("5.update record")
    print("6.exit")

    n=int(input("enter choice"))
    if n==1:
        create()
    elif n==2:
        read()
    elif n==3:
        search()
    elif n==4:
        append()
    elif n==5:
        update()
    else:
       f.close()
