import pytest


class TestDummy:
    @pytest.mark.parametrize(
        "a, b, c",
        [
            ("one", "two", "three"),
            ("1989", "13", "december"),
        ],
    )
    def test_dummy(self, a, b, c):
        """Dummy test"""
        result = a + b + c
        print(result)
        assert type(a + b + c) == str

    def test_boolean(self):
        """Most dummy test"""
        assert True is True
