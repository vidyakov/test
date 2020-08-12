import json
import requests

from .models import Friend


def save_user_photo(backend, user, response, *args, **kwargs):
    if kwargs.get('is_new'):
        user.photo = response.get('photo')
        user.save()


def save_user_friends(backend, user, response, *args, **kwargs):
    if kwargs.get('is_new'):
        url = 'https://api.vk.com/method/friends.get'
        params = {
            'access_token': response.get('access_token'),
            'user_id': response.get('id'),
            'order': 'random',
            'count': 5,
            'name_case': 'nom',
            'fields': 'photo_100,domain',
            'offset': 0,
            'v': 5.122
        }
        response = requests.get(url, params=params)
        for item in json.loads(response.text)['response']['items']:
            new_friend = Friend(
                first_name=item.get('first_name'),
                last_name=item.get('last_name'),
                photo_url=item.get('photo_100'),
                domain=item.get('domain')
            )
            user.friend_set.add(new_friend, bulk=False)
