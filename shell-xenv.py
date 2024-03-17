#!/usr/bin/python3

import os
import sys

preserverd_envs = [
    "DISPLAY",
    "XAUTHORITY",
]
envs = {var: os.environ[var] for var in preserverd_envs if var in os.environ.keys()}

args = ["nix-shell", "--pure",
    "--command",
    "".join([f"export {key}={val};" for key, val in envs.items()])+"bash;"]
print(args)
os.execvp(
    "nix-shell",
    args + sys.argv[1:],
)
