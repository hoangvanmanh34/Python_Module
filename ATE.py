import sys
import time
import json
import requests
import ssl
import urllib3
from datetime import datetime
from urllib3.exceptions import InsecureRequestWarning
from ast import literal_eval

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()
_create_unverified_https_context = ssl._create_unverified_context


def _SendTestTime(idata={}, iurl='https://10.228.110.91/e-alt-api/v1/test/testtimetracking/post'):
    idate = datetime.now()
    print(idate)
    '''iurl = 'https://10.228.110.91/e-alt-api/v1/test/testtimetracking/post'
    idata = {
            "ModelName": "U46C420.00",
            "Route": "OBA-WIFI",
            "Station": "T10OBAWIFI01",
            "Sn": "01234567891",
            "Result": "PASS",
            "ErrorCode": "",
            "TotalTime": 650.0,
            "FunctionTime": [
                    {"Name": "CHECK_ALIVE", "TestTime": 5.0},
                    {"Name": "INITIAL_DEVICE", "TestTime": 15.0},
                    {"Name": "CHECK_INFORMATION", "TestTime": 5.0},
                    {"Name": "CHECK_WIFI2G", "TestTime": 150.0},
                    {"Name": "CHECK_WIFI5G", "TestTime": 250.0},
                    {"Name": "FACTORY_RESET", "TestTime": 30.0},
                    {"Name": "CHECK_FACTORY_RESET", "TestTime": 200.0}
                ]
        }'''
    try:
        idata = literal_eval(str(idata))
    except Exception as e:
        print(idata)
        print('***Data not available***')
        print(e)
        return
    print(idata)
    #idata = json.loads(str(idata))
    #idata = json.dumps(str(idata))
    #print(idata)
    print(type(idata))
    print('**********************************************')
    for i in range(0, 5):
        try:
            if SendTestTime(idata, iurl): break
        except Exception as e:
            print(e)
            pass

def SendTestTime(idata={}, iurl='https://10.228.110.91/e-alt-api/v1/test/testtimetracking/post'):
    try:
        iupload = requests.post(url=iurl, json=idata, timeout=5, verify=False)
        print(iupload.text)
        if str(iupload.text).find('200') < 0:
            return False
    except Exception as e:
        print(e)
        return False
    return True

def _GetMaintain(iurl='http://200.168.130.25/ATE/api/ATEMachines/info/T16C382FT101/20220112'):
    idate = datetime.now()
    print(idate)
    try:
        print('**********************************************')
        for i in range(0, 5):
            try:
                if GetMaintain(iurl): break
            except Exception as e:
                print(e)
                pass
    except Exception as e:
        print('***EX***')
        print(e)
        return
    


def GetMaintain(iurl=''):
    try:
        if iurl!='': 
            iinfo = requests.get(url=iurl, timeout=5, verify=False)
            print(iinfo.text)
            print(iinfo.status_code)
            if str(iinfo.status_code).find('200') < 0:
                return False
    except Exception as e:
        print(e)
        return False
    return True
print('==========')
iargv = sys.argv
liargv = len(iargv)
print(liargv)

if liargv > 1:
    idate = datetime.now()
    print(idate)
    if liargv == 2: _GetMaintain(iargv[1])

#time.sleep(5)
