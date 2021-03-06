# Data Generator

Generate PIP<sup>[1](#myfootnote1)</sup> and PAP<sup>[2](#myfootnote2)</sup> datasets to be used in the AC<sup>[3](#myfootnote3)</sup> decision making as well as in the training processes.

- Generate _"empower"_ dataset : mapping **subjects** to **roles**

| Organization | Card ID | VIP badge | Role |
|:-------:|:---:|:---:|:---:|

- Generate _"use"_ dataset : mapping **objects** to **views**

| Organization | Plate ID | Company | Model | View |
|:-------:|:---:|:---:|:---:|:---:|

- Generate _"PAP"_ dataset : mapping **(org, role, view, activity, context)** to **(decision, proba)**

| Organization | Role | View | Activity | Context | Probability | Decision |
|:-------:|:---:|:---:|:---:|:---:|:---:|:---:|

- Two scripts : _"consider"_ and _"checkContext"_ to get the abstract entities for **actions** and **contexts** respectively are directlty stored in the PIP [see this link](../PIP/utils.py)

> _NUMPY, PANDAS, DATETIME, ITERTOOLS, SKLEARN_

# 
<h5>
<a name="myfootnote1">1</a>: Policy Information Point<br>
<a name="myfootnote2">2</a>: Policy Administration Point<br>
<a name="myfootnote3">3</a>: Access Control
</h5>
