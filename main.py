# -------------In The Name of Allah---------------
# ----------Project Finale------------------------
# In this project we will apply all what we 've learnt in 149 videos
# It should be more than 1000 code _Target_
# Project Idea=>
# -------------------------------------------------------------------
# In this project tool name is FINALITA
# So, what this tool doing =>
# do what ever we want but, keep it tight lads, No one likes a bug in code ^_^  (Just Ideas from now )
# 1) With selenuim downlod picture from a specific site we will define it later, search from google and print output in terminal (cool)
# after this we can add bookmarks in loved sites
# 2) Make different color for every terminal output
# 3) use oop | inheritence | Multiuple inheritence | abstact methods | Encapsulation | decorators | @property decorators
# 4) There is a part of the tool for Advanced info about code like, timeit, debugging, unittest
# 5) Generate serial numbers for a bunch of data like user_id, user_name from database (at least 15 character)
# 6) With all operation print date and time, make logs file and user defines it in any place for fisrt time only
# 7) In the tool it will be part for fun or small info like, calculating age, playing a music, read an article from txt file
# 8) Then we don't need to mention that regular expresions will be used, dealing with databases
# 9) we will Diversifie between OOP an usual programming
# 10) We can use numpy for dealing with arrays like: make user import the array and then do sums, reshaping, slicing,
# compare Memory speed in two cases, store it in a file if he wants
# 11) we talked about file handling before and User Cridintials
# 12) We will see try | except | finally, with-as stat
# 13) If the user has a long article and it contains alot of repetead letters we can use recursion *hint* use lambda function #function recursion
# 14) Sometimes use zip function to make a nice block of output on the terminal, if wanted
# -------------------------------------------------------------------


# Algorithim for the project
# -------------------------------------------------------------------
# 1)Import modules *,Ducomenting*, Tool Name*, Terms of use*, file logging location and date&&time for all operations __Just Wait!!__*
# 2)Make serials for users with ids #make passwd for the printed file for security reasons *
# 3)Numpy module and all its operation *
# 4)Read Article *
# 6) Search from google on terminal*
#7) Testing code by timeit*
# -------------------------------------------------------------------

# Part1
# Documenting



# Importing modules
import random
import string
import ctypes
import os
import sys
import termcolor
import sqlite3
import time
import logging
import pyfiglet
import timeit
import re
from contextlib import redirect_stdout
import numpy as np
from playsound import playsound
from scipy.io.wavfile import write
import sounddevice as sd
from PIL import Image
import cv2
from gtts import gTTS
from googlesearch import search
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from colored import fg, bg, attr



# Tool_Name
# print("%s Welcome, To FINALITA project. %s" % (fg(1), attr(0)) )
print(termcolor.colored(pyfiglet.figlet_format("FINALITA", font="Graffiti" ), color="red" )) #doh #colossal #puffy #speed #stop  #basic  #rowancap  #crawford

# print ('%s Hello World !!! %s' % (fg(1), attr(0)))
# input('''%s hello %s''' %  (fg(1), attr(0)))


# Terms_of_use


# log function
def Log_Credintials(filename, messege):
    logging.basicConfig(filename="",
                        filemode="",
                        datefmt="",
                        format="")

#Part2

# Logging
#Establish class for inheritince


class DataBase(object):

    def __init__(self):
            while True:
                rex = r"^([A-Z]:\\)([A-z0-9]+).+([A-z0-9])?((\.db))$"
                self.file_path = input("%s Enter DataBase path *EXAMPLE* {C:/file.db}:# %s" % (fg(50), attr(1)))
                print("%s%s" % (fg(220), attr(1)))

                if self.file_path == '':
                    print("%s No value given, try again=> %s" % (fg(1), attr(1)))

                else:
                    if re.search(rex, self.file_path):
                        if os.path.isfile(self.file_path):
                            time.sleep(0.5)
                            print("Done!!")
                            break
                        else:
                            print("%s No DataBase In This Location With This Name, Enter Existed DataBase......%s" % (fg(196), attr(0)))



                    else:  # rex   ([A-Z]:\\)([A-z0-9]+).+([A-z0-9])?((\.log)|(\.txt)|(\.db))
                        rex0 = r"([A-Z]:\\)([A-z0-9]+).+([A-z0-9])?(.)"
                        if re.search(rex0, self.file_path):
                            print(
                                r"__This is DataBase file_ it should ends with %{.db}%, %EXAMPLE {C:\file.db}%, Try Again")

                        else:
                            print("%s Invalid Absolute path, Try Again:# %s" % (fg(160), attr(0)))
        # def true(self):
        #     return self.check_file(r"^([A-Z]:\\)([A-z0-9]+).+([A-z0-9])?((\.db))$")

