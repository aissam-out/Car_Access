# The Booking Portal

The interface on which a client can book a car. It contains a catalog of available cars, a machine learning engine to extract text (mainly ID number) from ID card as well as the other building blocs responsible for the checkout.

> _HTML, CSS, JS, JQUERY, PHP, APACHE, MYSQL, PYTHON_

![Car booking portal](../images/portal.JPG)

Hereafter the relationships between all the webpages and scripts composing this portal :

![pages flow](../images/booking_flow.png)

### Extract text from image

After the user scan his ID card _(upload.html)_, an API _(image extractor)_ allows us to extract the ID number from it.

> _OPENCV, PYTESSERACT, FLASK_
