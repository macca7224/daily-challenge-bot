#!/usr/bin/python3

import os
import random

from dotenv import load_dotenv
import requests

load_dotenv()

maps = [
    {'name': 'A Balanced Australia', 'id': '60afb9b2dcdbe60001438fa6'},
    {'name': 'An Updated Australia', 'id': '6346e9fa501e83f27df9b372'},
    {'name': 'An Improved Australia', 'id': '64313bd5c716f7d2ec73a7a3'},
    {'name': 'An Arbitrary Rural Australia', 'id': '644fc37ac223d496e4994d63'},
    {'name': 'An Extensive Australia', 'id': '65e4930a510a6181195e012f'}
]

rare_maps = [
    {'name': 'An Updated Ai Generated Australia', 'id': '6409bc58e720ad96fc68fb63'},
    {'name': 'Australia', 'id': 'australia'},
    {'name': 'A Combined NZ and Australia', 'id': '64b7ce3ae42625d73c66d2b6'},
    {'name': 'Dirty Australia', 'id': '63f3c4e8c05a4bc09cfa6d20'},
    {'name': 'A Balanced Populated Australia', 'id': '6391cbdfff0757688ea6e9fe'},
    {'name': 'A Pinpointable Australia', 'id': '6393e166dc2e85eab0af0fd1'}
]

cookies = {
    'devicetoken': os.getenv('DEVICE_TOKEN'),
    '_ncfa': os.getenv('NCFA'),
    'session': os.getenv('SESSION'),
}


def create_daily_challenge():
    # Choose map
    standard_probability = 4/5

    if random.random() < standard_probability:
        map_pool = maps
    else:
        map_pool = rare_maps

    chosen_map = random.choice(map_pool)
    map_name = chosen_map['name']
    map_id = chosen_map['id']

    time_limit = random.choice([10, 20, 30, 40, 50, 60])
    if 'Pinpointable' in map_name:
        time_limit += 20

    json_data = {
        'map': map_id,
        'forbidMoving': True,
        'timeLimit': time_limit,
        'rounds': 5
    }

    # 50/50 chance of NM or NMPZ
    if random.random() < 0.5 or 'Pinpointable' in map_name:
        # NM
        json_data['forbidRotating'] = False
        json_data['forbidZooming'] = False
        game_format = 'NM'
    else:
        # NMPZ
        json_data['forbidRotating'] = True
        json_data['forbidZooming'] = True
        game_format = 'NMPZ'

    token = requests.post(
        'https://www.geoguessr.com/api/v3/challenges',
        cookies=cookies,
        json=json_data
    ).json()['token']

    message = f'{map_name}, {game_format}, {time_limit}s timer'

    return token, message