class Serial(DataBase):  #If you 've learnt Cryptography you can Add Password for The Serials file

        # Making serial numbers for a specific users
        # make choise about characters and how long is it (15, 20, 30)
        # choise between either a new database or old one to add serials
        def __init__(self):
            DataBase.__init__(self)

        def serial_make(self):
            while True:
                choise = input('''
1=> Make serials with accii_letters only %It will be just Alphabetical only% 
2=> Make serials with ascci_letters and hexdigits %It will be Characters and numbers%
3=> Make serials with ascii_letters, hexdigits and special characters %It will be Characters, numbers and Special Characters%\n
 Note!! The OutPut Files will be in TXT files, If you want it in '.csv', Just Change the Extension\n
99=> Return To Main Menu
YOUR CHOICE\n

''')
                if choise == "1":
                    time.sleep(0.5)
                    print("%s OK, You preferred to write in ascii_only....... %s" % (fg(46), attr(1)))
                    time.sleep(1)
                    while True:   #break after calling the function
                        def ascii_make(count):
                            # print("OK, You prefered to write in ascii_only.......")

                            all_chars = string.ascii_letters
                            lenth = len(all_chars)
                            serial_test = []
                            while count > 0:
                                random_int = random.randint(0, lenth - 1)
                                random_call = all_chars[random_int]
                                serial_test.append(random_call)
                                count -= 1

                            return "".join(serial_test)      #just return it !!!

                        def data2():
                            while True:
                                try:
                                    db = sqlite3.connect(self.file_path)
                                    cr = db.cursor()
                                    inn = input("%s Enter Your First Table Name In Your DataBase. __Case Insensitive, Please__:# %s" % (fg(200), attr(1)))
                                    cr.execute(f"SELECT * from {inn}")
                                    global result
                                    result = cr.fetchall()
                                    with open(f"{os.getcwd()}\Serials.txt", "a") as f:
                                        with redirect_stdout(f):
                                            for row in result:
                                                print(f"UserID => {row[0]}", end="         ")
                                                print(f"{ascii_make(15)}")
                                            print("#" * 50)

                                    print("%s For security reasons we redirected the output to a Text file in the CURRENT location %s" % (fg(190),attr(1)))
                                    print(f"The Current location is {os.getcwd()}")
                                    print("%s %s" % (fg(188), attr(1)))
                                    time.sleep(3)
                                    break
                                except sqlite3.Error as error:
                                    print(f"You have Error for database %{error} %")
                                    print("%s make sure of your Table Name...... %s " % (fg(9), attr(1)))
                        data2()
                        break
                    break

                elif choise == "2":
                    time.sleep(0.5)
                    print("%s Well, Your Serials will Be In Ascii and Digits....... %s" % (fg(46), attr(1)))
                    time.sleep(1)
                    while True:  # break after calling the function
                        def ascii_make(count):

                            all_chars = string.ascii_letters + string.digits
                            lenth = len(all_chars)
                            serial_test = []
                            while count > 0:
                                random_int = random.randint(0, lenth - 1)
                                random_call = all_chars[random_int]
                                serial_test.append(random_call)
                                count -= 1

                            return "".join(serial_test)  # just return it !!!

                        def data2():
                            while True:
                                try:
                                    db = sqlite3.connect(self.file_path)
                                    cr = db.cursor()
                                    inn = input("%s Enter Your First Table Name In Your DataBase. __Case Insensitive, Please__:# %s" % (fg(200), attr(1)))
                                    cr.execute(f"SELECT * from {inn}")
                                    global result
                                    result = cr.fetchall()
                                    with open(f"{os.getcwd()}\Serials.txt", "a") as f:
                                        with redirect_stdout(f):
                                            for row in result:
                                                print(f"UserID => {row[0]}", end="         ")
                                                print(f"{ascii_make(15)}")
                                            print("#" * 50)

                                    print("%s For security reasons we redirected the output to a Text file in the CURRENT location %s" % (fg(158),attr(1)))
                                    print(f"The Current location is {os.getcwd()} ")
                                    print("%s %s" % (fg(147), attr(1)))
                                    time.sleep(3)
                                    break

                                except sqlite3.Error as error:
                                    print(f"You have Error for database %{error} %")
                                    print("%s make sure of your Table Name...... %s " % (fg(9), attr(1)))

                        data2()
                        break
                    break

                elif choise == "3":
                    time.sleep(0.5)
                    print("%s Perfect Way, your OPSEC will not be compromised, Hard to Crack...... %s" % (fg(46), attr(1)))
                    time.sleep(1)
                    while True:  # break after calling the function
                        def ascii_make(count):

                            all_chars = string.ascii_letters + string.digits + string.printable
                            lenth = len(all_chars)
                            serial_test = []
                            while count > 0:
                                random_int = random.randint(0, lenth - 1)
                                random_call = all_chars[random_int]
                                serial_test.append(random_call)
                                count -= 1

                            # with open(r"I:\ahmed.txt", "a") as f:
                            #     with redirect_stdout(f):
                            # listq = [1, 3, 5,7]
                            # for num in listq:
                            #     print(f"user {num}")
                            # print("".join(serial_test))
                            return "".join(serial_test)  # just return it !!!

                        def data2():
                            while True:
                                try:
                                    db = sqlite3.connect(self.file_path)
                                    cr = db.cursor()
                                    inn = input("%s Enter Your First Table Name In Your DataBase. __Case Insensitive, Please__:# %s" % (fg(200), attr(1)))
                                    cr.execute(f"SELECT * from {inn}")
                                    global result
                                    result = cr.fetchall()
                                    with open(f"{os.getcwd()}\Serials.txt", "a") as f:
                                        with redirect_stdout(f):
                                            for row in result:
                                                print(f"UserID => {row[0]}", end="         ")
                                                print(f"{ascii_make(15)}")
                                            print("#" * 50)
                                            print("%s%s" % (fg(45), attr(1)))

                                    print("%s For security reasons we redirected the output to a Text file in the CURRENT location %s" % (fg(190),attr(1)))
                                    print("%s%s" % (fg(196), attr(1)))
                                    print(f"The Current location is {os.getcwd()} ")
                                    print("%s%s" % (fg(10), attr(1)))
                                    print("Note!!, you will find the output A little Bit Different!! ")
                                    print("%s %s" % (fg(166), attr(1)))
                                    time.sleep(3)
                                    break

                                except sqlite3.Error as error:
                                    print(f"You have Error for database %{error} %")
                                    print("%s make sure of your Table Name...... %s " % (fg(9), attr(1)))

                        data2()
                        break
                    break
                elif choise == "99":
                    print("%s%s" % (fg(253), attr(1)))
                    tool_choose()

                elif choise == '':
                    print("%s Hey!!!, Your Choice.....%s" % (fg(1), attr(1)))
                    print("%s %s" % (fg(159), attr(1)))
                else:
                    print("%s Enter Number from These Choises......%s " % (fg(202), attr(1)))
                    print("Blowen fi Alterminal, Mesh 7armak Men Haga ^_^")
                    print("%s %s" % (fg(39), attr(1)))

#######################################################
#The first Part Finished Cheers!!
#In route to second one
#NUMPY

