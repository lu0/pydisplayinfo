import pytest

from pydisplayinfo.dummy import dummy_sum


class TestDummy:
    @pytest.mark.parametrize(
        "a, b",
        [
            (-1, -3),
            (-6, -7),
            (-100, -1000),
        ],
    )
    def test_sum_negatives_remain_negatives(self, a, b):
        """Dummy test"""
        assert dummy_sum(a, b) < 0

    @pytest.mark.parametrize(
        "a, b",
        [
            (1, 3),
            (6, 7),
            (100, 1000),
        ],
    )
    def test_sum_positives_remain_positives(self, a, b):
        """Dummy test"""
        assert dummy_sum(a, b) > 0

    def test_sum_zeros(self):
        """Another dummy test"""
        assert dummy_sum(0, 0) == 0
