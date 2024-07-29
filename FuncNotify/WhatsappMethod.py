"""Sends whatsapp messages to users via a whatsapp number and twilio

Setup:
    1. Create a twilio accountt and purchase a (free) number. No credit card. Quick guide: https://www.twilio.com/docs/sms/quickstart/python
        1b. Per account, one has limited notifications.
    2. Grab the twilio account, API token, twilio phone and your phone to be added to .env
"""

import NotifyMethods as NotifyMethods # Using the predefined functions from the abstract class
from .api import time_func

# Specify here other Packages to be imported specific for whatsapp Alerts.
from twilio.rest import Client

def time_Whatsapp(func=None, use_env: bool=True, env_path: str=".env", update_env: bool=False, whatsapp_number=None, twilio_number: str=None, twilio_account_sid: str=None, twilio_token: str=None, *args, **kwargs): # Include something to check the rest of the arguments in the word
    """TODO Decorator specific for xNotifyx, if no credentials specified, it wil fill in with .env variables.

    Args:
        func (function, optional): In case you want to use time_func as a pure decoratr without argumetns, Alert serves as
        the function. Defaults to None.
        use_env (str, optional): Loads .env file envionment variables. Defaults to False
        env_path (str, optional): path to .env file. Defaults to ".env".
        update_env (bool, optional): whether to update the .env file to current. Always updatess on
        initialization. Defaults to False.

        Insert remaining args here
        NOTE add all key word arguments that could be used by the class to enable more accurate mesaging
        [variable] ([type], optional): [Summary]. Defaults to [Default]"""
    return time_func(*args, **kwargs, **locals(), NotifyMethod="Whatsapp")

class WhatsappMethod(NotifyMethods):
    """TODO Summaraize exactly how xNotifyxMethod will notify the end user and what platform.
    """

    __slots__ = ("__whatsappnumber,__twilionumber,__client") # List all instance variables here in string form, saves memory,
                            # optional, don't forget `__`

    def __init__(self, *args, **kwargs):
        """TODO Specify key word arguments in the init as var=xyz and define them as instances
        """
        super().__init__(*args, **kwargs)

    def _set_credentials(self, token: str=None, *args, **kwargs)->None:
        """TODO If instance variables are not defined, define environment variables here
        Then add the env variables to my.env for your specific environment variables
        Finally add the variable name and equal sign in a new section in template.env
        for future use. Extension of __init__

        Use self.str_or_env(str | any, str) to prevent accidentally passing int or long as arguments,
        and also to allow users to define some values

        NOTE Try and keep all client errors here, and try and catch as many CredentialErrors
        here by making some api calls here
        NOTE use `__` to make all private information sorta private!!!

        Args:
            Add your own and document!
        """
        self.__whatsappnumber=self._type_or_env(whatsapp_number, "WHATSAPP_NUMBER")
        self.__twilio_number = self._type_or_env(twilio_number, "TWILIO_NUMBER")
        self.__client = Client(self._type_or_env(twilio_account_sid, "TWILIO_ACCOUNT_SID"), self._type_or_env(twilio_token, "TWILIO_TOKEN"))


    def send_message(self, message: str):
        try:
            self.__client.messages.create(body=message,
                       from_=__twilio_number,
                       to=__whatsappnumber)
            pass
        except Exception as ex:
            raise ex


whatsapp=WhatsappMethod()
whatsapp.send_message("hello")