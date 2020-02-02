import os #line:2
import time #line:3
import sys #line:4
from sys import platform #line:5
from gtts import gTTS #line:6
import speech_recognition as sr #line:7
import webbrowser #line:8
import smtplib #line:9
import getpass #line:10
import platform #line:11
__version__ ="1.0"#line:15
__codename__ ="Install"#line:16
__appname__ ="CoronaVirus"#line:17
__authors__ =["_Hwd_"]#line:18
__status__ ="Beta"#line:19
help ="!help"#line:21
options ="!options"#line:22
time .sleep (1 )#line:24
os .system ('clear')#line:25
Help1 ="Welcome to. Corona,Virus Created By. Hwd."#line:27
In1stal ="Installing CoronaVirus Tool"#line:28
In1stalled ="Sufficiently Installed Corona,Virus."#line:29
Upgrade1 ="Starting Upgrade tool"#line:30
UpgradeInst ="Installing Upgrades in Work!"#line:31
Upgraded ="Sufficiently Upgrade!"#line:32
MainMenu ="Main Menu"#line:33
GoodBye =("GoodByee,"+getpass .getuser ())#line:34
openweb ="Opening Url"#line:35
coping ="Getting Folder from Hwd Database"#line:36
copied =("Sufficiently Copied!, the file is on CoronaVirus. Hwd. Malicious Folder, do not start on your pc, Copy the folder on The victim Computer thanks for using, GoodBye."+getpass .getuser ())#line:37
Uninstalled ="Sufficiently Uninstalled!"#line:38
language ='en'#line:40
output =gTTS (text =Help1 ,lang =language ,slow =False )#line:42
output1 =gTTS (text =In1stal ,lang =language ,slow =False )#line:43
output2 =gTTS (text =In1stalled ,lang =language ,slow =False )#line:44
output3 =gTTS (text =Upgrade1 ,lang =language ,slow =False )#line:45
output4 =gTTS (text =UpgradeInst ,lang =language ,slow =False )#line:46
output5 =gTTS (text =Upgraded ,lang =language ,slow =False )#line:47
output6 =gTTS (text =MainMenu ,lang =language ,slow =False )#line:48
output7 =gTTS (text =GoodBye ,lang =language ,slow =False )#line:49
output8 =gTTS (text =openweb ,lang =language ,slow =False )#line:50
output9 =gTTS (text =coping ,lang =language ,slow =False )#line:51
output10 =gTTS (text =copied ,lang =language ,slow =False )#line:52
output11 =gTTS (text =Uninstalled ,lang =language ,slow =False )#line:53
output .save ("Help1.mp3")#line:55
output1 .save ("1.mp3")#line:56
output2 .save ("Installed.mp3")#line:57
output3 .save ("SUpgrade.mp3")#line:58
output4 .save ("UpgradeInst.mp3")#line:59
output5 .save ("Upgraded.mp3")#line:60
output6 .save ("MainMenu.mp3")#line:61
output7 .save ("GoodBye.mp3")#line:62
output8 .save ("url.mp3")#line:63
output9 .save ("coping.mp3")#line:64
output10 .save ("copied.mp3")#line:65
output11 .save ("Uninstalled.mp3")#line:66
class colors :#line:72
    HEADER ='\033[95m'#line:73
    OKBLUE ='\033[94m'#line:74
    OKGREEN ='\033[92m'#line:75
    WARNING ='\033[93m'#line:76
    FAIL ='\033[91m'#line:77
    BFAIL ='\033[1m\033[91m'#line:78
    ENDC ='\033[0m'#line:79
    BOLD ='\033[1m'#line:80
    UNDERLINE ='\033[4m'#line:81
print ("Checking Updates...")#line:82
os .system ('clear')#line:83
if platform =="linux"or platform =="linux2"or platform =="Linux"or platform =="Debian"or platform =="debian":#line:84
    print ("checking platform..")#line:85
    time .sleep (1 )#line:86
    os .system ("uname")#line:87
    time .sleep (2 )#line:88
    os .system ('clear')#line:89
    os .system ('pip install -r requirements.txt')#line:90
    print ("Sufficiently Updated! Error: ["+colors .HEADER +"NO"+colors .ENDC +"]")#line:91
    time .sleep (1 )#line:92
    os .system ('clear')#line:93
else :#line:94
    os .system ('pip install -r requirements.txt')#line:95
    print ("Sufficiently Updated! Error: ["+colors .HEADER +"NO"+colors .ENDC +"]")#line:96
    time .sleep (1 )#line:97
    os .system ('clear')#line:98
