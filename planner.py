print("WELCOME TO WEEKLY PLANNER")
print()
name=input("Enter your name")
print("Welcome",name)
print()
print("You have selected the best platform for scheduling your day")
print()
print("Start planning your day")
print()
day=input("Enter today's day")
if day=="Monday":
    print("Quote of the day is BELIEVE IN YOURSELF")
if day=="Tuesday":
    print("Quote of the day is NEVER DOUBT YOUR WORTH")
if day=="Wednesday":
    print("Quote of the day is DREAM IT, WISH IT, DO IT")
if day=="Thursday":
    print("Quote of the day is BE GOOD TO PEOPLE FOR NO REASON")
if day=="Friday":
    print("Quote of the day is JUST KEEP GOING")
if day=="Saturday":
    print("Quote of the day is IF YOU WANT IT, WORK FOR IT")
if day=="Sunday":
    print("Quote of the day is WHEN YOU FOCUS ON THE GOOD THE GOOD GETS BETTER")

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

def updatea():
   f=open("D:\\timetable.dat","rb+")
   temp=int(input("enter serial no. of which you want to change"))
   flag=0
   try:
      while True:
         p=f.tell()
         s=pickle.load(f)
         if s[0]==temp:
            x=input("enter the work to be updated")
            s[4]=x
            f.seek(p)
            pickle.dump(s,f)
            flag=1
   except EOFError:
         if flag==0:
           print("record not found")
         else:
            print("Record updated")
   f.close()


def updateb():
   f=open("D:\\timetable.dat","rb+")
   temp=int(input("enter serial no. of which you want to change"))
   flag=0
   try:
      while True:
         p=f.tell()
         s=pickle.load(f)
         if s[0]==temp:
            x=input("enter the day to be updated")
            s[1]=x
            f.seek(p)
            pickle.dump(s,f)
            flag=1
   except EOFError:
         if flag==0:
           print("record not found")
         else:
            print("Record updated")
   f.close()


def updatec():
   f=open("D:\\timetable.dat","rb+")
   temp=int(input("enter serial no. of which you want to change"))
   flag=0
   try:
      while True:
         p=f.tell()
         s=pickle.load(f)
         if s[0]==temp:
            x=input("enter the date to be updated")
            s[2]=x
            f.seek(p)
            pickle.dump(s,f)
            flag=1
   except EOFError:
         if flag==0:
           print("record not found")
         else:
            print("Record updated")
   f.close()


def updated():
   f=open("D:\\timetable.dat","rb+")
   temp=int(input("enter serial no. of which you want to change"))
   flag=0
   try:
      while True:
         p=f.tell()
         s=pickle.load(f)
         if s[0]==temp:
            x=input("enter the time to be updated")
            s[3]=x
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
        p=input("enter what you want to update(work,day,date,time)")
        if p=="work":
                 updatea()
        if p=="day":
              updateb()
        if p=="date":
              updatec()
        if p=="time":
              updated()
    else:
        break
        f.close()

