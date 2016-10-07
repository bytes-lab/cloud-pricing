import json

from django.http import HttpResponse
from digital_ocean_pricing import get_price_DO_droplet
from ec2_pricing import get_price_on_demand_ec2_instance


def get_cloud_pricing(request):
    if request.method == 'GET':
        result = []
        params = json.loads(request.body)
        for param in params:
            cloud = param.get('cloud')
            if cloud == 'digital ocean':
                result_ = get_price_DO_droplet(param)
            elif cloud == 'aws ec2':
                result_ = get_price_on_demand_ec2_instance(param)
            else:
                result_ = dict(param)
                result_['error'] = 'Please specify correct cloud type. e.g) `cloud`: `aws ec2` or `digital ocean`'
            result.append(result_)

        return HttpResponse(json.dumps(result, 'application/json'))
    else:
        return HttpResponse("This api supports only GET.", 'application/json')