# OpsClick_BE_Pricing

## Purpose

Generalized API for price of cloud services:

- AWS
- digital ocean

Input:
	all info for instances.	
	m1.large, small, ...
	HW size

Digital Ocean:
	droplet.


Output: 
	price - daily / monthly

## Reference

http://a0.awsstatic.com/pricing/1/ec2/sles-od.min.js
http://stackoverflow.com/questions/7334035/get-ec2-pricing-programmatically
https://github.com/erans/ec2instancespricing/blob/master/ec2instancespricing/ec2instancespricing.py

## Run

	sudo docker-compose build
	sudo docker-compose up

## Sample curl

curl -H "Accept: application/json" -H "Content-type: application/json" -X GET -d '[{"cloud": "digital ocean", "cpu": "1", "memory": "0.5"}, {"cloud": "digital ocean", "cpu": "4", "memory": "8", "storage": "120"}, {"cloud": "aws ec2", "filter_os_type": "sles", "filter_region": "us-east-1", "filter_type": "m4.large"}, {"cloud": "aws ec2", "filter_os_type": "sles", "filter_region": "us-east-1", "filter_type": "t2.large"}]' http://localhost:8000/api/cloud_pricing/|json_pp
