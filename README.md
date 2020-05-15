# Disaster Site Resources Locator - Project

## CIIC 4060 / ICOM 5016 - Database Systems

Backend System for Disaster Site Resources Locator

### Usage:

A user (```users```) can be registered without specifying a role (without a role, the user only exists as a person with first name and last name). No interaction is available for a user without a role.

It is recommended to add new ```users``` from the role they will belong to, thus granting the user the specific permissions.

  * A ```consumer``` can be added by specifying: consumer username, user first name, user last name
  * A ```supplier``` can be added by specifying: supplier username, supplier company, user first name, user last name
    * If the company for which the ```supplier``` works exists, you can also link it providing the ```company``` ID.
  * A system administrator (```sys_adm```) can be added by specifying: system administrator username, user first name, user last name
  
A ```company``` can be added by specifying the company's name. A ```company``` can exist without a ```supplier```, but it will not be able to provide ```resources```.

* To link a ```company``` to an existing ```supplier```, from ```supplier```, update ```supplier``` while providing the ```company``` ID.

A ```resource``` can be added by specifying the resource's name, type, price, location, and stock. A valid ```supplier``` needs to be specified for the ```resource``` to be available.

  * For 'location' to generate a Google Maps link, it will require the following format: latitude,longitude . (Example: " 18.46542,-66.1172515 ") This will allow creating a link with the exact location of the resource. It is also possible to specify the town (Example: " San Juan "), our internal system will provide the corresponding coordinates for you (this library will be updated in the future, so far it only works with busiest cities). Lastly, any other string may be used in location, but it WILL NOT provide a Google Maps link.
    
A ```reservation``` can be added by specifying the needed resource name, type, price, location, stock, and reservation time. A valid ```consumer``` needs to be specified for a reservation to be valid.
 
  * Name, type, and price needs to match resource parameters
  * If the price is 0.00, it means that it was not purchased, it was reserved.
    * The preferred format for reservation time is: '```YYYY-MM-DD hh:mm:ss```' ; typing '```default```' will return current time at that moment.
    * For a purchased item, reservation time refers to 'when the reservation is needed'
    * For a reserved item, reservation time refers to 'until when an item is going to be reserved'
  * All successful reservations receive as receipt an Order; if a reservation does not receive an order, that means that the reservation was unsuccessful, indicating that the resource was not available.
  
An ```order``` is only added once a reservation is successfully completed. See ```reservation```
  * If for some reason an order is being added manually:
    * The preferred format for order time is: '```YYYY-MM-DD hh:mm:ss```' ; typing '```default```' will return current time at that moment.
    * Receives order number and time, and reference to an existing valid reservation.

A paying method (```pay_method```) can be added by specifying a payment method name. A valid ```consumer``` needs to be specified to have a valid payment method.



### You need the following software installed to run this application:

1. PostgreSQL - database engine

2. Pyscopg2 - library to connect to PostgreSQL form Python

3. PgAdmin3 - app to manage the databases

4. Flask - web bases framework to implement the REST API.
