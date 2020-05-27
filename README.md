# Car_Access

The IoT is growing by leaps and bounds, thus creating this large, smart and autonomous system requiring less and less human intervention. Smart city (SC) was always the case in point that portrays this vision where devices not only interact but depend on (even control) each other. 

## Car booking portal

The interface on which a client can book a car. It contains a catalog of available cars, a machine learning engine to extract text (mainly ID number) from ID card as well as the other building blocs responsible for the checkout.

> _HTML, CSS, JS, JQUERY, PHP, MYSQL, PYTHON_

![Car booking portal](./images/portal.JPG)

## Extract text from image

After the user scan his ID card, this API allow us to extract the ID number from it.

> _OPENCV, PYTESSERACT, FLASK_

## Data generation

- Generate _"empower"_ dataset : mapping **subjects** to **roles**

- Generate _"use"_ dataset : mapping **objects** to **views**

- Generate _"pap"_ dataset : mapping **(org,role,view,activity,context)** to **(decision, proba)**

- Two scripts : _"consider"_ and _"checkContext"_ to get the abstract entities for **actions** and **contexts** respectively 

> _NUMPY, PANDAS, DATETIME, ITERTOOLS, SKLEARN_

## Policy Information Point

## Policy Administation Point

## Policy Decision Point

## The overall architecture

As a CRA, our organization is mainly composed of selfdriving cars (decomposed into two views: luxury and normal cars); its customers are generally normal clients, VIP clients or blacklisted ones (which makes respectively three roles: NC, VIP, BC); regarding the activities it is more realistic to categorize them by rental period (a1: 1 day, a2: between 1 and 3 days, and a3: more than 3 days). Finally, the context represents the time of the year during which the request is made: is it a peak season (peak) like summer for example, or off season (off).

![The building blocks of the implementation](./images/architecture.PNG)

## Installation requirements
