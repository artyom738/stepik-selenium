import pytest
from selenium import webdriver
from os import system

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False

def main():
    system(f'pytest -v "{__file__}"')
if __name__ == "__main__":
    main()
