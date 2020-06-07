#!/usr/bin/env python3
"""
    This script watches for sources and rebuild theme.json
"""

import json, yaml
import time
from random import choice as ch

import hashlib

from datetime import datetime
from os.path import splitext


class Theme:
    def __init__(self):

        self._file_palette = "src/palette.yaml"
        self._file_theme = "src/theme.yaml"
        self._file_tokens = "src/tokens.yaml"
        self._monitor = {}

        self.dest = "theme.json"

    def dpath(self, color_map, path):
        tmp = dict(color_map)

        for i in path.split("."):
            tmp = tmp.get(i, f"{path}")
            if isinstance(tmp, str):
                return tmp

        return tmp

    def pick(self, path):

        if path == '_':
            param_value = Theme.random_color()
        elif "/" in path:
            rgb, a = path.split("/")
            param_value = self.dpath(self._palette, rgb) + self.dpath(
                self._palette, a)
        elif "." in path:
            param_value = self.dpath(self._palette, path)
        elif path[0] == "#":
            param_value = path
        else:
            param_value = self.dpath(self._palette, path)

        return param_value

    def is_changed(self) -> bool:

        changed_theme = self._is_changed(self._file_theme)
        changed_tokens = self._is_changed(self._file_tokens)
        changed_palette = self._is_changed(self._file_palette)

        if changed_palette:
            self._palette = Theme.read(self._file_palette)
            print("Palette changed  : {0}".format(datetime.now().time()))

        if changed_tokens:
            self._tokens = Theme.read(self._file_tokens)
            print("Tokens changed   : {0}".format(datetime.now().time()))

        if changed_theme:
            self._theme = Theme.read(self._file_theme)
            print("Theme changed    : {0}".format(datetime.now().time()))

        return changed_palette or changed_theme or changed_tokens

    def _is_changed(self, file) -> bool:
        hasher = hashlib.md5()
        with open(file, "r") as f:
            buf = f.read()
            hasher.update(buf.encode())

        if self._monitor.get(file, None) == hasher.hexdigest():
            return False

        self._monitor[file] = hasher.hexdigest()
        return True

    def generate(self):
        t = Theme.read(self.dest)
        if not len(t):
            t = {
                "name": "Mryaka",
                "type": "dark",
            }

        # Updating colors
        t['colors'] = {}

        if self._theme:
            for section, values in self._theme.items():

                if isinstance(values, dict):
                    for param, value in values.items():
                        # print(value)
                        name = f"{section}.{param}"
                        t['colors'][name] = self.pick(value)
                else:
                    t['colors'][f"{section}"] = self.pick(values)

        # updating tokens
        t['tokenColors'] = []
        if self._tokens:
            for item in self._tokens.get('scopes', []):
                if "settings" not in item:
                    continue

                for k, v in item['settings'].items():
                    item['settings'][k] = self.pick(v)

                t['tokenColors'].append(item)

        with open(self.dest, "w") as f:
            print("Same theme       : {0}".format(datetime.now().time()))
            json.dump(t, fp=f, indent=4)

    @staticmethod
    def random_color() -> str:
        return "#" + ''.join([ch('0123456789ABCDEF') for j in range(6)])

    @staticmethod
    def read(file):
        _, ext = splitext(file)

        executors = {
            '.yaml': lambda file: yaml.load(file, Loader=yaml.CLoader),
            '.yml': lambda file: yaml.load(file, Loader=yaml.CLoader),
            '.json': lambda file: json.load(file),
        }
        try:
            with open(file, "r") as f:
                return executors.get(ext)(f)
        except BaseException as e:
            print(f"Error reading {file} with {e}")

        return {}


def main():
    theme = Theme()
    while True:
        if theme.is_changed():
            theme.generate()
        time.sleep(1)


#     colors = "src/colors.yaml"
#     params = "src/settings.yaml"

#     syntax = "src/darkly.yaml"
#     colors = "src/palette.yaml"

#     def value_as_color(colors, value):
#         if value == '_':
#             param_value = color()
#         elif "/" in value:
#             rgb, a = value.split("/")
#             param_value = dpath(colors, rgb) + dpath(colors, a)
#         elif "." in value:
#             param_value = dpath(colors, value)
#         elif value[0] == "#":
#             param_value = value
#         else:
#             param_value = value

#         return param_value

#     # Base theme file we changing.
#     theme = {}
#     try:
#         with open("theme.json", "r") as f:
#             theme = json.load(f)
#     except FileNotFoundError:
#         theme = {
#             "name": "Mryaka",
#             "type": "dark",
#         }

#     while True:

#         # Updating theme colors
#         if is_changed(colors) or is_changed(params):
#             data_colors = read_yaml(colors)
#             data_params = read_yaml(params)

#             theme['colors'] = {}
#             for section, values in data_params.items():

#                 if isinstance(values, dict):
#                     for param, value in values.items():
#                         # print(value)
#                         theme['colors'][f"{section}.{param}"] = value_as_color(
#                             data_colors, value)
#                 else:
#                     theme['colors'][f"{section}"] = value_as_color(
#                         data_colors, values)

#             with open("theme.json", "w") as f:
#                 print("Updating Theme  : {0}".format(datetime.now().time()))
#                 json.dump(theme, fp=f, indent=4)

#         if is_changed(syntax):
#             data_colors = read_yaml(syntax)
#             theme['tokenColors'] = []

#             for item in data_colors.get('scopes', []):
#                 if "settings" not in item:
#                     continue

#                 for k, v in item['settings'].items():
#                     item['settings'][k] = value_as_color(data_colors, v)

#                 theme['tokenColors'].append(item)

#             with open("theme.json", "w") as f:
#                 print("Updating Tokens : {0}".format(datetime.now().time()))
#                 json.dump(theme, fp=f, indent=4)

#         else:
#             time.sleep(1.0)

# def read_yaml(file):
#     with open(file, "r") as f:
#         return yaml.load(f, Loader=yaml.CLoader)
#     return {}

if __name__ == "__main__":
    main()
