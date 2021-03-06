import pytest

import sys

from Controller import Controller
from Model import Model
from View import View


from api import is_palindrome
from api import app

from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_line(monkeypatch):
    view = View()
    model = Model()
    controller = Controller(model, view)

    monkeypatch.setattr(View, 'read', lambda _: "toto")
    controller.get_line()
    assert model.lines == ['TOTO']

    controller.get_line()
    assert model.lines == ['TOTO', 'TOTO']


def test_get_uppercase():
    response = client.get("/text/uppercase?source=toto")
    assert response.json() == {"result": "TOTO"}

def test_is_palindrome():
    response = client.get("/text/palindrome?source=toto")
    assert response.json() == {"result": False}

    response = client.get("/text/palindrome?source=kayak")
    assert response.json() == {"result": True}

