import config
import requests


class API:
    backend_server = config.wordle_backend_server

    @classmethod
    def daily(cls, word):
        url = "/daily"
        parameters = {"guess": word, "size": config.word_length}

        response = requests.get(
            f"{API.backend_server}{url}",
            params=parameters,
        )

        if response.status_code != 200:
            raise Exception(f"API call error: {response.reason}")
        else:
            return response.json()
