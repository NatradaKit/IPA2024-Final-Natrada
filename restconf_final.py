import json
import requests
requests.packages.urllib3.disable_warnings()
import os
from dotenv import load_dotenv

load_dotenv()
username = os.environ.get('TELNET_USER')
password = os.environ.get('TELNET_PASSWORD')

# Router IP Address is 10.0.15.181-184
api_url = "https://10.0.15.182/restconf/data/ietf-interfaces:interfaces/interface=Loopback65070082"

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = {"Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
            }
basicauth = (username, password)


def create():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070082",
            "description": "",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                    "ip": "172.30.82.1",
                    "netmask": "255.255.255.0"
                    }
                ]
            },
                "ietf-ip:ipv6": {}
        }
    }

    resp = requests.put(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070082 is created successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def delete():
    resp = requests.delete(
        api_url, 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 66070082 is deleted successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def enable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070082",
            "enabled": True
        }
    }

    resp = requests.patch(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 66070082 is enabled successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def disable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070082",
            "enabled": False
        }
    }

    resp = requests.patch(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 66070082 is disenabled successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def status():
    api_url_status = "https://10.0.15.182/restconf/data/ietf-interfaces:interfaces-state/interface=Loopback65070082"
    
    resp = requests.get(
        api_url_status, 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        admin_status = response_json["ietf-interfaces:interface"]["admin-status"]
        oper_status = response_json["ietf-interfaces:interface"]["oper-status"]
        if admin_status == 'up' and oper_status == 'up':
            return "Interface loopback 66070082 is enabled"
        elif admin_status == 'down' and oper_status == 'down':
            return "Interface loopback 66070082 is disabled"
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "No Interface loopback 66070082"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        print("Response Text:", resp.text)