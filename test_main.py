from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# TESTING GET JOKE

def test_joke_ramdon():
    response = client.get("/jokes")
    assert response.status_code == 200

def test_joke_chuck():
    response = client.get("/jokes/chuck")
    assert response.status_code == 200

def test_joke_dad():
    response = client.get("/jokes/dad")
    assert response.status_code == 200

def test_joke_undefined():
    response = client.get("/jokes/undefined")
    assert response.status_code == 422

# TESTING POST JOKE

def test_insert_joke_values_1():
    param={"joke":"This is a joke"}
    response = client.post("/jokes",json=param)
    joke=response.json()
    assert response.status_code == 200
    assert joke['joke'] == "This is a joke"

def test_insert_joke_values_2():
    param={"joke":"This is another joke"}
    response = client.post("/jokes",json=param)
    joke=response.json()
    assert response.status_code == 200
    assert joke['joke'] == "This is another joke"

def test_insert_joke_wrong_param():
    response = client.post("/jokes?number=a")
    assert response.status_code == 422

def test_insert_joke_no_param():
    response = client.post("/jokes")
    assert response.status_code == 422

# TESTING UPDATE JOKE
def test_update_joke_values_1():
    param={"number":1,"joke":"Updated joke"}
    response = client.patch("/jokes",json=param)
    assert response.status_code == 200
    assert response.json() == {'number': 1,"joke":"Updated joke"}

def test_update_joke_values_2():
    param={"number":2,"joke":"Another updated joke"}
    response = client.patch("/jokes",json=param)
    assert response.status_code == 200
    assert response.json() == {'number': 2,"joke":"Another updated joke"}

def test_update_joke_values_3():
    param={"number":100,"joke":"Updated joke"}
    response = client.patch("/jokes",json=param)
    assert response.status_code == 404

def test_update_joke_values_4():
    param={"number":1,"joke":""}
    response = client.patch("/jokes",json=param)
    assert response.status_code == 422

def test_update_joke_param_string():
    response = client.patch("/jokes?number=a")
    assert response.status_code == 422

def test_update_joke_no_param():
    response = client.patch("/jokes")
    assert response.status_code == 422

# TESTING DELETE JOKE

def test_delete_joke_values_1():
    param={"number":1}
    response = client.delete("/jokes",params=param)
    assert response.status_code == 200
    assert response.json() == {'ok': True}

def test_delete_joke_values_2():
    param={"number":100}
    response = client.delete("/jokes",params=param)
    assert response.status_code == 404

def test_delete_joke_param_string():
    param={"number":"a"}
    response = client.delete("/jokes",params=param)
    assert response.status_code == 422

def test_delete_joke_no_param():
    response = client.delete("/jokes")
    assert response.status_code == 422

# TESTING LEAST_COMMON_MULTIPLE
def test_least_common_multiple_values_1():
    response = client.get("/least-common-multiple?numbers=4&numbers=6&numbers=8")
    assert response.status_code == 200
    assert response.json() == {'least_common_multiple': 24}

def test_least_common_multiple_values_2():
    response = client.get("/least-common-multiple?numbers=2&numbers=3&numbers=6")
    assert response.status_code == 200
    assert response.json() == {'least_common_multiple': 6}

def test_least_common_multiple_param_string():
    response = client.get("/least-common-multiple?numbers=a")
    assert response.status_code == 422

def test_least_common_multiple_no_params():
    response = client.get("/least-common-multiple")
    assert response.status_code == 422

# TESTING ADDITION
def test_addition_five():
    response = client.get("/addition?number=5")
    assert response.status_code == 200
    assert response.json() == {'number': 6}

def test_addition_six():
    response = client.get("/addition?number=6")
    assert response.status_code == 200
    assert response.json() == {'number': 7}

def test_addition_param_string():
    response = client.get("/addition?number=a")
    assert response.status_code == 422

def test_addition_no_params():
    response = client.get("/addition")
    assert response.status_code == 422