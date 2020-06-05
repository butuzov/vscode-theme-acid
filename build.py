#!/usr/bin/env python3

import json, yaml
import time
from random import choice as ch

import hashlib


def color():
    """ Generate random color  """
    return "#" + ''.join([ch('0123456789ABCDEF') for j in range(6)])


def dpath(dict, path):
    tmp = dict

    for i in path.split("."):
        tmp = tmp.get(i, {})
    return tmp


def main():

    files = {}  # hash storage

    def is_changed(file):
        hasher = hashlib.md5()
        with open(file, "r") as f:
            buf = f.read()
            hasher.update(buf.encode())

        if files.get(file, None) == hasher.hexdigest():
            return False

        files[file] = hasher.hexdigest()
        return True

    colors = "src/colors.yaml"
    params = "src/settings.yml"

    def value_as_color(value):
        if value == '_':
            param_value = color()
        elif "/" in value:
            rgb, a = value.split("/")
            param_value = dpath(data_colors, rgb) + dpath(data_colors, a)
        elif "." in value:
            param_value = dpath(data_colors, value)
        elif value[0] == "#":
            param_value = value

        return param_value

    theme = {}
    try:
        with open("theme.json", "r") as f:
            theme = json.load(f)
    except FileNotFoundError:
        theme = {
            "name": "Mryaka",
            "type": "dark",
        }

    while True:

        # Updating theme colors
        if is_changed(colors) or is_changed(params):
            data_colors = read_yaml(colors)
            data_params = read_yaml(params)

            theme['colors'] = {}
            for section, values in data_params.items():

                if isinstance(values, dict):
                    for param, value in values.items():
                        # print(value)
                        theme['colors'][f"{section}.{param}"] = value_as_color(
                            value)
                else:
                    theme['colors'][f"{section}"] = value_as_color(values)

            with open("theme.json", "w") as f:
                json.dump(theme, fp=f, indent=4)

        else:
            time.sleep(1.0)


def read_yaml(file):
    with open(file, "r") as f:
        return yaml.load(f, Loader=yaml.CLoader)
    return {}


if __name__ == "__main__":
    main()
