import datetime
import os
#this script I programmed in 202à that the first project programmin with python
while True:
  o= input ("""
                ©yousssef
                   2020
00000000000000000000000000000000000000
           <===hello========>        0
           <===calendar=====>        0
           <===calculator===>        0
           <===calc=========>        0
           <===questions====>        0
           <===help=========>        0
           <===exit=========>        0
00000000000000000000000000000000000000
----> """)
  if o == "calculator" :
    k = input ("""calculator:
<<<math>>>
_______
+     |
------|
-     |
------|
/     |
------|
*     |
------|
:""")
    b1= int(input("fist number: "))
    b2= int(input("second number: "))
    if k == "+" :
       print ('{} + {} ='.format(b1,b2))
       print (b1 + b2 )
    elif k == "-":
       print ('{} - {} ='.format(b1,b2))
       print (b1 - b2)
    elif k == "*":
       print ('{} * {} ='.format(b1,b2))
       print (b1 * b2)
    elif k == "/":
       print ('{} ÷ {} ='.format(b1,b2))
       print (b1 / b2)
    else:
       print ("🙈🙉🙊")
  elif o == "calc":
   u = input("""
[1]
[2]
:""")
   if u == "1":
       b1= int(input("fist number: "))
       b2= int(input("second number: "))
       b3= int(input("Third number:"))
       b4= int(input("fourth number:"))
       p = input("""
1{math=000110001}
o = x+y*z-a
h = x-y*z/a
k = x*y+z/a
l = x/y*z+a
:""")
       if p == "o":
        print ('{}+{}*{}-{}= '.format(b1,b2,b3,b4))
        print (b1+b2*b3-b4)
       elif p == "h":
        print ('{}-{}*{}/{}= '.format(b1,b2,b3,b4))
        print (b1-b2*b3/b4)
       elif p == "k":
        print ('{}*{}+{}/{}= '.format(b1,b2,b3,b4))
        print (b1*b2+b3/b4)
       elif p == "l":
        print ('{}/{}*{}+{}= '.format(b1,b2,b3,b4))
        print (b1/b2*b3+b4)
       else:
        print ("b9a tchof mzyan alhlof")
   elif u =="2":
       b1= int(input("fist number: "))
       b2= int(input("second number: "))
       b3= int(input("Third number:"))
       j= input("""
1 = x*y/a
2 = x+y*a
3 = x-y/a
4 = x/y+a
5 = x/y-a
:""")
       if j == "1":
        print ('{}*{}/{}= '.format(b1,b2,b3))
        print (b1*b2/b3)
       elif j == "2":
        print ('{}+{}*{}= '.format(b1,b2,b3))
        print (b1+b2*b3)
       elif j == "3":
        print ('{}-{}/{}= '.format(b1,b2,b3))
        print (b1-b2/b3)
       elif j == "4":
        print ('{}/{}+{}= '.format(b1,b2,b3))
        print (b1/b2+b3)
       elif j == "5":
        print ('{}/{}-{}= '.format(b1,b2,b3))
        print (b1/b2-b3)
       else:
        print ("b9a tchof mzyan alhlof")
  elif o =="calendar":
       import calendar
       calendar.prcal(2021)
  elif o =="exit":
     exit()
  elif o =="questions":
       u = input("""
[  1  ]
[  2  ]
[  3  ]
[  4  ]
:""")
       if u == "1":
        nam= "plays"
        nam= input('he"....."the piano(play):')
        print ('he {} the piano'.format(nam))
        if nam =="plays":
          print ("👍👍👍👍")
        else:
           print ("hhhhhh b4l")
       elif u =="2":
        nam9= "are"
        nam9= input("They....professors(to be):")
        print ('they {} professors'.format(nam9))
        if nam9 =="are":
          print ("gooooood")
        else:
           print ("mj4yol")
       elif u =="3":
        i = input('i')
        print ('i {}'.format(i))
        if i =="i am":
          print ("👏👏👏👏")
        else:
           print ("hmar 🐴")
       elif u =="4":
        h = "0.95"
        h = input("95%=")
        print ('95%= {}'.format(h))
        if h == "0.95":
           print ("👏👏👏👏")
        else:
           print ("kasol hhh")
       else:
        print ("chof mzyan alhlof")
  elif o =="help":
      print ("""
hello my name is youssef my project is hello world hhhhhh??? 
""")
  elif o =="hello":
       print ("what's you name ?")
       print ("::::::::::::::::::::")
       name = input('my name ')
       print ("::::::::::::::::::::")
       print ("how old are you ?")
       print ("::::::::::::::::::::")
       name1= int(input("I am "))
       print ("-------------------------")
       print ("where are you from?")
       print ("-------------------------")
       name2= input("I am from ")
       print ("-------------------------")
       print ("What is your job ?")
       print ("-------------------------")
       name3= input('my job is ')
       print ("-------------------------")
       print ("What is the father name ?")
       print ("-------------------------")
       name4= input("Name of father is ")
       print ("========================")
       print ("What is the mother name ?")
       print ("========================")
       name5= input("Name of mother is ")
       print ("========================")
       print ("Where do you live ?")
       print ("========================")
       name6= input("I live in ")
       print ("========================")
       print ("Are you male or female ?")
       print ("========================")
       nam7= input("I am ")
       print ("========================")
       print ("Are you a man or a  boy or woman or a girl ?")
       print ("========================")
       nam8= input("I am ")
       print ("========================")
       print ("")
       print ("")
       print ("")
       print ("")
       print ("")
       x= datetime.datetime.now()
       print ("       identity card     ")
       print ("|>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
       print ('|username: {}           '.format(name))
       print ("|----------------------------")
       print ('|age: {} year old               '.format(name1))
       print ("|----------------------------")
       print ("|country : {} ".format(name2))
       print ("|----------------------------")
       print ("|work: {}".format(name3))
       print ("|----------------------------")
       print ("|Name mother: {}".format(name4))
       print ("|----------------------------")
       print ("|Name father: {}".format(name5))
       print ("|----------------------------")
       print ("|he lives in : {}".format(name6))
       print ("|----------------------------")
       print ("|time: ")
       print ("|----------------------------")
       print ("|",x)
       print ("|----------------------------")
       print ("|{},{}".format(nam7,nam8))
       print ("|>>>>>>>>>>2729910>>>>>>>>>>>")
  else:
    print ("hlof")
