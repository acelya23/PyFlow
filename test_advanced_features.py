import pytest

# Fixture tanımlama
@pytest.fixture
def example_data():
    return [1, 2, 3, 4, 5]

# Basit bir test örneği (fixtures kullanarak)
def test_sum(example_data):
    assert sum(example_data) == 15

# Parametrized test örneği
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),      # 1 + 2 = 3
    (-1, 1, 0),     # -1 + 1 = 0
    (0, 0, 0),      # 0 + 0 = 0
    (5, 5, 10)      # 5 + 5 = 10
])
def test_add(a, b, expected):
    assert a + b == expected

