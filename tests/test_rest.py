import requests
from pytest_voluptuous import S
from requests import Response
from Schema.Schema import user, user_unsuccessful


def test_get_users_status_code():
	response = requests.get(url="https://reqres.in/api/users/2")
	
	assert response.status_code == 200
	assert response.json


def test_post_users():
	response: Response = requests.post(
		url="https://reqres.in/api/users",
		json={
			"name": "Alena",
			"job": "QA"
		})
	
	assert response.status_code == 201
	assert response.json().get("name") == "Alena"
	assert response.json().get("job") == "QA"


def test_post_unknown():
	response: Response = requests.get(url="https://reqres.in/api/unknown")
	assert response.status_code == 200
	assert S(user) == response.json()


def test_post_register():
	response: Response = requests.post(
		url="https://reqres.in/api/register",
		json={
			"email": "eve.holt@reqres.in",
			"password": "pistol"
		})
	assert response.status_code == 200
	assert response.json().get("id") == 4
	assert response.json().get("token") == "QpwL5tke4Pnpja7X4"


def test_user_unsuccessful():
	response: Response = requests.post(
		url="https://reqres.in/api/login",
		json=
		{
			"email": "peter@klaven"
		}
	)
	assert response.status_code == 400
	assert S(user_unsuccessful) == response.json()
	assert response.json()["error"] == "Missing password"
