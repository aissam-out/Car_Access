# Policy Information Point

Policy information point (a.k.a. PIP) is the system entity that acts as a source of attribute values. It contains the dataset/rules matching each concreate entity -subject, object, action, context- with its abstract category -role, view, activity, Context (respectively)-

On top of these datasets/rules, our PIP provides a [Flask](https://flask.palletsprojects.com) based web framework able to receive _matching_ requests from the PDP using JSON format.


- The _"empower"_ dataset : mapping **subjects** to **roles**

| Organization | Card ID | VIP badge | Role |
|:-------:|:---:|:---:|:---:|

- The _"use"_ dataset : mapping **objects** to **views**

| Organization | Plate ID | Company | Model | View |
|:-------:|:---:|:---:|:---:|:---:|

- Two scripts : _"consider"_ and _"checkContext"_ to get the abstract entities for **actions** and **contexts** respectively are directlty stored in the PIP

- The file _request.csv_ is optional : it serves to store the abstract entities after answering a given request 

| Organization | Role | View | Activity | Context |
|:-------:|:---:|:---:|:---:|:---:|

> _FLASK, PANDAS_
