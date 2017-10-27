from unittest import TestCase

import numpy as np

from hrv.filters import moving_average


class Filter(TestCase):
    def test_moving_average_order_3(self):
        fake_rri = np.array([810, 830, 860, 790, 804])

        rri_filt = moving_average(fake_rri, order=3)

        expected = [810, 833.33, 826.66, 818, 804]
        np.testing.assert_almost_equal(rri_filt, expected, decimal=2)
