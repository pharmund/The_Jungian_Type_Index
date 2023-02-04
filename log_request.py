def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearchlog', 'a') as log:
        print(req, res, file = log)