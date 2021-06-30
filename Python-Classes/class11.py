import requests


def return_data_zip_code(zipcode):
    response = requests.get('https://viacep.com.br/ws/{}/json/' .format(zipcode))
    print(response.status_code)
    print(response.json())
    print(type(response.json()))
    data_zip_code = response.json()
    print(data_zip_code['logradouro'])
    print(data_zip_code['complemento'])
    return data_zip_code


def return_data_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/' .format(pokemon))
    data_pokemon = response.json()
    return data_pokemon


def return_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    response = return_response('https://www.mdpi.com/journal/ai')
    print(response)

    # return_data_zip_code('01001000')
    # data_pokemon = return_data_pokemon('pikachu')
    # print(data_pokemon['sprites']['front_shiny'])