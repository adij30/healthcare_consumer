import requests
print('hi')
address_url = 'http://127.0.0.1:8000/api/healthcare/address/'


def get_all_address():
    # response = requests.get(address_url, headers={'Authorization': 'Token 1ebccfd17553fc7d4160eab5f50527a22df576f8'})
    response = requests.get(address_url)

    print(response.json())


get_all_address()