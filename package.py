class Package(object):
    """
     Class used to represent a Package
    """

    W_GR_100 = 1.0

    def __init__(self, id_package: int = 0, weight: float = 1.0, description: str = "Description", cost: float = 1.0):
        """ Package constructor object.

        :param id_package: id of package.
        :type id_package: int
        :param weight: weight of package.
        :type weight: float
        :param description: description of package.
        :type description: str
        :param cost: cost of package.
        :type cost: float
        :returns: Package object.
        :rtype: object
        """
        self._id_package = id_package
        self._weight = weight
        self._description = description
        self._cost = cost

    @property
    def id_package(self) -> int:
        """ Returns the id of the package.
        :returns: id of package.
        :rtype: int
        """
        return self._id_package

    @id_package.setter
    def id_package(self, id_package: int):
        """ The id of the package.
        :param id_package: id of package.
        :type: int
        """
        self._id_package = id_package

    @property
    def weight(self) -> float:
        """ Returns the weight of the package.
        :returns: weight of package.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight: float):
        """ The weight of the package.
        :param weight: weight of package.
        :type: float
        """
        self._weight = weight

    @property
    def description(self) -> str:
        """ Returns the description of the package.
        :returns: description of package.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """ The description of the package.
        :param description: description of package.
        :type: str
        """
        self._description = description

    @property
    def cost(self) -> float:
        """ Returns the cost of the package.
        :returns: cost of package.
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost: float):
        """ The cost of the package.
        :param cost: cost of package.
        :type: float
        """
        self._cost = cost

    def calculate(self):
        print(f"The final cost associated with sending the package is ${self._cost * self._weight}")

    def __eq__(self, another_package):
        """ Returns bool of equality of package objects.
        :returns: bool package
        :rtype: bool
        """
        return another_package.id_package == self.id_package

    def __str__(self):
        """ Returns str of package.
        :returns: sting package
        :rtype: str
        """
        return 'Id of package: {0}, Weight: {1}, Description: {2}, Cost: {3}'.format(self._id_package, self._weight,
                                                                                     self._description, self._cost)
