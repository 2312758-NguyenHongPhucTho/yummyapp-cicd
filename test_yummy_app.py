import unittest
from unittest.mock import patch

import gps_service
from yummy_app import YummyApp


class TestEasyLevel(unittest.TestCase):
    """Kiem thu chuc nang co ban tinh tien don hang."""

    def setUp(self):
        self.app = YummyApp()

    def test_calculate_total_for_single_item(self):
        cart = {"pho": 2}
        self.assertEqual(self.app.calculate_order_total(cart), 100000)

    def test_calculate_total_for_multiple_items(self):
        cart = {"pho": 1, "bun": 1}
        self.assertEqual(self.app.calculate_order_total(cart), 95000)

    def test_calculate_total_for_empty_cart(self):
        self.assertEqual(self.app.calculate_order_total({}), 0.0)

    def test_calculate_total_with_zero_quantity(self):
        cart = {"pho": 0}
        self.assertEqual(self.app.calculate_order_total(cart), 0.0)


class TestMediumLevel(unittest.TestCase):
    def test_online_with_valid_giam10_code(self):
        app = YummyApp(network_status="online", os_version=15)
        self.assertEqual(app.apply_promo_code(100000, "GIAM10"), 90000)

    def test_offline_raises_connection_error(self):
        app = YummyApp(network_status="offline", os_version=15)
        with self.assertRaises(ConnectionError):
            app.apply_promo_code(100000, "GIAM10")

    def test_new_os_only_on_os_15(self):
        app = YummyApp(network_status="online", os_version=15)
        self.assertEqual(app.apply_promo_code(100000, "NEW_OS_ONLY"), 80000)

    def test_new_os_only_on_os_14_raises_value_error(self):
        app = YummyApp(network_status="online", os_version=14)
        with self.assertRaises(ValueError):
            app.apply_promo_code(100000, "NEW_OS_ONLY")


class TestHardLevel(unittest.TestCase):
    @patch("yummy_app.gps_service.get_current_location")
    def test_gps_in_supported_area_returns_restaurants(self, mock_location):
        mock_location.return_value = (10.0, 105.0)
        expected = ["Nha hang Pho Ly Quoc Su", "Bun cha Huong Lien"]
        self.assertEqual(YummyApp().get_nearby_restaurants(), expected)

    @patch("yummy_app.gps_service.get_current_location")
    def test_gps_outside_supported_area_returns_empty_list(self, mock_location):
        mock_location.return_value = (20.0, 110.0)
        self.assertEqual(YummyApp().get_nearby_restaurants(), [])

    @patch("yummy_app.gps_service.get_current_location")
    def test_gps_signal_lost_returns_message(self, mock_location):
        mock_location.side_effect = gps_service.GPSSignalLostError
        self.assertEqual(
            YummyApp().get_nearby_restaurants(),
            "Khong the xac dinh vi tri.",
        )


if __name__ == "__main__":
    unittest.main()
