import configuration
import requests
import data


# новый заказ, POST запрос
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.header_content)


# Получение заказа, GET запрос
def get_order(parameters):
    return requests.get(configuration.URL_SERVICE + configuration.REQUEST_ORDER,
                        params=parameters)
