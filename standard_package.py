from package import Package


class StandardPackage(Package):
    """
     Class used to represent a Standard Package
    """

    def __init__(self, id_package: int = 0, weight: float = 1.0, description: str = "Description", cost: float = 1.0,
                 fixed_fee: float = 1.0):
        """ Standard package constructor object.

        :param fixed_fee: fixed fee of package.
        :type fixed_fee: float
        :returns: Standard package object.
        :rtype: object
        """
        super().__init__(id_package, weight, description, cost)
        self._fixed_fee = fixed_fee

    @property
    def fixed_fee(self) -> float:
        """ Returns the fixed fee of the package.
        :returns: fixed fee of package.
        :rtype: float
        """
        return self._fixed_fee

    @fixed_fee.setter
    def fixed_fee(self, fixed_fee: float):
        """ The fixed free of the package.
        :param fixed_fee: fixed free of package.
        :type: float
        """
        self._fixed_fee = fixed_fee

    def calculate(self):
        print(f"The shipping cost by adding the fixed fee at the cost based on the weight of the package "
              f"is ${(self._fixed_fee + self._weight) * self._cost}")

    def __eq__(self, another_standard_package):
        """ Returns bool of equality of standard package objects.
        :returns: bool fixed fee
        :rtype: bool
        """
        return another_standard_package.fixed_fee == self.fixed_fee

    def __str__(self):
        """ Returns str of standard package.
        :returns: sting standard package
        :rtype: str
        """
        return 'Id package: {0}, Weight: {1}, Description: {2}, Cost without fixed free: {3}'.format(
            self._id_package, self._weight, self._description, self._cost, self.calculate())
