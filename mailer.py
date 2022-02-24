
import os
import sys

import requests


# Custom Exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class MissingSendTo(Error):
    """Missing email address to send to"""

    def __init__(self):
        if (__name__ == "__main__"):
            sys.exit("Missing email address to send to")

    def __str__(self) -> str:
        return "Missing email address to send to"


class MissingSubject(Error):
    """Missing email subject"""

    def __init__(self):
        if (__name__ == "__main__"):
            sys.exit("Missing email subject")

    def __str__(self) -> str:
        return "Missing email subject"


class MissingContent(Error):
    """Missing Email Content"""

    def __init__(self):
        if (__name__ == "__main__"):
            sys.exit("Missing Email Content")

    def __str__(self) -> str:
        return "Missing Email Content"


class AnonymousEmail:
    def __init__(self, e_send_to: str = None,
                 e_subject: str = None,
                 e_content: str = None):
        self.e_send_to = e_send_to
        self.e_subject = e_subject
        self.e_content = e_content

        self.api_link = "http://anonymouse.org/cgi-bin/anon-email.cgi"
        self.user_agent = 'Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]'
        self.headers = {
            'Host': 'anonymouse.org',
            'User-Agent': self.user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://anonymouse.org/anonemail.html',
            'Connection': 'close',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

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
            print("[Content] (enter 'done' when done)")
            final_content = ""
            count = 0
            while True:
                count += 1
                temp = input(f"{count}: ")
                if temp.strip().lower().startswith("done"):
                    break
            self.e_content = final_content
        else:
            self.e_content = e_content

    def getData(self):
        if self.e_send_to is None:
            raise MissingSendTo

        if self.e_subject is None:
            raise MissingSubject

        if self.e_content is None:
            raise MissingContent

        return {
            'to': self.e_send_to,
            'subject': self.e_subject,
            'text': self.e_content
        }

    def sendEmail(self, display_info: bool = True):
        session = requests.Session()
        rth = session.post(self.api_link,
                           headers=self.headers,
                           data=self.getData())

        if display_info:
            if '200' in rth.text:
                print("[+] Sending Email")
            else:
                print("[+] Sending Email")
                print(
                    "[+] In order to increase your privacy, the anonymous e-mail will be randomly delated upto 12 hours")
                sys.exit()
