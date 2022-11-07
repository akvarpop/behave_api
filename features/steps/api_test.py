from behave import *
import requests
import json
from features.configuration import USER_POPRAVKA, USER_POPRAVKA_CHANGE

import pathlib
from pathlib import Path
# USER_POPRAVKA = {
#     "username": "Popravka",
#     "email": "test@test.test",
#     "groups": []
# }
# USER_POPRAVKA_CHANGE = {
#     "username": "Popravka",
#     "email": "new_test@test.test",
#     "groups": []
# }

"""create a variable to work with json file"""
path = Path(pathlib.Path.cwd(), "response.json")
path_new_user = Path(pathlib.Path.cwd(), "new_user_page.json")

@given('open site "{url}" and send data admin login "{login}" password "{password}"')
def step_impl(context, url, login, password):
    context.response = requests.get(url, auth=(login, password))
    assert context.response.status_code == 200


@given('create new user: USER_POPRAVKA "{url}" auth= login "{login}" password "{password}"')
def step_impl(context, url,  login, password):
    context.response = requests.request("POST", url, data=USER_POPRAVKA, auth=(login, password))


@step("check user create USER_POPRAVKA")
def step_impl(context):
    new_user_info = context.response.json()
    with open('new_user_page.json', 'w') as r:
        json.dump(new_user_info, r)
    assert new_user_info["username"] == USER_POPRAVKA["username"]


@given('log in and get a file json with all users "{url}" login "{login}" password "{password}"')
def step_impl(context,url, login, password):
    result = []
    response_new = requests.get(url, auth=(login, password)).json()
    temp_result = response_new['results']
    result += temp_result
    while True:
        next_url = response_new['next']
        if not next_url:
            break
        response_new = requests.get(next_url, auth=(login, password)).json()
        result += response_new['results']

    with open('response.json', 'w') as r:
        json.dump(result, r)


@then('checking the user "{user}" creation in the json file')
def step_impl(context, user):
    with open(path, 'r') as file:
        data = json.load(file)
    for item in data:
        context.value = item.get("username", None)
        if context.value == user:
            return context.value
    # assert context.value == user, "User Not Found"


@then('assert checking the user "{user}"')
def step_impl(context, user):
    assert context.value == user, "User Not Found"

@given('to change the user data in the file, we get his url from the file new_user_page.json')
def step_impl(context):
    with open(path_new_user, 'r') as file:
        data = json.load(file)
        context.url = data['url']

@then('change user USER_POPRAVKA_CHANGE (url take in Given) auth= login "{login}" password "{password}"')
def step_impl(context,  login, password):
    context.response = requests.request("PATCH", context.url, data=USER_POPRAVKA_CHANGE, auth=(login, password))

@step("check change url USER_POPRAVKA_CHANGE")
def step_impl(context):
    new_user_info = context.response.json()
    assert new_user_info["email"] == USER_POPRAVKA_CHANGE["email"], "Data users not change"

@then('delete user USER_POPRAVKA_CHANGE (url take in Given) auth= login "{login}" password "{password}"')
def step_impl(context,  login, password):
    context.response = requests.request("DELETE", context.url, data=USER_POPRAVKA_CHANGE, auth=(login, password))
    assert context.response.status_code == 204,"User not delete"

@then('assert delete the user "{user}"')
def step_impl(context, user):
    assert context.value != user, "User not delete"
