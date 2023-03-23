from package import Package
from person import Person
from address import Address


class Deliver(Person):
    """
     Class used to represent a Delivery
    """

    def __init__(self, id_person: int = 0, name: str = 'Name', last_name: str = "LastName", phone: int = 0,
                 id_deliver: int = 0, date: str = "01/99/9999", time: str = "00:00:00", sender: object = Person,
                 sender_add: object = Address, receiver: object = Person, receiver_add: object = Address,
                 contact: object = Person, items: object = Package):
        """ Delivery constructor object.

        :param id_deliver: id of deliver.
        :type id_deliver: int
        :param date: date of deliver.
        :type date: str
        :param time: time of deliver.
        :type time: str
        :param sender: sender of deliver.
        :type sender: object
        :param sender_add: sender address of deliver.
        :type sender_add: object
        :param receiver: receiver of deliver.
        :type receiver: object
        :param receiver_add: receiver address of deliver.
        :type receiver_add: object
        :param contact: contact of deliver.
        :type contact: object
        :param items: items of deliver.
        :type items: object
        :returns: Deliver object.
        :rtype: object
        """
        super().__init__(id_person, name, last_name, phone)
        self._id_deliver = id_deliver
        self._date = date
        self._time = time
        self._sender = sender
        self._sender_add = sender_add
        self._receiver = receiver
        self._receiver_add = receiver_add
        self._contact = contact
        self._items = items

    @property
    def id_deliver(self) -> int:
        return self._id_deliver

    @id_deliver.setter
    def id_deliver(self, id_deliver: int):
        self._id_deliver = id_deliver

    @property
    def date(self) -> str:
        return self._date

    @date.setter
    def date(self, date: str):
        self._date = date

    @property
    def time(self) -> str:
        return self._time

    @time.setter
    def time(self, time: str):
        self._time = time

    @property
    def sender(self) -> object:
        return self._sender

    @sender.setter
    def sender(self, sender: object):
        self._sender = sender

    @property
    def sender_add(self) -> object:
        return self._sender_add

    @sender_add.setter
    def sender_add(self, sender_add: object):
        self._sender_add = sender_add

    @property
    def receiver(self) -> object:
        return self._receiver

    @receiver.setter
    def receiver(self, receiver: object):
        self._receiver = receiver

    @property
    def receiver_add(self) -> object:
        return self._receiver_add

    @receiver_add.setter
    def receiver_add(self, receiver_add: object):
        self._receiver_add = receiver_add

    @property
    def contact(self) -> object:
        return self._contact

    @contact.setter
    def contact(self, contact: object):
        self._contact = contact

    @property
    def items(self) -> object:
        return self._items

    @items.setter
    def items(self, items: object):
        self._items = items

    def __eq__(self, another_deliver):
        """ Returns bool of equality of deliver objects.
        :returns: bool deliver
        :rtype: bool
        """
        return another_deliver.id_deliver == self.id_deliver

    def __str__(self):
        return ' Id delivery: {0}\n Date: {1}, Time: {2}\n Information of sender -> {3}, {4}\n Information of ' \
               'receiver-> {5}, {6}\n Contact-> {7}\n Items-> {8}\n'.format(self._id_deliver, self._date, self._time,
                                                                      self._sender, self._sender_add, self._receiver,
                                                                      self._receiver_add, self._contact, self._items)
