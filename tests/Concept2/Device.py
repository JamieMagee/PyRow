"""
tests.PyRow.Concept2.Device
"""
import mock


class PM3(mock.NonCallableMock):
    """
    PM3 Device Mock
    """

    def __init__(self):
        """
        :return:
        """
        super(PM3, self).__init__()

        self.__commands = []

        self.serial_number = "400124190"

        self.iManufacturer = 0x1
        self.iProduct = 0x2
        self.iSerialNumber = 0x3

        self.idProduct = 0x0001

        in_endpoint = mock.Mock()
        out_endpoint = mock.Mock()
        in_endpoint.bEndPointAddress = 'IN_ENDPOINT'
        out_endpoint.bEndPointAddress = 'OUT_ENDPOINT'

        self.info = [
            {
                (0, 0): [
                    in_endpoint,
                    out_endpoint
                ]
            }
        ]

    def get_usb_util_string(self, key):
        """
        :param int key:
        :return:
        """
        if self.iManufacturer == key:
            return "Concept2"
        elif self.iProduct == key:
            return "Concept2 Performance Monitor 3 (PM3)"
        elif self.iSerialNumber == key:
            return "400124190"

        raise Exception("Unknown descriptor: {0}".format(key))

    def __getitem__(self, item):
        """
        :param item:
        :return mixed:
        """
        return self.info[item]

    def is_kernel_driver_active(self, value):
        """
        :param value:
        :return boolean:
        """
        return False

    def set_configuration(self):
        """
        :return:
        """
        pass

    def write(self, address, commands, timeout=2000):
        """
        TODO: Mock return based on commands
        :param address:
        :param commands:
        :param timeout:
        :return:
        """

        self.__commands = commands

        return 80

    def read(self, address, length, timeout=2000):
        """
        TODO: Mock return based on last command
        :param address:
        :param length:
        :param timeout:
        :return:
        """

        return []
