from package import Package


class OverWeightPackage(Package):
    """
     Class used to represent an Over Weight Package
    """

    def __init__(self, id_package: int = 0, weight: float = 1.0, description: str = "Description", cost: float = 1.0,
                 over_weight: float = 1.0):
        """ Over weight package constructor object.

        :param over_weight: over weight of package.
        :type over_weight: float
        :returns: Over weight package object.
        :rtype: object
        """
        super().__init__(id_package, weight, description, cost)
        self._over_weight = over_weight

    @property
    def over_weight(self) -> float:
        """ Returns the over weight of the package.
        :returns: over weight of package.
        :rtype: float
        """
        return self._over_weight

    @over_weight.setter
    def over_weight(self, over_weight: float):
        """ The over weight of the package.
        :param over_weight: over weight of package.
        :type: float
        """
        self._over_weight = over_weight

    def calculate(self):
        print(f"The additional charge for grams in the shipment of the package "
              f"is ${(self._over_weight + self._weight) * self._cost}")

    def __eq__(self, another_over_weight_package):
        """ Returns bool of equality of over weight package objects.
        :returns: bool over weight
        :rtype: bool
        """
        return another_over_weight_package.over_weight == self.over_weight

    def __str__(self):
        """ Returns str of over weight package.
        :returns: sting over weight package
        :rtype: str
        """
        return 'Id package: {0}, Weight: {1}, Description: {2}, Cost without over weight: {3}'.format(
            self._id_package, self._weight, self._description, self._cost, self.calculate())
