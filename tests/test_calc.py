import pytest
import os
import glob
import requests
from subprocess import check_output

script_path = "tests/test.sh"

# def run_shell_test(script, function_name, arg1, arg2):
#     process = Popen([script, function_name, str(arg1), str(arg2)], stdout=PIPE)
#     stdout = process.communicate()[0]
#     return stdout

def run_shell_test(script, function_name, arg1, arg2):
    out = check_output([script, function_name, str(arg1), str(arg2)], universal_newlines=True)
    return int(out.split("\n")[0])

def test_add():
    result = run_shell_test(script_path, 'add', 1, 2)
    assert result == 3

def test_mul():
    result = run_shell_test(script_path, 'mul', 1, 2)
    assert result == 2

def test_sub():
    result = run_shell_test(script_path, 'sub', 1, 2)
    assert result == -1

def test_div():
    result = run_shell_test(script_path, 'sub', 2, 2)
    assert result == 1
    
def test_connect():
    url = 'https://filesamples.com/samples/document/txt/sample3.txt'
    r = requests.get(url, allow_redirects=True)
    open('checkup-linux', 'wb').write(r.content)
    
    assert r.content == 1
    

