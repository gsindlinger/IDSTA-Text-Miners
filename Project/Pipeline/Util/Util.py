import requests


def get_html_resource_to_json(base: str, path: str, token: str, headers=None, params=None):
    '''Send request and get response in json format.'''
    # Generate request URL
    requrl = '/'.join([base, path])
    token = "Bearer {}".format(token)
    if headers:
        headers['Authorization'] = token
    else:
        headers = {"Authorization": token}

    # Get response object from querying genius api
    response = requests.get(url=requrl, params=params, headers=headers)
    response.raise_for_status()
    return response.json()
