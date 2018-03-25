import pytest

from pypack.spark import get_spark
from pypack.mission import with_life_goal

class TestMission(object):

    def test_with_life_goal(self):
        source_data = [
            ("jose", 1),
            ("pedro", 2)
        ]
        source_df = get_spark().createDataFrame(
            source_data,
            ["name", "age"]
        )

        actual_df = with_life_goal(source_df)

        expected_data = [
            ("jose", 1, "escape 2!"),
            ("pedro", 2, "escape 1!")
        ]
        expected_df = get_spark().createDataFrame(
            expected_data,
            ["name", "age", "life_goal"]
        )

        assert(expected_df.collect() == actual_df.collect())

