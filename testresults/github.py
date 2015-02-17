import requests
import json

def call_api(owner, repo, subpath, data=None, username=None, password=None):
    """ Takes a subpath under the repository (ex: /releases) and returns the json data from the api """
    api_url = 'https://api.github.com/repos/%s/%s%s' % (owner, repo, subpath)
    # Use Github Authentication if available for the repo
    kwargs = {}
    if username and password:
        kwargs['auth'] = (username, password)

    if data:
        resp = requests.post(api_url, data=json.dumps(data), **kwargs)
    else:
        resp = requests.get(api_url, **kwargs)

    try:
        data = json.loads(resp.content)
        return data
    except:
        return resp.status_code
