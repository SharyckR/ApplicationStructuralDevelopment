class Address(object):
    """
     Class used to represent an Address
    """

    def __init__(self, street: str = "Street", number: int = 0, postal_code: int = 0, country: str = "Country",
                 department: str = "Department", city: str = "City"):
        """ Address constructor object.

        :param street: street of address.
        :type street: str
        :param number: number of address.
        :type number: int
        :param postal_code: postal code of address.
        :type postal_code: int
        :param country: country of address.
        :type country: str
        :param department: department of address.
        :type department: str
        :param city: city of address.
        :type city: str
        :returns: Address object.
        :rtype: object
        """
        self._street = street
        self._number = number
        self._postal_code = postal_code
        self._country = country
        self._department = department
        self._city = city

    @property
    def street(self) -> str:
        """ Returns the street of the address.
        :returns: street of address.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street: str):
        """ The street of the address.
        :param street: street of address.
        :type: str
        """
        self._street = street

    @property
    def number(self) -> int:
        """ Returns the number of the address.
        :returns: number of address.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number: int):
        """ The number of the address.
        :param number: number of address.
        :type: int
        """
        self._number = number

    @property
    def postal_code(self) -> int:
        """ Returns the postal code of the address.
        :returns: postal code of address.
        :rtype: int
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code: int):
        """ The postal code of the address.
        :param postal_code: postal code of address.
        :type: int
        """
        self._postal_code = postal_code

    @property
    def country(self) -> str:
        """ Returns the country of the address.
        :returns: country of address.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country: str):
        """ The country of the address.
        :param country: country of address.
        :type: str
        """
        self._country = country

    @property
    def department(self) -> str:
        """ Returns the department of the address.
        :returns: department of address.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department: str):
        """ The department of the address.
        :param department: department of address.
        :type: str
        """
        self._department = department

    @property
    def city(self) -> str:
        """ Returns the city of the address.
        :returns: city of address.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """ The city of the address.
        :param city: city of address.
        :type: str
        """
        self._city = city

    def __eq__(self, another_address):
        """ Returns bool of equality of bill objects.
        :returns: bool bill
        :rtype: bool
        """
        return another_address.street == self.street and another_address.number == self.number \
            and another_address.postal_code == self.postal_code and another_address.country == self.country \
            and another_address.department == self.department and another_address.city == self.city

    def __str__(self):
        """ Returns str of address.
        :returns: sting address
        :rtype: str
        """
        return 'Street: {0}, Number of street: {1}, Postal code: {2}, Country: {3}, Department: {4}, City: {5},'.\
            format(self._street, self._number, self._postal_code, self._country, self._department, self._city)
