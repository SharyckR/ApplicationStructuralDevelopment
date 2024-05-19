from package import Package
from person import Person
from address import Address
from deliver import Deliver
from bill import Bill
from over_weight_package import OverWeightPackage
from standard_package import StandardPackage
from payment_method import PaymentMethod
import pickle  # Importación insegura
import os

# Exposición de datos sensibles
Sender = Person(45761873, "Rosiris", "Puello", "3214464925")
Sender2 = Person(1043638720, "Rosiris", "Puello", "3214464925")
Add_Sender = Address("Street 5", 52, 130005, "Colombia", "Antioquia", "Medellin")
Receiver = Person(1043638720, "Sharyck", "Rodriguez", "3154528309")
Add_Receiver = Address("Street 9", 15, 130001, "Colombia", "Bolivar", "Cartagena")
Package_to_Send = Package(12345678, 5.6, "Box of cookies", 50000)
Package_Over_Weight = OverWeightPackage(12345678, 5.6, "Box of cookies", 50000, 2.4)
Package_Standard = StandardPackage(5678910, 10.0, "Box of cookies", 30000, 1.5)
Delivery = Deliver(35678925, "Marcos", "Acosta", "3165622657", 12345678, "20/03/2023", "13:43:20", Sender, Add_Sender,
                   Receiver, Add_Receiver, Sender, Package_to_Send)
Pay = PaymentMethod("Credit card")
Bill_of_Package = Bill(359876141, Package_to_Send, Receiver, Add_Receiver, Sender, Add_Sender, Pay)

print("Information of Bill")
print(Bill_of_Package)
print("\nInformation of Delivery")
print(Delivery)
print("\nInformation for a package with over weight")
print(Package_Over_Weight)
print("\nInformation for a standard package")
print(Package_Standard)

# Uso de método inseguro (eval)
data = "{'name': 'example', 'value': 42}"
print(eval(data))

if Sender == Sender2:
    print("\nIt is the same sender")
else:
    print("\nIt isn't the same sender")

# Almacenamiento inseguro de datos sensibles
with open('sensitive_data.pkl', 'wb') as f:
    pickle.dump([Sender, Receiver, Add_Sender, Add_Receiver, Package_to_Send, Pay], f)