class Numpy_Comparison():

    def comparison_file(self):
        while True:
            try:
                elements = int(input("%s Enter your Elements Number, To Compare Between list And Numpy => %s" % (fg(40), attr(1))))
                if elements >= 1000000:
                    print(
                        "%s Please Wait, This Depending On your Ram, CPU Speed, I know They Are TOO SLOW ^_^.....%s" % (
                        fg(160), attr(1)))
                    print("%s%s" % (fg(226), attr(1)))
                    time.sleep(2)
                    list_nums1 = range(elements)
                    list_nums2 = range(elements)
                    array_num1 = np.arange(elements)
                    array_num2 = np.arange(elements)
                    list_time = time.time()
                    array_time = time.time()

                    #list Result
                    result = [(n1 + n2) for n1, n2 in zip(list_nums1, list_nums2)]
                    time.sleep(2)
                    print(f"List Time  '{time.time() - list_time}'")
                    #Array Result
                    Array_col = array_num1 + array_num2
                    time.sleep(2)
                    print(f"Array Time  '{time.time() - array_time}'")
                    if {time.time() - array_time} > {time.time() - list_time}:
                        print("%s$ Array $ is Faster Than $ List $ %s" % (fg(76), attr(1)))
                    else:
                        print("%s$ list $ is Faster Than $ Array $\n\n %s" % (fg(13), attr(1)))
                    time.sleep(3)
                    print("%s%s" % (fg(4), attr(1)))
                    print("__Hint!!__ ")
                    print(f"All Bytes for Array are {array_num2.size * array_num2.itemsize}\n")
                    print(f"All Bytes for List are {sys.getsizeof(list_nums2) * len(list_nums2)}")
                    print("%s%s" % (fg(199), attr(1)))
                    time.sleep(4)
                    break

                elif elements < 1000000:
                    print("%s Your Number Is To Small, Insert A bigger One, To Get A Clear Comparison.....%s" % (fg(1), attr(1)))
                    print("%s At Least 1 million.......%s " % (fg(10), attr(1)))
                    print("%s%s" % (fg(40), attr(1)))

            except ValueError:
                print("%s Enter A valid Number, please %s" % (fg(124),attr(1)))

class TimeIt():

    def time_it(self):
        while True:
            print("%s%s" % (fg(92), attr(1)))
            menu = input('''
1_) Test Your Input Time For One Time Only
2_) Test Your Input Time For Several Time\n
99-) Quit To Main Menu
            \n''')
            if menu == "1":
                time.sleep(0.5)
                while True:
                    try:
                        timeit_name = input("%s Enter your Input To Test (str, float, int):=>  %s" % (fg(220), attr(1)))
                        timeit_times = int(input("%s How Many Times you Wanna Run It:=> %s"% (fg(87), attr(1))))
                        # print(timeit.timeit(f"Your Input Time is '{timeit_name}' * {timeit_times}'"))
                        print("%s%s" % (fg(213), attr(1)))
                        print(f"Your Input Time Is: ")
                        print(timeit.timeit(f"name = '{timeit_name}'; name * {timeit_times}"))
                        print("%s%s" % (fg(227), attr(1)))
                        time.sleep(4)
                        break

                    except ValueError:
                        print("%s Enter A valid Input, Try Again:\n %s" % (fg(197), attr(1)))
                break #The Bigger LOOP breaks here
            elif menu == "2":
                time.sleep(2)
                while True:
                    try:
                        timeit2_name = input("%s Enter your Input To Test (str, int, float):=>  %s" % (fg(83), attr(1)))
                        timeit2_times = int(input("%s How Many Times you Wanna Run It (int):=> %s" % (fg(69), attr(1))))
                        print("%s%s" % (fg(1), attr(1)))
                        print("__WARNING!!__The Following Input, will be The Times To REPEAT the input, Don't Enter A big number, OR $ KERNEL PANIC $ ^_^ ")
                        print("%s%s" % (fg(14), attr(1)))
                        timeit_repeat = int(input("How Many Times you Wanna Repeat It:=> "))
                        print("Your Input Time Is:")
                        print("%s%s" % (fg(34), attr(1)))
                        print(timeit.repeat(f"name= '{timeit2_name}'; name * {timeit2_times}", repeat=timeit_repeat))
                        print("%s%s" % (fg(144), attr(1)))
                        time.sleep(4)

                        break

                    except ValueError:
                        time.sleep(1)
                        print("%s Enter A Valid Number. Please, Try Again:=>\n %s" % (fg(160), attr(1)))
                break
            elif menu == "99":
                print("%s%s" % (fg(253), attr(1)))
                tool_choose()
                break
            else:
                time.sleep(1)
                print("%s Please, Enter A Choice From Those: %s" % (fg(198), attr(1)))


#In route to the third
#Media


