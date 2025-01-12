import config
import requests


class API:
    backend_server = config.wordle_backend_server

    @classmethod
    def daily(cls, word):
        url = "/daily"
        parameters = {"guess": word, "size": config.word_length}

        return requests.get(
            f"{API.backend_server}{url}",
            params=parameters,
        ).json()
