# OpsClick_BE_Pricing


After docker-compose up run this command:

curl -H "Accept: application/json" -H "Content-type: application/json" -X GET -d '[{"cloud": "digital ocean", "cpu": "1", "memory": "0.5"}, {"cloud": "digital ocean", "cpu": "4", "memory": "8", "storage": "120"}, {"cloud": "aws ec2", "filter_os_type": "sles", "filter_region": "us-east-1", "filter_type": "m4.large"}, {"cloud": "aws ec2", "filter_os_type": "sles", "filter_region": "us-east-1", "filter_type": "t2.large"}]' http://localhost:8000/api/cloud_pricing/|json_pp
