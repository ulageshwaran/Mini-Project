import qrcode
import unittest


class TestQRCode(unittest.TestCase):

    def test_generate_qrcode(self):
        # Arrange
        expected_result = 'https://google.com'
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        qr.add_data(expected_result)
        qr.make(fit=True)

        # Act
        actual_result = qr.make_image()

        # Assert
        self.assertIsInstance(actual_result, qrcode.image.Image)
        self.assertEqual(expected_result, qr.text)


if __name__ == '__main__':
    unittest.main()