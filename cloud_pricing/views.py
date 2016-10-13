import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from digital_ocean_pricing import get_price_DO_droplet
from ec2_pricing import get_price_on_demand_ec2_instance


@csrf_exempt
def get_cloud_pricing(request):
    if request.method in ['GET', 'POST']:
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

        response = HttpResponse(json.dumps(result, 'application/json'))

        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "accept, access-control-allow-headers, access-control-allow-methods, access-control-allow-origin, authid, authorization, content-type"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"

        return response
    else:
        return HttpResponse("This api supports only GET.", 'application/json')
