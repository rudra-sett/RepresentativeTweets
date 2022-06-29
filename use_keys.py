import io
import os

key_file = open("KEYS","r")

api_key = key_file.readline().rstrip()
api_secret = key_file.readline().rstrip()
bearer_key = key_file.readline().rstrip()

key_file.close()

