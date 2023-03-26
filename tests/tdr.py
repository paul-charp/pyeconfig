import pyeconfig
import os

config_file: str = './example_config.py'
keys: list[str] = ['SIMPLE_VALUE',
                   'PATH_VALUE']

config: dict[str] = pyeconfig.pyeconfig.get_config(config_file)

print(config)
