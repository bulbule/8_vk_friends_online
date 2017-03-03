import vk
from getpass import getpass


APP_ID = 5904450


def get_user_login():
    return input("Enter your login:")


def get_user_password():
    return getpass("Enter your password:")


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_ids = api.friends.getOnline()
    friends_online = api.users.get(user_ids=friends_ids)
    return friends_online


def output_friends_to_console(friends_online):

    for friend in friends_online:
        print('{} {}'.format(friend['first_name'], friend['last_name']))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
