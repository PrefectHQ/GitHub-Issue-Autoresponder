import os

import marvin
from marvin import ai_fn
from prefect import flow


@flow()
def main():
    print("Hello, world!")
