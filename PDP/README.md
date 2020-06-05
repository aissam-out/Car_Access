# Policy Decision Point

The policy decision point (a.k.a. PDP) is the component of access control system that decides whether or not to authorize a user’s request, based on available information from the PIP<sup>[1](#myfootnote1)</sup> and security policies from the PAP<sup>[2](#myfootnote2)</sup>.

This implementation provides an extra feature : In case the received request contains fields the system have never dealt with, the PDP predicts the answer based on machine learning algorithms ([Catboost](https://catboost.ai/) in our case).

Here is the pseudocode which details how this algorithm works

![The building blocks of the implementation](./images/pdpseudo.PNG)

> _CATBOOST_

# 
<h5>
<a name="myfootnote1">1</a>: Policy Information Point<br>
<a name="myfootnote2">2</a>: Policy Administration Point<br>
</h5>
