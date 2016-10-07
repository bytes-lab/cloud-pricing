import json


"""
key: memory-cpu
val: [monthly, default storage]
"""
DO_MONTHLY_PRICE = {
    '0.5-1': [5, 20],
    '1-1': [10, 30],
    '2-2': [20, 40],
    '4-2': [40, 60],
    '8-4': [80, 80],
    '16-8': [160, 160],
    '16-2': [120, 30],
    '32-4': [240, 90],
    '64-8': [480, 200],
    '128-16': [960, 340],
    '224-32': [1680, 500]
}


def get_price_DO_droplet(filter_):
    result = dict(filter_)

    try:
        key = '{}-{}'.format(filter_['memory'], filter_['cpu'])
    except Exception, e:
        result['error'] = 'Format is wrong. Required parameters are `cpu` (number of CPUs), `memory` (size of memory in GB), `storage` (size of memory in GB)'
        return result

    try:
        default = DO_MONTHLY_PRICE[key]
        storage = int(filter_.get('storage', '0'))
    except Exception, e:
        result['error'] = 'There is no such instance. Please check parameters again.'
        return result
        
    if default[1] >= storage:
        extra = 0
    else:
        extra = (storage - default[1]) / 10.0

    monthly = default[0] + extra
    result['Daily'] = "{0:.2f}".format(monthly / 24.0)
    result['Monthly'] = "{0:.2f}".format(monthly)

    return result


if __name__ == "__main__":

    filter_ = {
        'cpu': '1', 
        'memory': '0.5', 
        'storage': '50'
    }

    print (json.dumps(get_price_DO_droplet(filter_)))

