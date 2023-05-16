#!/usr/bin/env python3

from fastapi.testclient import TestClient
from initial_phase.src.api import api

client = TestClient(api)

expected_resp = {"api_name": "simple_fastapi", "api_state": "active"}


def test_get_events():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == expected_resp
