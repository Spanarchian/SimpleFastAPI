#!/usr/bin/env python3

from fastapi import FastAPI

api = FastAPI()


@api.get("/")
async def root():
    return {"api_name": "simple_fastapi", "api_state": "active"}


# Time to think
