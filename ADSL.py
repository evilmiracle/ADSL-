#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time
import os
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
os.popen('rasdial /DISCONNECT')
os.popen('rasdial /DISCONNECT')
os.popen('rasdial /DISCONNECT')
os.popen('rasdial /DISCONNECT')


class mythread(threading.Thread):

    def __init__(self, ThreadID, name):
        threading.Thread.__init__(self)

        self.ThreadID = ThreadID
        self.name = name

    def run(self):
        print "Starting thread:%s" % self.name
        os.popen('rasdial /DISCONNECT')
        threadLock = threading.Lock()
        while True:
            try:
                threadLock.acquire()
                conn = os.popen(
                    'rasdial "xaxa" "057916870790" "438101"').read()
                print conn
                time.sleep(4)
                print 'IP:    ' + urllib2.urlopen('http://www.mksec.net/hx/ip.php').read()
                get = urllib2.urlopen(
                    'http://zt.luoohu.com/api/Index160428/SaveClientInfo?callback=jQuery1111032658216467291434_1464144198502&StreetId=5&CommunityId=40&_=1464144198512').read().decode('utf-8')
                get1 = urllib2.urlopen(
                    'http://zt.luoohu.com/api/Index160428/Vote?callback=jQuery111105685882110217748_1465256374552&PId=68&DataCategory=1&_=1465256374615').read().decode('utf-8')  # 033
                get2 = urllib2.urlopen(
                    'http://zt.luoohu.com//api/Index160428/Vote?callback=jQuery111105685882110217748_1465256374552&PId=38&DataCategory=1&_=1465256374616').read().decode('utf-8')  # 003
                print get1 + get2
                conn1 = os.popen('rasdial /DISCONNECT').read()
                print 'disconnects success!!!'
                threadLock.release()
            except Exception, e:
                print 'error' + str(e)
                os.popen('rasdial /DISCONNECT')
                os.popen('rasdial /DISCONNECT')
                os.popen('rasdial /DISCONNECT')
                os.popen('rasdial /DISCONNECT')
                time.sleep(2)
        print "End thread:%s" % self.name


def main():
    try:
        os.popen('rasdial /DISCONNECT')
        threads = []
        thread1 = mythread(1, "Thread-1")
        thread2 = mythread(2, "Thread-2")
        thread3 = mythread(3, "Thread-3")
        thread1.start()
        thread2.start()
        thread3.start()
        threads.append(thread1)
        threads.append(thread2)
        threads.append(thread3)
        os.popen('rasdial /DISCONNECT')
        for j in threads:
            j.join()
    except:
        os.popen('rasdial /DISCONNECT')
        print "Start thread Error"
    print "Exting Main Thread"


if __name__ == '__main__':
    main()
