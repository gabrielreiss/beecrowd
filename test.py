import requests
import pytest


base_url = f'www.udebug.com'

list_inputs = f'/input_api/input_list/retrieve.json'

judge_alias = 'URI Online Judge'
problem_id = 2061

input_test = f'/input_api/input/retrieve.json'

#assert
output_test = f'/output_api/output/retrieve.json'


def buscar():
    request = requests.get(f'{base_url}{list_inputs}?judge_alias={judge_alias}+problem_id={problem_id}')
    print(requests.content)
    

if __name__ == "__main__":
    buscar()
    
