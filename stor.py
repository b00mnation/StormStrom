#!/usr/bin/env python2.7
#
#
#

import os
import sys
d3=os.system("curl http://ipinfo.io/ip")
os.system("clear && clear && clear")
logo = '''\033[92m 
T o o l s
I n s t a l l e r \033[92m \033[92m \033[92m
       -->Programmed By badb00m And The Rest<--
    --->11223344556677889910101111121213131414<---
    '''
menu = '''\033[92m
     <0>Install BlackEye
     <1>Install NetAttack
     <2>Install The-Profiler
     <3>Install Fsociety
     <4>Install Kali-Termux
     <5>Install Social-Engineer-Toolkit
     <6>Install Shellphish
     <7>Hammer (DoS Tool That My Friend Daniel Uses)
     <999>Exit
'''
print logo
print menu
def quit():
            con = raw_input('Continue [Y/n] -> ')
            if con[0].upper() == 'N':
                exit()
            else:
                os.system("clear")
                print logo
                print menu
                select()
           
def  select():
  try:
    choice = input("user.new~# ")
    if choice == 1:
      d3 = raw_input('Execute/Decline : ')
      os.system("clear")
      print("""
N e t A t t a c k                           
      """)
      print("Installing! Please Wait!")
      os.system("git clone https://github.com/chrizator/netattack2")
      os.system("clear")
      print("Successfully Installed NetAttack2!")
      print("")
      quit()
    elif choice == 0:
        d3 = raw_input('Execute/Decline : ')
	  print("""
B l a c k e y e
""")
	  print("Installing! Please Wait!")
	  os.system("git clone https://github.com/thelinuxchoice/blackeye")
	  os.system("clear")
	  print("Successfully Installed Blackeye!")
	  print("")
	  quit()
    elif choice == 2:
        d3 = raw_input('Execute/Decline : ')
        os.system("clear")
        print("""
T h e - P r o f i l e r
""")
        print("Installing! Please Wait!")
        os.system("git clone https://github.com/b00mnation/The-Profiler")
        os.system("clear")
        print("Successfully Installed The-Profiler!")
        print("")
        quit()
    elif choice == 3:
        d3 = raw_input('Execute/Decline : ')
        os.system("clear")
        print("""
F s o c i e t y
""")
        print("Installing! Please Wait!")
        os.system("git clone https://github.com/Manisso/fsociety")
        os.system("clear")
        print("Successfully Installed Fsociety!")
        print("")
        quit()
    elif choice == 4:
        d3 = raw_input('Execute/Decline : ')
        os.system("clear")
        print("""
K a l i  N e t H u n t e r  I n  T e r m u x
""")
        print("Installing! Please Wait!")
        os.system("git clone https:///Hax4us/Nethunter-In-Termux")
        os.system("clear")
        print("Successfully Installed NetHunter!")
        print("")
        quit()
    elif choice == 5:
        d3 = raw_input('Execute/Decline : ')
        os.system("clear")
        print("""
S E T
""")
        print("Installing! Please Wait!")
        os.system("git clone https://github.com/trustedsec/social-engineer-toolkit")
        os.system("clear")
        print("Successfully Installed S E T!")
        print("")
        quit()
    elif choice == 6:
        d3 = raw_input('Execute/Decline : ')
        os.system("clear")
        print("""
S h e l l p h i s h
""")
        print("Installing! Please Wait!")
        os.system("git clone https://github.com/thelinuxchoice/shellphish")
        os.system("clear")
        print("Successfully Installed Shellphish!")
        print("")
        quit()
    elif choice == 7:
        d3 = raw_input('Execute/Decline : ')
        os.system("clear")
        print("""
H a m m e r
""")
        print("Installing! Please Wait!")
        os.system("git clone https://github.com/cyweb/hammer")
        os.system("clear")
        print("Successfully Installed Hammer!")
        print("")
        quit()
  except(KeyboardInterrupt):
    print ""
select()
