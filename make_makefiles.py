import re
from subprocess import call
import os

regex = re.compile("(?P<number>\d+)-.+")
extensions = ["hs", "py", "cpp", "rb"]

for folder in os.listdir("."):
    match = regex.match(folder)
    if match:
        problem = match.group("number")
        for extension in extensions:
            old_path = "{}/{}.{}".format(folder, problem, extension)
            if os.path.exists(old_path):
                new_path = "{}/main.{}".format(folder, extension)
                command = "git mv {} {}".format(old_path, new_path)
                call(command.split())
