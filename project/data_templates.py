empty_html = '<html>\n<head>\n%s</head>\n<body>\n%s</body>\n</html>'

output = {
    # "status": True,
    # "code": 200,
    "note": '',
    "data": {
        "item": {},
        "list": []
    }
}
get_output = {
    # "status": True,
    # "code": 200,
    "note": '',
    "data": {
        "page": 1,
        "count": 0,
        "list": [],
        "item": {}
    }
}

log_template = {
    'params': {},
    'status': '',
    'date': '',
    'http_code': '',
    'token': '',
    'user_id': '',
    'output': {},
    'method': '',
    'url': '',
    'debug': '',
    'details': {},
    'results': {},
    'doc': {},
}

# test_step_template = {
#     'title': '',
#     'description': '',
#     'duration': 0,
#     'steps': []
# }