print ('''                
               `  .ss.  `               
        `-   ohy``.oo.``yho   -`        
       -sy:-'''+colors .FAIL +"""CoronaVirusTool"""+colors .ENDC +'''-:ys-       
        `-oooo+++++/oo//++oooo-`        
      -/ -oo++o++o+/++/os+/+oo- /-      
     `hyso+/+++++/os++o+/+so/+osyh`     
      ``oo/+o+/oo+///+++++/++/oo``      
   :o::/o++o+/++///////+o+/+o/+o/::o:   
   :o::/o++++/++///////+o+/+o/+o/::o:   
      ``oo/+o+/oo////+++++/++/oo``      
     `hyso+/++++//oo/+o+/+s+/+osyh`     
      -/ -oo++o++o+/++/oo//+oo- /-      
        `-oooo+++++/o+//++oooo-`        
       -sy:  -osooooooooso-  :ys-       
        `-   ohy``.oo.``yho   -`        
               `  .ss.  `               
        '''+colors .FAIL +"  By -=-> _Hwd_ <-=-"+colors .WARNING +"\n"+colors .ENDC +"              ~->  v1.0  <-~")#line:117
time .sleep (1 )#line:118
os .system ('nohup play .enable_sound.wav')#line:121
print (colors .WARNING +"Type ("+colors .HEADER +"!help"+colors .WARNING +''') to see ('''+colors .FAIL +"how to install"+colors .WARNING +")")#line:124
def menu ():#line:125
    try :#line:126
        O0OO00OOO0O0O00O0 =input (str (colors .FAIL +"\nCoronaVirus~~> "+colors .HEADER +""))#line:127
        if O0OO00OOO0O0O00O0 ==options :#line:128
            print ("")#line:129
        if O0OO00OOO0O0O00O0 ==help :#line:130
            os .system ('nohup play .enable_sound.wav')#line:131
            time .sleep (1 )#line:132
            os .system ('nohup play HelpMenu.mp3')#line:133
            print (colors .OKBLUE +''' Welcome to CoronaVirus Tool, 
                this tool is \ncreated for infectation \ndevices and for see vulnerability of \nmachines type
                ('''+colors .HEADER +"!options"+colors .OKBLUE +''') to go in the menu.''')#line:136
            menu ()#line:137
        else :#line:138
            if O0OO00OOO0O0O00O0 !=help :#line:139
                if O0OO00OOO0O0O00O0 !=options :#line:140
                    if O0OO00OOO0O0O00O0 !="1":#line:141
                       if O0OO00OOO0O0O00O0 !="2":#line:142
                            if O0OO00OOO0O0O00O0 !="3":#line:143
                                if O0OO00OOO0O0O00O0 !="4":#line:144
                                    if O0OO00OOO0O0O00O0 !="exit":#line:145
                                        if O0OO00OOO0O0O00O0 !="info":#line:146
                                            if O0OO00OOO0O0O00O0 !="clear":#line:147
                                                if O0OO00OOO0O0O00O0 !="back":#line:148
                                                    print (colors .FAIL +colors .UNDERLINE +"\n\n!!!Syntax Error!!!\n"+colors .ENDC +colors .WARNING )#line:149
                                                    menu ()#line:150
        if O0OO00OOO0O0O00O0 ==options :#line:151
            os .system ('nohup play .enable_sound.wav')#line:152
            print ('''
                [!help] to see help menu
                [!options] to see this menu
                1.Install
                2.Uninstall
                3.CheckUpgrades
                4.Back
                [back] to go in the Main menu
                [info] to see information of I.A and About
                [clear] to clear the screen
                [exit] to exit
                    ''')#line:164
            OOO0O00OO0O000O0O =input (colors .FAIL +"\nInsert Key~~> "+colors .OKBLUE )#line:165
            if OOO0O00OO0O000O0O =="1":#line:166
                os .system ('nohup play .enable_sound.wav')#line:167
                time .sleep (1 )#line:168
                os .system ('nohup play 1.mp3')#line:169
                print ("\nStarting Installation")#line:170
                time .sleep (1 )#line:171
                print ("\nThe installation required 1/2 minutes")#line:172
                time .sleep (1 )#line:173
                print ("Checking Upgrades")#line:174
                time .sleep (1 )#line:175
                os .system ('clear')#line:176
                os .system ('pip freeze > upgrades.Corona'+'pip2 freeze > upgrades.Corona'+'pip3 freeze > upgades.Corona')#line:177
                print ("\nSaving Upgrades...")#line:178
                os .system ('clear')#line:179
                time .sleep (1 )#line:180
                print ("Installation Upgrades")#line:181
                time .sleep (1 )#line:182
                os .system ('clear')#line:183
                os .system ('pip install -r upgrades.Corona')#line:184
                os .system ('clear')#line:185
                print (colors .HEADER +"Sufficiently Installed!"+colors .ENDC )#line:186
                if platform .system ()=="Linux":#line:187
                    os .system ('nohup play .enable_sound.wav')#line:188
                    print (colors .HEADER +"the folder was been copyed on CoronaVirus. Hwd. Malicious Folder move Malicius Folder on the Victim Computer")#line:189
                    time .sleep (5 )#line:190
                    os .system ('clear')#line:191
                    os .system ('nohup play coping.mp3')#line:192
                    os .system ('sudo git clone https://github.com/HwdTech010/Hwd.git')#line:193
                    os .system ('clear')#line:194
                    time .sleep (1 )#line:195
                    os .system ('nohup play copied.mp3')#line:196
                    menu ()#line:197
                if platform .system ()=="Windows":#line:198
                    os .system ('nohup play .enable_sound.wav')#line:199
                    print (colors .WARNING +"Download the folder CoronaVirus. Hwd. Malicious, and copy folder on VirusCorona Direcory"+colors .FAIL +"!!DO NOT START FILE!!"+colors .HEADER +"copy this folder on the Victim Computer")#line:200
                    os .system ('nohup play url.mp3')#line:201
                    time .sleep (1 )#line:202
                    webbrowser .open ('https://github.com/HwdTech010/Hwd.git')#line:203
                    menu ()#line:204
                os .system ('nohup play Installed.mp3')#line:205
                menu ()#line:206
            elif OOO0O00OO0O000O0O =="2":#line:207
                os .system ('nohup play .enable_sound.wav')#line:208
                print ("\n Uninstall")#line:209
                if platform .system =="Linux":#line:210
                    os .remove ("/HWD/")#line:211
                    os .system ('nohup play Uninstalled.mp3')#line:212
                    menu ()#line:213
                if platform .system ()=="Windows":#line:214
                    os .remove ("\HWD")#line:215
                    os .system ('play Uninstalled.mp3')#line:216
                    menu ()#line:217
            elif OOO0O00OO0O000O0O =="3":#line:218
                os .system ('nohup play .enable_sound.wav')#line:219
                time .sleep (1 )#line:220
                os .system ('nohup play SUpgrade.mp3')#line:221
                print ("\nChecking Upgrades")#line:222
                time .sleep (1 )#line:223
                os .system ('clear')#line:224
                os .system ('nohup play UpgradeInst.mp3')#line:225
                print ("Installing Upgrades")#line:226
                time .sleep (1 )#line:227
                os .system ('clear')#line:228
                os .system ('pip install -r upgrades.Corona')#line:229
                os .system ('clear')#line:230
                os .system ('nohup play Upgraded.mp3')#line:231
                print ("Sufficiently Upgraded!")#line:232
                menu ()#line:233
            elif OOO0O00OO0O000O0O =="4"or "back":#line:234
                os .system ('nohup play .enable_sound.wav')#line:235
                menu ()#line:236
        if O0OO00OOO0O0O00O0 =="exit":#line:237
            os .system ('nohup play .enable_sound.wav')#line:238
            time .sleep (1 )#line:239
            os .system ('nohup play GoodBye.mp3')#line:240
            time .sleep (1 )#line:241
            os .system ('clear')#line:242
            os .system ('exit && exit')#line:243
        if O0OO00OOO0O0O00O0 =="info":#line:244
            os .system ('nohup play .enable_sound.wav')#line:245
            print ('''            
 ___  ___   ___       __    ________     
|\  \|\  \ |\  \     |\  \ |\   ___ \    
\ \  \\\  \\ \  \    \ \  \\ \  \_|\ \   
 \ \   __  \\ \  \  __\ \  \\ \  \ \\ \  
  \ \  \ \  \\ \  \|\__\_\  \\ \  \_\\ \ 
   \ \__\ \__\\ \____________\\ \_______\
       Author: ~ _Hwd_
       Telegram: ~ @Hwd01011010
       Version: ~ 1.0
       License: ~ GNULinux 
                        
                        ''')#line:258
            menu ()#line:259
        if O0OO00OOO0O0O00O0 =="clear":#line:260
            os .system ('nohup play .enable_sound.wav')#line:261
            os .system ('clear')#line:262
            menu ()#line:263
    except SyntaxError :#line:265
        print (colors .FAIL +colors .UNDERLINE +"\n\n!!!Syntax Error!!!"+colors .ENDC +colors .WARNING )#line:266
        menu ()#line:267
menu ()
