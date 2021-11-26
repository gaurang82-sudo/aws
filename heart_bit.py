
import ec2_metadata 
import requests
from datetime import datetime
url= 'http://3.12.85.239:8000/api/customeraws/'
net = ec2_metadata.NetworkInterface(mac=ec2_metadata.ec2_metadata.mac)
ec2_metadata = ec2_metadata.ec2_metadata

def send_heartbit():
    time=datetime.now()
    data = {'instance_id':ec2_metadata.instance_id,'last_time':time.strftime("%H:%M:%S"),'mac':ec2_metadata.mac,'owner_id':net.owner_id,'vpc_id':net.vpc_id}
    updated_url = f'{url}{int(ec2_metadata.account_id)}'
    Response = requests.post(updated_url,data)
    if Response.status_code == 200:
        return True
    else:
       	return False

def login():
    time=datetime.now()
    password=input('enter password')
    aws_id=ec2_metadata.account_id
    data = {'password':password,'aws_id':aws_id,'instance_id':ec2_metadata.instance_id,'last_time':time.strftime("%H:%M:%S"),'mac':ec2_metadata.mac,'owner_id':net.owner_id,'vpc_id':net.vpc_id}

    url='http://3.12.85.239:8000/api/login'
    Responce = requests.post(url,data)
    if Responce.status_code == 200:
        return True
    else:
        return False



