import requests


class SQLQuestionMapper(object):

    def __init__(self):
        self.url = "http://localhost:8400/sempre"
        self.query_params = {
            'format': 'json'
        }

    def convert(self, question):
        immutable_params = self.query_params.copy()
        immutable_params['q'] = question

        response = requests.get(self.url, params=immutable_params)

        if response.status_code != 200:
            raise ValueError("Response returned with status code = %s instead of 200" % response.status_code)

        candidates = response.json()['candidates']

        if len(candidates) == 0:
            print("No candidates")
            return ""

        # the last replace can be a bit dangerous
        return candidates[0]['value'].replace('(string "', '').replace('")', '')


#print(SQLQuestionMapper().convert("client x tenor"))