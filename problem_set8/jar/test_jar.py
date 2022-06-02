from jar import Jar
import pytest

def test_init():
    jar = Jar()
    jar._capacity == 12
    jar = Jar(0)
    jar._capacity == 0

    with pytest.raises(ValueError):
        Jar(-1)
        Jar('cookie')
        Jar('')

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar._size == 5
    with pytest.raises(ValueError):
        jar.deposit(14)
        jar.deposit(343)

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar._size == 3
    with pytest.raises(ValueError):
        jar.withdraw(45)
        jar.withdraw(234)
