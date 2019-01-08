import unittest

import point


class TestPoint(unittest.TestCase):
    def test_attributes(self):
        pt = point.Point()

        self.assertEqual(0, pt.x)

    def test_distance_to_same(self):
        pt = point.Point()

        distance = pt.distance_to(pt)

        self.assertEqual(
            0, distance,
            "Should return when both points are the same"
        )

    def test_distance_to_one_axis(self):
        pt0 = point.Point(x=3)
        pt1 = point.Point()

        distance = pt0.distance_to(pt1)

        self.assertEqual(
            3, distance,
            "Should return distance between point 1 and 2 when on the same axis"
        )

    def test_dimension(self):
        pt = point.Point(x=3)

        self.assertEqual(
            3, pt.dimension,
            "Should return the proper dimension of the point (minimum: 3"
        )

    def test_distance_to_across_axis(self):
        pt0 = point.Point(x=3)
        pt1 = point.Point(x=-3)

        distance = pt0.distance_to(pt1)

        self.assertEqual(
            6, distance,
            "Should return distance between point 1 and 2 when on across the origin"
        )

    def test_distance_to_two_axes(self):
        pt0 = point.Point(x=10, y=10)
        pt1 = point.Point()

        distance = pt0.distance_to(pt1)

        self.assertAlmostEqual(
            14.1421, distance, 4,
            "Should return distance between point 1 and 2 are on different axes"
        )

    def test_distance_to_three_axes(self):
        pt0 = point.Point(x=10, y=10, z=10)
        pt1 = point.Point()

        distance = pt0.distance_to(pt1)

        self.assertAlmostEqual(
            17.32050, distance, 4,
            "Should return distance between point 1 and 2 are on different axes"
        )

    def test_distance_to_three_axes_2(self):
        pt0 = point.Point(coords=[10, 10, 10])
        pt1 = point.Point()

        distance = pt0.distance_to(pt1)

        self.assertAlmostEqual(
            17.32050, distance, 4,
            "Should return distance between point 1 and 2 are on different axes"
        )

    def test_distance_to_mismatched_dimensions(self):
        pt0 = point.Point(coords=[10, 10, 10])
        pt1 = point.Point(coords=[10, 10])

        with self.assertRaises(point.DimensionMismatch):
                pt0.distance_to(pt1)

    def test_distance_to_non_numeric(self):
        pt0 = point.Point(coords=['A', 10, 10])
        pt1 = point.Point(coords=[10, 10, 10])

        with self.assertRaises(TypeError):
                pt0.distance_to(pt1)
