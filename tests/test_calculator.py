from app.main import Calculator


def test_sum_2_numbers():
    assert Calculator().sum(2, 3) == 5
