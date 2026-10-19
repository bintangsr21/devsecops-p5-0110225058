import subprocess


def run_command(user_input):
    return subprocess.call(user_input, shell=True)


def calculate(expression):
    return eval(expression)