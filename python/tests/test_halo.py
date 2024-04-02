from rypm import lib
import pytest


def test_halo():
    assert lib.halo() == "Hello rypm from rust!"


def test_add():
    assert lib.add(1, 2) == 3
    assert lib.add(1, 1) != 3


if __name__ == "__main__":
    pytest.main()
