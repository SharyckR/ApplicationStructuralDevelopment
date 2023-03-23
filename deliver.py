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
        """ Returns the id of the deliver.
        :returns: id of deliver.
        :rtype: int
        """
        return self._id_deliver

    @id_deliver.setter
    def id_deliver(self, id_deliver: int):
        """ The id of the deliver.
        :param id_deliver: id of deliver.
        :type: int
        """
        self._id_deliver = id_deliver

    @property
    def date(self) -> str:
        """ Returns the date of the deliver.
        :returns: date of deliver.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date: str):
        """ The date of the deliver.
        :param date: date of deliver.
        :type: str
        """
        self._date = date

    @property
    def time(self) -> str:
        """ Returns the time of the deliver.
        :returns: time of deliver.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time: str):
        """ The time of the deliver.
        :param time: time of deliver.
        :type: str
        """
        self._time = time

    @property
    def sender(self) -> object:
        """ Returns the sender of the deliver.
        :returns: sender of deliver.
        :rtype: object
        """
        return self._sender

    @sender.setter
    def sender(self, sender: object):
        """ The sender of the deliver.
        :param sender: sender of deliver.
        :type: object
        """
        self._sender = sender

    @property
    def sender_add(self) -> object:
        """ Returns the sender address of the deliver.
        :returns: sender address of deliver.
        :rtype: object
        """
        return self._sender_add

    @sender_add.setter
    def sender_add(self, sender_add: object):
        """ The sender address of the deliver.
        :param sender_add: sender address of deliver.
        :type: object
        """
        self._sender_add = sender_add

    @property
    def receiver(self) -> object:
        """ Returns the receiver of the deliver.
        :returns: receiver of deliver.
        :rtype: object
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver: object):
        """ The receive of the deliver.
        :param receive: receive of deliver.
        :type: object
        """
        self._receiver = receiver

    @property
    def receiver_add(self) -> object:
        """ Returns the receiver address of the deliver.
        :returns: receiver address of deliver.
        :rtype: object
        """
        return self._receiver_add

    @receiver_add.setter
    def receiver_add(self, receiver_add: object):
        """ The receiver address of the deliver.
        :param receiver_add: receiver address of deliver.
        :type: object
        """
        self._receiver_add = receiver_add

    @property
    def contact(self) -> object:
        """ Returns the contact of the deliver.
        :returns: contact of deliver.
        :rtype: object
        """
        return self._contact

    @contact.setter
    def contact(self, contact: object):
        """ The contact of the deliver.
        :param contact: contact of deliver.
        :type: object
        """
        self._contact = contact

    @property
    def items(self) -> object:
        """ Returns the items of the deliver.
        :returns: items of deliver.
        :rtype: object
        """
        return self._items

    @items.setter
    def items(self, items: object):
        """ The items of the deliver.
        :param items: items of deliver.
        :type: object
        """
        self._items = items

    def __eq__(self, another_deliver):
        """ Returns bool of equality of deliver objects.
        :returns: bool deliver
        :rtype: bool
        """
        return another_deliver.id_deliver == self.id_deliver

    def __str__(self):
        """ Returns str of deliver.
        :returns: sting deliver
        :rtype: str
        """
        return ' Id delivery: {0}\n Date: {1}, Time: {2}\n Information of sender -> {3}, {4}\n Information of ' \
               'receiver-> {5}, {6}\n Contact-> {7}\n Items-> {8}\n'.format(self._id_deliver, self._date, self._time,
                                                                      self._sender, self._sender_add, self._receiver,
                                                                      self._receiver_add, self._contact, self._items)
