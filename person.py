class Person(object):
  """
   Class used to represent a Person
  """

  def __init__(self, id_person: int = 0, name: str = 'Name', last_name: str = "LastName", phone: int = 0):
    """ Person constructor object.

    :param id_person: id of person.
    :type id_person: int
    :param name: name of person.
    :type name: str
    :param last_name: last name of person.
    :type last_name: str
    :param phone: phone of person.
    :type phone: int
    :returns: Person object.
    :rtype: object
    """
    self._id_person = id_person
    self._name = name
    self._last_name = last_name
    self._phone = phone

  @property
  def id_person(self) -> int:
    """ Returns the id of the person.
    :returns: id of person.
    :rtype: int
    """
    return self._id_person

  @id_person.setter
  def id_person(self, id_person: int):
    """ The id of the person.
    :param id_person: id of person.
    :type: int
    """
    self._id_person = id_person

  @property
  def name(self) -> str:
    """ Returns the name of the person.
    :returns: name of person.
    :rtype: str
    """
    return self._name

  @name.setter
  def name(self, name: str):
    """ The name of the person.
    :param name: id of person.
    :type: str
    """
    self._name = name

  @property
  def last_name(self) -> str:
    """ Returns the last name of the person.
    :returns: last name of person.
    :rtype: str
    """
    return self._last_name

  @last_name.setter
  def last_name(self, last_name: str):
    """ The last name of the person.
    :param last_name: last name of person.
    :type: str
    """
    self._last_name = last_name

  @property
  def phone(self) -> int:
    """ Returns the phone of the person.
    :returns: phone of person.
    :rtype: int
    """
    return self._phone

  @phone.setter
  def phone(self, phone: int):
    """ The phone of the person.
    :param phone: phone of person.
    :type: int
    """
    self._phone = phone

  def __eq__(self, another_person):
    """ Returns bool of equality of person objects.
    :returns: bool person
    :rtype: bool
    """
    return another_person.id_person == self.id_person

  def __str__(self):
    """ Returns str of person.
    :returns: sting person
    :rtype: str
    """
    return 'Id of person: {0}, Full name: {1} {2}, Phone: {3}'.format(self._id_person, self._name, self._last_name,
                                     self._phone)
      