class Music:
        def Music_Player(self):
            while True:
                print("%s%s" % (fg(252), attr(1)))
                menu = input('''
_1_ )Play A Music
_2_) Record An Audio (__I Know Your Sound Is terrifying__ ^_^)\n
_99_) Return To Main Menu
''')

                if menu == "1":
                    time.sleep(2)
                    while True:   #JUST ADD A WHILE LOOP, SHIT.... IAM A STUPED ONE!!!!!!
                        path = input("%s Enter Your Directory Path __Just The Directory__=> %s" % (fg(47), attr(1)))
                        rex0 = r"([A-Z]:\\)([A-z0-9]+)?"
                        if re.search(rex0, path):
                            time.sleep(1)
                            os.chdir(path)
                            print("%s%s" % (fg(14), attr(1)))
                            for key, file in enumerate(os.listdir(path)):
                                print(f"{key + 1} => {file}")

                            while True:
                                song = input("%s Enter your Song __With The Extension__=> %s" % (fg(226), attr(1)))
                                rex1 = r"^([A-z0-9]+).+((\.mp3)|(\.wav)|(\.wma)|(\.aac)|(\.aiff)|(\.m4a)|(\.asf)|(\.aif)|(\.mp4))$"
                                if re.search(rex1, song):
                                    time.sleep(2)
                                    print("Palying........")
                                    playsound(song)
                                    print("%s%s" % (fg(136), attr(1)))
                                    break

                                elif song == '':
                                    print("%s Hey, Your Song.. %s" % (fg(196), attr(1)))
                                elif os.path.exists(song):
                                    print("%s No, Songs Here With This Name %s" % (fg(88), attr(1)))
                                    print("Remember You Are In The Song Directory.....")
                                else:
                                    time.sleep(2)
                                    print("%s {mp3, wav, wma, aac, aiff, m4a, asf, aif, mp4} %s" % (fg(4), attr(1)))
                                    print("Enter a valid Song Extension From Above ex:{C:\Sound.mp3}=> ")
                                    print(
                                        "%s Remember You Are In The Song Directory, Just Insert Song with Extension.....%s" % (fg(124), attr(1)))

                            break #Bigger Loop breaks here

                        elif path == '':
                            print("%s Enter Your Path, MAN %s" % (fg(1), attr(1)))
                        else:
                            print("%s Enter A Valid One %s " % (fg(196), attr(1)))
                    break

                elif menu == "2":
                    time.sleep(2)
                    while True:
                        print("%s Enter Your Record Duration from This List: %s" % (fg(83), attr(1)))
                        print("%s%s" % (fg(167), attr(1)))
                        menu0 = input('''
1-) 10 seconds
2-) 20 seconds 
3-) 30 seconds 
4-) 40 seconds 
5-) 1 Min
6-) 2 Min
7-) 3 Min  Mane3darsh Nesta7mel Sotak Aktar Men 3 D3aye3 :)\n
''')

                        def record_sound(seconds):
                            fs = 44100  # Sample rate
                            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                            sd.wait()  # Wait until recording is finished
                            write('Record.wav', fs, myrecording)
                            os.system("start Record.wav")

                        try:
                            if menu0 == "1":
                                print("Recording in 3 seconds.....")
                                time.sleep(3)
                                print("Now!!")
                                record_sound(10)
                                break
                            elif menu0 == "2":
                                print("Recording in 3 seconds.....")
                                time.sleep(3)
                                print("Now!!")
                                record_sound(20)
                                break
                            elif menu0 == "3":
                                print("Recording in 3 seconds.....")
                                time.sleep(3)
                                print("Now!!")
                                record_sound(30)
                                break
                            elif menu0 == "4":
                                print("Recording in 3 seconds.....")
                                time.sleep(3)
                                print("Now!!")
                                record_sound(40)
                                break
                            elif menu0 == "5":
                                print("Recording in 3 seconds.....")
                                time.sleep(3)
                                print("Now!!")
                                record_sound(60)
                                break
                            elif menu0 == "6":
                                print("Recording in 3 seconds.....")
                                time.sleep(3)
                                print("Now!!")
                                record_sound(120)
                                break
                            elif menu0 == "7":
                                print("Recording in 3 seconds.....")
                                time.sleep(3)
                                print("Now!!")
                                record_sound(180)
                                break
                            else:
                                print("%s Hey!!!, Your Choice\n %s" % (fg(196), attr(1)))
                            print("%s%s" % (fg(11), attr(1)))

                        except:
                            pass
                    break

                elif menu == "99":
                    print("%s%s" % (fg(253), attr(1)))
                    tool_choose()

                elif menu == '':
                    print("%s Your Choice!!!, You Forget The choise Everytime, Are You Testing The App ^_^ %s" % (fg(199), attr(1)))
                else:
                    print("%s Your ****** Choice! %s" % (fg(1), attr(1)))

class Images:
        def Image_show(self):
            while True:
                print("%s%s" % (fg(41), attr(1)))
                menu1 = input('''
_1_) Show A Picture
_2_) Print Histogram For An Image\n
_99_) Return To Main Menu
''')

                if menu1 == "1":
                    time.sleep(2)
                    while True:
                        path = input("%s Enter Your Directory Path __Just The Dir__=> %s" % (fg(48), attr(1)))
                        rex0 = r"([A-Z]:\\)([A-z0-9]+)?"
                        regex = "[A-z0-9].+((\.jpe?g)|(\.png)|(\.gif)|(\.bmp))"
                        if re.search(rex0, path):
                            time.sleep(2)
                            os.chdir(path)
                            print("%s%s" % (fg(40), attr(1)))
                            for key, file in enumerate(os.listdir(path)):
                                print(f"{key + 1} => {file}")
                            while True:
                                image = input("%s Enter your Image __With The Extension__=> %s" % (fg(10), attr(1)))
                                rex1 = r"^([A-z0-9]+).+?$"
                                if re.search(regex, image):
                                    time.sleep(2)
                                    print("Showing........")
                                    img = Image.open(image)
                                    Image._show(img)
                                    print("%s%s" % (fg(45), attr(1)))
                                    break

                                elif image == '':
                                    print("%s Hey, Your Image.. %s" % (fg(13), attr(1)))
                                # elif IOError:
                                #     print("No, Images Here With This Name")
                                else:
                                    print(
                                        "%s Remember You Are In The Image Directory, Just Insert Image with Extension..... %s" % (fg(196), attr(1)))
                                    print("Enter The Image With The Right Extension")
                            break
                        elif path == '':
                            print("%s Enter Your Path, MAN %s" % (fg(196), attr(1)))
                        else:
                            print("%s Enter A Valid One %s" % (fg(125), attr(1)))

                    break# Bigger Loop breaks here
                elif menu1 == "2":
                    time.sleep(2)
                    print(
                        "%s \nA histogram of an image is a graphical representation of the tonal distribution in a digital image.\nIt contains what all the brightness values contained in an image are.\nIt plots the number of pixels for each brightness value.\n %s" % (fg(48), attr(1)))
                    while True:
                        path = input("%s Enter Your Directory Path __Just The Dir__=> %s" % (fg(44), attr(1)))
                        rex0 = r"([A-Z]:\\)([A-z0-9]+)?"
                        regex = "[A-z0-9].+((\.jpe?g)|(\.png)|(\.gif)|(\.bmp))"
                        if re.search(rex0, path):
                            time.sleep(1)
                            os.chdir(path)
                            print("%s%s" % (fg(184), attr(1)))
                            for key, file in enumerate(os.listdir(path)):
                                print(f"{key + 1} => {file}")
                            while True:
                                image = input("%s Enter your Image __With The Extension__=> %s" % (fg(46), attr(1)))

                                rex1 = r"^([A-z0-9]+).+?$"
                                if re.search(regex, image):
                                    time.sleep(1)
                                    print("Hold On!!...")
                                    img = Image.open(image)
                                    print(img.histogram())
                                    print("%s%s" % (fg(2), attr(1)))
                                    break

                                elif image == '':
                                    print("%s Hey, Your Image.. %s" % (fg(196), attr(1)))
                                # elif IOError:
                                #     print("No, Images Here With This Name")
                                else:
                                    print("%s Enter The Image With The Right Extension ex:{C:\image.jpg} %s" % (fg(148), attr(1)))
                                    print(
                                        "Remember You Are In The Image Directory, Just Insert Image with Extension.....")

                            break
                        elif path == '':
                            print("%s Enter Your Path, MAN %s" % (fg(196), attr(1)) )
                        else:
                            print("%s Enter A Valid Path.. %s" % (fg(196), attr(1)))
                    break

                elif menu1 == "99":
                    print("%s%s" % (fg(253), attr(1)))
                    tool_choose()
                else:
                    print("%s Enter Number from Those... %s" % (fg(124), attr(1)))

