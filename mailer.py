
import os
import sys

import requests


class AnonymousEmail:
    def __init__(self, e_send_to: str = None,
                 e_subject: str = None,
                 e_content: str = None):
        self.e_send_to = e_send_to
        self.e_subject = e_subject
        self.e_content = e_content

    def setSendTo(self, e_send_to: str = None):
        if e_send_to is None:
            self.e_send_to = input("[To]: ")
        else:
            self.e_send_to = e_send_to

    def setSubject(self, e_subject: str = None):
        if e_subject is None:
            self.e_subject = input("[Subject]: ")
        else:
            self.e_subject = e_subject

    def setContent(self, e_content: str = None):
        if e_content is None:
            self.e_content = input("[Content]: ")
        else:
            self.e_content = e_content

    def getData(self):
        if self.e_send_to is None:
            pass

        if self.e_subject is None:
            pass

        if self.e_content is None:
            pass

        data = {
            'to': self.e_send_to,
            'subject': self.e_subject,
            'text': self.e_content
        }


api_link = "http://anonymouse.org/cgi-bin/anon-email.cgi"
user_agent = 'Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]'
headers = {
    'Host': 'anonymouse.org',
    'User-Agent': user_agent,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://anonymouse.org/anonemail.html',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded'
}


session = requests.Session()
rth = session.post(api_link,
                   headers=headers,
                   data=data)

if '200' in rth.text:
    print("[+] Sending Email")
else:
    print("[+] Sending Email")
    print("[+] In order to increase your privacy, the anonymous e-mail will be randomly delated upto 12 hours")
    sys.exit()
