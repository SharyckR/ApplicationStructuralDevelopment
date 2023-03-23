class PaymentMethod(object):
    """
     Class used to represent a Payment Method
    """

    def __init__(self, payment_method: str = "Payment Method"):
        """ Payment Method constructor object.

        :param payment_method: payment method of package.
        :type payment_method: str
        :returns: Bill object.
        :rtype: object
        """
        self._payment_method = payment_method

    @property
    def payment_method(self) -> str:
        """ Returns the payment method of the package.
        :returns: payment method.
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method: str):
        """ The payment method of the package.
        :param payment_method: payment method of package.
        :type: str
        """
        self._payment_method = payment_method

    def __eq__(self, another_payment_method):
        """ Returns bool of equality of payment method objects.
        :returns: bool payment method
        :rtype: bool
        """
        return another_payment_method.payment_method == self.payment_method

    def __str__(self):
        """ Returns str of payment method.
        :returns: sting payment method
        :rtype: str
        """
        return self._payment_method
