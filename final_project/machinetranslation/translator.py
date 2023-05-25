# sudo python3 -m pip install --upgrade --force pip
# pip3 install --upgrade ibm-watson
# pip3 install ibm-cloud-sdk-core
# pylint: disable=unused-import,line-too-long,bare-except,import-error,invalid-name,missing-final-newline

"""This is a translator module"""

import os
import ibm_watson

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

url_lt= os.environ['url']
apikey_lt=os.environ['apikey']
version_lt='2018-05-01'
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
lt = language_translator

def englishtofrench(englishText):
    """This class does english to french translation"""

    if  not(bool(englishText)):
        return None

    translation = lt.translate(text=englishText, model_id="en-fr").get_result()
    return translation['translations'][0]['translation']

def frenchToEnglish(frenchText):
    """This class does french to english translation"""

    if  not(bool(frenchText)):
        return None
    translation = lt.translate(text=frenchText, model_id="fr-en").get_result()
    return translation['translations'][0]['translation']