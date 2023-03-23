from package import Package
from person import Person
from address import Address
from payment_method import PaymentMethod


class Bill(object):
    """
     Class used to represent a Bill
    """

    def __init__(self, id_bill: int = 0, description_package: object = Package, receiver: object = Person,
                 receiver_address: object = Address, sender: object = Person, sender_address: object = Address,
                 pay_method: object = PaymentMethod):
        """ Person constructor object.

        :param description_package: description package of bill.
        :type description_package: object
        :param receiver: receiver of bill.
        :type receiver: object
        :param receiver_address: receiver address of bill.
        :type receiver_address: object
        :param sender: sender of bill.
        :type sender: object
        :param sender_address: sender address of bill.
        :type sender_address: object
        :returns: Bill object.
        :rtype: object
        """
        self._id_bill = id_bill
        self._description_package = description_package
        self._receiver = receiver
        self._receiver_address = receiver_address
        self._sender = sender
        self._sender_address = sender_address
        self._pay_method = pay_method

    @property
    def id_bill(self) -> int:
        return self._id_bill

    @id_bill.setter
    def id_bill(self, id_bill: int):
        self._id_bill = id_bill

    @property
    def description_package(self) -> object:
        return self._description_package

    @description_package.setter
    def description_package(self, description_package: object):
        self._description_package = description_package

    @property
    def receiver(self) -> object:
        return self._receiver

    @receiver.setter
    def receiver(self, receiver: object):
        self._receiver = receiver

    @property
    def receiver_address(self) -> object:
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, receiver_address: object):
        self._receiver_address = receiver_address

    @property
    def sender(self) -> object:
        return self._sender

    @sender.setter
    def sender(self, sender: object):
        self._sender = sender

    @property
    def sender_address(self) -> object:
        return self._sender_address

    @sender_address.setter
    def sender_address(self, sender_address: object):
        self._sender_address = sender_address

    @property
    def pay_method(self) -> object:
        return self._pay_method

    @pay_method.setter
    def pay_method(self, pay_method: object):
        self.pay_method = pay_method

    def __eq__(self, another_bill):
        """ Returns bool of equality of bill objects.
        :returns: bool bill
        :rtype: bool
        """
        return another_bill.id_bill == self.id_bill

    def __str__(self):
        """ Returns str of bill.
        :returns: sting bill
        :rtype: str
        """
        return ' ID of the bill: {0}\n Full description of the package-> {1}\n Information of Receiver -> {2}, {3}\n ' \
            'Information of Sender-> {4}, {5}\n Payment method: {6}\n'.format(self._id_bill, self._description_package,
            self._receiver, self._receiver_address, self._sender, self._sender_address, self._pay_method)
