import json

from tornado.web import RequestHandler


class JsonHandler(RequestHandler):
    def prepare(self):
        if self.request.body:
            try:
                json_data = json.loads(self.request.body)
                self.request.arguments.update(json_data)
            except ValueError:
                message = 'Unable to parse JSON.'
                self.send_error(400, message=message)  # Bad Request

        self.response = dict()

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def write_error(self, status_code, **kwargs):
        if 'message' not in kwargs:
            if status_code == 405:
                kwargs['message'] = 'Invalid HTTP method.'
            elif status_code == 404:
                kwargs['message'] = 'Not found.'
            else:
                kwargs['message'] = 'Unknown error.'

        error = {
            'status': status_code,
            'error': kwargs['message']
        }

        self.response['error'] = error
        self.write_json()

    def write_json(self):
        output = json.dumps(self.response)
        self.write(output)

    def write_empty(self):
        self.set_status(204)
        self.write('')
