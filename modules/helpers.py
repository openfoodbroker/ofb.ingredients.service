import requests
import pprint
import os
import yaml
import re



def get_config_yml(path, stage_name):
    with open(path) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data["stages"][stage_name]


def plainfile2list(path):
    data = []
    with open(path) as fp:
        for line in fp:
            data.append(line.strip())
    return data

