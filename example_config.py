"""Base config example file.
A config variable should be CAPITALIZE (constant) and use only letters or underscores (to keep the compatibility with the environement) and should be strings.
The advantage of using a python file for the config is that you can use python to build your configuration.
"""


# A simple value.
SIMPLE_VALUE: str = 'a simple value'

# Multiple value (like the env path).
PATH_VALUE: list[str] = ['C:/',
                         'E:/Programs',
                         'S:/Test']
