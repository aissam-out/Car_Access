# Policy Administration Point

The policy administration point (a.k.a. PAP) is the interface or tool that enables you to create, edit and store digital policies or rules.

- The _csv_pap_ is the dataset mapping each set of _(org, role, view, ay, Cxt)_ to a decision and a level of confidence regarding this decision

| Organization | Role | View | Activity | Context | Probability | Decision |
|:-------:|:---:|:---:|:---:|:---:|:---:|:---:|

- The file _response.csv_ is optional : it serves to store the result after answering a given request 

- On top of the dataset, our PAP provides a [Flask](https://flask.palletsprojects.com) based web framework able to receive _get_decision_ requests from the PDP using JSON format.

> _FLASK, PANDAS_