class Video_Player():

        def video_player(self):
            while True:
                print("%s%s" % (fg(77), attr(1)))
                menu2 = input('''
I) Play A video  __If you Wanna Quit From Video, Just Press 'Q'__
II) Record A Video\n
99) Return To Main Menu           
''')
                if menu2 == "1":
                    time.sleep(2)
                    while True:
                        path = input("%s Enter Your Directory Path:=> %s" % (fg(155), attr(1)))
                        rex0 = r"([A-Z]:\\)([A-z0-9]+)?"
                        if re.search(rex0, path):
                            time.sleep(2)
                            os.chdir(path)
                            print("%s%s" % (fg(123), attr(1)))
                            for key, file in enumerate(os.listdir(path)):
                                print(f"{key + 1} => {file}")

                            while True:
                                video = input("%s Enter Your VIDEO Name __With Its Extension__ => %s" % (fg(118), attr(1)))
                                rex1 = r"^([A-z0-9]+).+((\.mp4)|(\.mov)|(\.wmv)|(\.avi)|(\.mkv)|(\.mpg)|(\.ogg)|(\.3gp)|(\.ogv))$"
                                if re.search(rex1, video):
                                    cap = cv2.VideoCapture(video)

                                    # Check if camera opened successfully
                                    if (cap.isOpened() == False):
                                        print("Here Is An Error From Cv2 ")

                                    # Read until video is completed
                                    while (cap.isOpened()):

                                        # Capture frame-by-frame
                                        ret, frame = cap.read()
                                        if ret == True:
                                            cv2.imshow('VideoPlayer', frame)
                                            # print("Playing.........")

                                            # Press Q on keyboard to  exit
                                            if cv2.waitKey(25) & 0xFF == ord('q'):

                                                break

                                        # Break the loop
                                        else:
                                            break
                                    #Close EveryThing
                                    cap.release()
                                    cv2.destroyAllWindows()
                                    print("%s%s" % (fg(36), attr(1)))
                                    break
                                elif video == '':
                                    print("%s You Forgot To Enter Your Video...__Omal Ent Gaybni leah!!__ %s" % (fg(124), attr(1)))
                                else:
                                    print("%s Enter Your Video with Extension: %s" % (fg(200),attr(1)))
                                    print("It may be one of Those => { (mp4), (mov), (wmv), (avi), (mkv), (mpg), (ogg), (3gp), (ogv) }")
                        elif path == '':
                            print("%s Enter Your Path, Dud... %s" % (fg(196), attr(1)))
                        else:
                            print("%s Enter A Valid Absolute Path.... %s" % (fg(198), attr(1)))
                            print("Remember You Are In The Video Directory, Just Insert Video with Extension.....")

                elif menu2 == "2":
                    time.sleep(2)
                    print("%s To end Capturing, Press 'q', The Video will Be saved In Current Location %s" % (fg(82), attr(1)))
                    print(f"Current Working Dir is: {os.getcwd()}")
                    print("Playing in 3 sec....")
                    time.sleep(3)
                    print("Now!!")
                    filename = 'video.mp4'
                    frames_per_second = 24.0
                    res = '720p'

                    # Set resolution for the video capture
                    # Function adapted from https://kirr.co/0l6qmh
                    def change_res(cap, width, height):
                        cap.set(3, width)
                        cap.set(4, height)

                    # Standard Video Dimensions Sizes
                    STD_DIMENSIONS = {
                        "480p": (640, 480),
                        "720p": (1280, 720),
                        "1080p": (1920, 1080),
                        "4k": (3840, 2160),
                    }

                    # grab resolution dimensions and set video capture to it.
                    def get_dims(cap, res='1080p'):
                        width, height = STD_DIMENSIONS["720p"]
                        if res in STD_DIMENSIONS:
                            width, height = STD_DIMENSIONS[res]
                        ## change the current caputre device
                        ## to the resulting resolution
                        change_res(cap, width, height)
                        return width, height

                    VIDEO_TYPE = {
                        'avi': cv2.VideoWriter_fourcc(*'XVID'),
                        # 'mp4': cv2.VideoWriter_fourcc(*'H264'),
                        'mp4': cv2.VideoWriter_fourcc(*'XVID'),
                    }

                    def get_video_type(filename):
                        filename, ext = os.path.splitext(filename)
                        if ext in VIDEO_TYPE:
                            return VIDEO_TYPE[ext]
                        return VIDEO_TYPE['avi']

                    cap = cv2.VideoCapture(0)
                    out = cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(cap, res))

                    while True:
                        ret, frame = cap.read()
                        out.write(frame)
                        cv2.imshow('frame', frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break

                    cap.release()
                    out.release()
                    cv2.destroyAllWindows()
                    print("%s%s" % (fg(77), attr(1)))
                    break

                elif menu2 == "99":
                    print("%s%s" % (fg(253), attr(1)))
                    tool_choose()
                else:
                    print("%s Import Your Number!!!. These Numbers In Latin Language!! %s" % (fg(196), attr(1)))


#YOU BETTER WATCH OUT!!!!

class Article_Reader():
    def article(self):
        while True:
            path = input("%s Enter Your Article path:=> %s" % (fg(120), attr(1)))
            rex = r"^([A-Z]:\\)([A-z0-9]+).+([A-z0-9])?((\.log)|(\.txt))$"
            if re.search(rex, path):
                time.sleep(2)
                file1 = open(path, "r").read().replace("\n", " ")
                print("%s Alright, Redirected It Into An Mp3 file........ %s" % (fg(94), attr(1)))
                speech = gTTS(text=str(file1), lang='en', slow=False)   #You can change language form here lang="your one"
                speech.save("voice.mp3")
                print("%s Starting Mp3 file in 3 seconds....... %s" % (fg(48), attr(1)))
                time.sleep(3)
                os.system("start voice.mp3")
                print("%s%s" % (fg(214), attr(1)))
                break

            else:
                print("%s Enter Valid Absolute Path __Your file should Ends with (.txt), (.log) %s" % (fg(197), attr(1)))
                print("%s%s" % (fg(83), attr(1)))
                print(r"EX{C:\file.txt}.....")


class Age:
    def Age_clac(self):
        while True:
            try:
                print("%s%s" % (fg(1), attr(1)))
                print("Note This App -Ager- Is to Basic, Just for Fun!!")
                age = int(input("%s Please Write Your Age:=> %s" % (fg(2), attr(1))))
                print("%s ######Just Choose the first letter###### %s" % (fg(196), attr(1)))
                while True:
                    unit = input("%s Please Choose Time Unit: Months(m), Weeks(w), Days(d), Hours(h) %s" % (fg(45), attr(1))).strip().lower()

                    year = unit
                    months = int(age) * 12
                    weeks = months * 4
                    days = int(age) * 365
                    hours = int(days) * 24
                    time.sleep(2)
                    print("%s%s" % (fg(214), attr(1)))
                    if unit == 'months' or unit == 'm':
                        print(f"Your Age in Months is: {months} Months.")
                        print("%s%s" % (fg(126), attr(1)))
                        break
                    elif unit == 'weeks' or unit == 'w':
                        print(f"Your Age in Weeks is:  {weeks} Weeks.")
                        print("%s%s" % (fg(126), attr(1)))
                        break
                    elif unit == 'days' or unit == 'd':
                        print(f"Your Age in Days is:  {days} Days.")
                        print("%s%s" % (fg(126), attr(1)))
                        break
                    elif unit == 'hours' or unit == "h" or unit == "H":
                        print(f"Your Age in Hours is:  {hours} Hours")
                        print("%s%s" % (fg(126), attr(1)))
                        break
                    # elif unit == "a":
                    #     print(f"Years: {age}  Months {months}  Days {days}  Hours {hours}")
                    #     break
                    else:
                        print("%s Enter A Choice from (m, w, d, h) %s" % (fg(160), attr(1)))
                break

            except ValueError:
                print("%s Enter Integer Please %s" % (fg(87), attr(1)))


#Chrome Work  __Selinum__
class Google:
    def google_search(self):
        while True:
            query = input("%s Enter Your Query=> %s" % (fg(184), attr(1)))
            if query == '':
                print("%s Enter Your Search, Please..... %s" % (fg(124), attr(1)))
            else:
                while True:
                    time.sleep(2)
                    results = input("%s How Many Results You Want=> %s" % (fg(46), attr(1)))
                    if results.isdigit():
                        print("%s You Can just Click your Link from Below And you 'll Be Redirected To Your Browser......%s" % (fg(1), attr(1)))
                        time.sleep(2)
                        for go in search(query,  num_results=int(results), lang="en"):  #You can change it to your language!!
                            print(go)
                            print("%s%s" % (fg(28), attr(1)))
                        break
                    elif results == '':
                        print("%s Enter Number of Search Results...... %s" % (fg(200), attr(1)))
                    else:
                        print("%s This is The Number Of The Results, It Should Be A number (BY LOGIC!!)........ %s" % (fg(82),attr(1)))
                break #Bigger loop breaks here

class Selenium:  # WE did not Enter selenuim So Deeply just the basics, you can develop the code
    def selenium_search(self):
        while True:
                print("%s%s" % (fg(196), attr(1)))
                print("Note!! This APP -Seleniumer- Is too too Basic, We Did not Go so Deep, You Can Develop It....^_^.")
                path = input("%s Enter Your website Ex:{google.com}=> %s" % (fg(45),attr(1)))
                print("%s%s" % (fg(2), attr(1)))
                print("OR You Can Start with 'elzero.org', Ay Khedma ya Handasa :) ")
                rex = '^(\w+)\.(\w+)$'   #You Can Update This Rex
                while True:
                    if re.search(rex, path):
                        time.sleep(2)
                        browser = webdriver.Chrome(ChromeDriverManager().install())
                        browser.get(f"https://{path}")
                        browser.fullscreen_window()
                        browser.implicitly_wait(20)
                        break
                    else:
                     print("%s Your URL Should Be Like This: {example.example} %s" % (fg(124), attr(1)))
                    break



class LogFile(object):
    def check_file(self):
        # self.file_path1 = input("Enter file path you wanna save the logging file in it *EXAMPLE* {C:/file.log}:# ")
        while True:
            file_path1 = input("Enter file path you wanna save the logging file in it *EXAMPLE* {C:/file.log}:# ")
            if file_path1 == '':
                print("No value given, try again=> ")
            elif os.path.exists(file_path1):
                print("This file Already Exists, try Another name=> ")
            else:
                rex = r"^([A-Z]:\\)([A-z0-9]+).+([A-z0-9])?(\.log)"
                if re.search(rex, file_path1):

                    def Check_Admin():
                        try:
                            os.getuid() == 0
                        except AttributeError:
                            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

                            Log_Credintials(logging.basicConfig(filename=file_path1,
                                                                filemode="a",
                                                                datefmt="%d %B %y, %H:%M:%S",
                                                                format="%(asctime)s _%(name)s_  * %(levelname)s * => '%(message)s'"),
                                            messege=logging.critical("Unrooted user used the tool..."))
                            print("Done!!")

                    Check_Admin()

                    Log_Credintials(filename=logging.basicConfig(filename=file_path1,
                                                                 filemode="a",
                                                                 datefmt="%d %B %y, %H:%M:%S",
                                                                 format="%(asctime)s _%(name)s_  * %(levelname)s * => '%(message)s'"),
                                    messege=logging.warning("Log file created!...."))
                    if DataBase:
                        Log_Credintials(logging.basicConfig(filename=f"{file_path1}",
                                                            filemode="a",
                                                            datefmt="%d %B %y, %H:%M:%S",
                                                            format="%(asctime)s _%(name)s_  * %(levelname)s * => '%(message)s'"),
                                        messege=logging.critical(" Users IDs Retrieved from DataBase..."))
                    elif Serial:
                        Log_Credintials(logging.basicConfig(filename=f"{file_path1}",
                                                            filemode="a",
                                                            datefmt="%d %B %y, %H:%M:%S",
                                                            format="%(asctime)s _%(name)s_  * %(levelname)s * => '%(message)s'"),
                                        messege=logging.critical(" Serials Numbers Generated..."))

                    elif Numpy_Comparison:
                        Log_Credintials(logging.basicConfig(filename=f"{file_path1}",
                                                            filemode="a",
                                                            datefmt="%d %B %y, %H:%M:%S",
                                                            format="%(asctime)s _%(name)s_  * %(levelname)s * => '%(message)s'"),
                                        messege=logging.critical("A Comparison Between Numpy and List Generated..."))
                    elif TimeIt:
                        Log_Credintials(logging.basicConfig(filename=f"{file_path1}",
                                                            filemode="a",
                                                            datefmt="%d %B %y, %H:%M:%S",
                                                            format="%(asctime)s _%(name)s_  * %(levelname)s * => '%(message)s'"),
                                        messege=logging.critical(" Code Speed Measured By TimeIt Module..."))
                    elif Music:
                        Log_Credintials(logging.basicConfig(filename=f"{file_path1}",
                                                            filemode="a",
                                                            datefmt="%d %B %y, %H:%M:%S",
                                                            format="%(asctime)s _%(name)s_  * %(levelname)s * => '%(message)s'"),
                                        messege=logging.critical(" Music Class Opened Even To Play a song or To record Video..."))
                    elif Images:
                        Log_Credintials(logging.basicConfig(filename=f"{file_path1}",
                                                            filemode="a",
                                                            datefmt="%d %B %y, %H:%M:%S",
                                                            format="%(asctime)s _%(name)s_  * %(levelname)s * => '%(message)s'"),
                                        messege=logging.critical(" Image Class Opened Even for Showing A picture or Print Historgram for A picture..."))
                    elif Video_Player:
                        Log_Credintials(logging.basicConfig(filename=f"{file_path1}",
                                                            filemode="a",
                                                            datefmt="%d %B %y, %H:%M:%S",
                                                            format="%(asctime)s _%(name)s_  * %(levelname)s * => '%(message)s'"),
                                        messege=logging.critical(" Video Class opened Even for Playing A vedio or For Recording A video..."))
                    elif Article_Reader:
                        Log_Credintials(logging.basicConfig(filename=f"{file_path1}",
                                                            filemode="a",
                                                            datefmt="%d %B %y, %H:%M:%S",
                                                            format="%(asctime)s _%(name)s_  * %(levelname)s * => '%(message)s'"),
                                        messege=logging.critical(" Article_Reader Class Opened for Making An Mp3 file for Article..."))

                    elif Age:
                        Log_Credintials(logging.basicConfig(filename=f"{file_path1}",
                                                            filemode="a",
                                                            datefmt="%d %B %y, %H:%M:%S",
                                                            format="%(asctime)s _%(name)s_  * %(levelname)s * => '%(message)s'"),
                                        messege=logging.critical(" Age Class Opened for Calculating Age..."))
                    elif Google:
                        Log_Credintials(logging.basicConfig(filename=f"{file_path1}",
                                                            filemode="a",
                                                            datefmt="%d %B %y, %H:%M:%S",
                                                            format="%(asctime)s _%(name)s_  * %(levelname)s * => '%(message)s'"),
                                        messege=logging.critical(" Google Class Opened for Searching In Google..."))
                    elif Selenium:
                        Log_Credintials(logging.basicConfig(filename=f"{file_path1}",
                                                            filemode="a",
                                                            datefmt="%d %B %y, %H:%M:%S",
                                                            format="%(asctime)s _%(name)s_  * %(levelname)s * => '%(message)s'"),
                                        messege=logging.critical(" Selenium Class Opened for Automating Browser..."))

                    break


                else:  # rex   ([A-Z]:\\)([A-z0-9]+).+([A-z0-9])?((\.log)|(\.txt)|(\.db))
                    rex0 = r"([A-Z]:\\)([A-z0-9]+).+([A-z0-9])?(.)"
                    if re.search(rex0, file_path1):
                        print(r" This is a log file it should ends with %{.log}%, %EXAMPLE {C:\file.log}%, Try Again ")
                    else:
                        print("Invalid Absolute path, Try Again:# ")



def Finalita_Help():
    '''
    So, what does this tool doing => simply it makes a bunch of things like:
    1=> Generate serial numbers for users in DataBase
    2=> Compare Arrays and List Speed in Memory
    3=> Test code time and how fast is it with TIMEIT
    4=> Record Music, Show Histogram for Pictures, Record Video
    5=> Playing a music, Show Image, Play Video
    6=> Read an article from txt file
    7=> Calculating Age
    8=> Search in google and print the result on terminal
    9=> Open Chrome Browser With Selenium
    '''


#Choise
def tool_choose():
    while True:
        choice = input('''
1-) Generate Serial Numbers for Users in A Specific DataBase.
2-) Compare Between Numpy And List Speed.
3-) Measure Your Code With TimeIt.
4-) Play && Record Audio.
5-) Show && Print Histogram For A Picture.
6-) Play && Record Video .
7-) Read An Article From Txt File (By The Nice Lady from Google.^_^).
8-) Calculate Your Age.
9-) Search From Google In The Terminal.
10-) Automate Browser With Selenium and Open A Specific Site.
11-) FINALITA Help Manual!
404-) Quit Finalita
''')
        if choice == "1":
            time.sleep(1)
            print(termcolor.colored(pyfiglet.figlet_format("Serials", font="Starwars" ), color="red" ))  # define it in a function
            serial = Serial()
            serial.serial_make()
        elif choice == "2":
            time.sleep(1)
            print(termcolor.colored(pyfiglet.figlet_format("comparator", font="Orge"), color="blue"))
            numpy = Numpy_Comparison()
            numpy.comparison_file()
        elif choice == "3":
            time.sleep(1)
            print(termcolor.colored(pyfiglet.figlet_format("Measurer", font="Banner3"), color="green"))
            timeit = TimeIt()
            timeit.time_it()
        elif choice == "4":
            time.sleep(1)
            print(termcolor.colored(pyfiglet.figlet_format("Dancer", font="Block"), color="red"))
            music = Music()
            music.Music_Player()
        elif choice == "5":
            time.sleep(1)
            print(termcolor.colored(pyfiglet.figlet_format("Imager", font="Chunky"), color="red"))
            image = Images()
            image.Image_show()
        elif choice == "6":
            time.sleep(1)
            print(termcolor.colored(pyfiglet.figlet_format("V.Player", font="colossal"), color="blue"))
            video = Video_Player()
            video.video_player()
        elif choice == "7":
            time.sleep(1)
            print(termcolor.colored(pyfiglet.figlet_format("Speaker", font="Cricket"), color="blue"))
            article = Article_Reader()
            article.article()
        elif choice == "8":
            time.sleep(1)
            print(termcolor.colored(pyfiglet.figlet_format("Ager", font="Caligraphy"), color="red"))
            age = Age()
            age.Age_clac()
        elif choice == "9":
            time.sleep(1)
            print(termcolor.colored(pyfiglet.figlet_format("Googler", font="Speedy"), color="red"))
            search = Google()
            search.google_search()
        elif choice == "10":
            print(termcolor.colored(pyfiglet.figlet_format("Seleniumer", font="Doom"), color="yellow"))
            time.sleep(1)
            selenium = Selenium()
            selenium.selenium_search()
        elif choice == "11":
            time.sleep(1)
            print("%s%s" % (fg(10), attr(1)))
            print(Finalita_Help.__doc__)
            print("Lets Try The Tool Again.")
            print("%s%s" % (fg(25), attr(1)))
            time.sleep(15)
        elif choice == "404":
            print("%s%s" % (fg(10), attr(1)))
            print("Sad To See You Leave, Bye!!")
            time.sleep(2)
            sys.exit()


        elif choice == '':
            time.sleep(1)
            print("%s%s" % (fg(196), attr(1)))
            print("Hmmmmmmm!!!, Here We Begin Joking Time. Your Number Please ^_^ ")
            print("%s%s" % (fg(251), attr(1)))
        else:
            time.sleep(1)
            print("%s%s" % (fg(82), attr(1)))
            print("Mr User, We Have Numbers From 1-11, Please Choose From 'em.")
            print("Very Important Hint!!. I Don't Know Your Name, So I said Mr User :), Sorry! Just Kidding.")
            print("%s%s" % (fg(251), attr(1)))


def main():
    while True:
        print("%s%s" % (fg(14), attr(1)))
        terms_of_use = input(
            "Note we have Terms of use, like:\n#Access DataBase Tables\n#Automate Browser\n#Create files and modify 'em"
            "\n#Acsses music, Images and videos libraries. Do you Agree On This? \n(y/n)?")

        if terms_of_use == "yes" or terms_of_use == "y" or terms_of_use == "Y" or terms_of_use == "Yes":  # All what next will be after this condition
            time.sleep(1.5)
            print("%s%s" % (fg(196), attr(1)))
            print("Welcome To FINALITA...")
            print("%s%s" % (fg(251), attr(1)))
            tool_choose()

        elif terms_of_use == "no" or terms_of_use == "N" or terms_of_use == "n" or terms_of_use == "No":
            print("%s%s" % (fg(196), attr(1)))
            retry = input("Sorry we cannot proceed without your Acceptance, Are you sure you wanna quit? (y/n)?")
            if retry == "yes" or retry == "y" or retry == "Y" or retry == "Yes":
                print("%s Bye, Have a nice day!! ^_^ %s" % (fg(87), attr(1)))
                exit()
            else:
                time.sleep(1.5)
                print("%s Then, It's Ok..... %s" % (fg(46), attr(1)))
                print("Welcome To FINALITA...")
                print("%s%s" % (fg(253), attr(1)))
                tool_choose()
        else:
            print("%s Please Choose Either 'yes' or 'no'\n %s" % (fg(197), attr(1)))


if __name__ == "__main__":
    main()







#########################################################
#Finished
#Do I Even Exist??

#Easster Egg _Like Ones In Gta__ ^_^ , If You Read This Line You Will Observe That The 5 Projects Ends with "ITA" =>
#FINALITA | CONTACTITA | JOBITA, If You Wanna Know Why, So Lets Make It More Challenging.....
#This HASH OF an ENCRYPTED TEXT DECRYPT IT AND find out why??
"muAboCaluMAPWa2guBE3mNBjIafVjskb8twGlp8OR0IPbixiTw8+CjevDr9YKdehcHEKcguxZxoJDhHLOaMI/RfE7WXfI92hDrFvRE0IPAXFLoCAjpVUzWJBdwC3dt53uLeab5XLReD3nbUOas7G20gheNaZ0wtm7WM73F9LPpz+kVt5XszrQ0RJlPZglF4k5BG/sjM8LMWzPuC2PrB3w7dHY1g5yKpB3GB7HVtU5hoxHUE0vzsQRaJICYUNmws/"
#Site To Help You: "https://www.online-toolz.com/tools/text-encryption-decryption.php"

