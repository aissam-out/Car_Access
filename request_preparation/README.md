# Request preparation

After a user has checked out in the [Booking Portal](../Booking_Portal/), his information are stored in a MYSQL database.

Here we are about to prepare these scattered data and formulate them as a _get_access()_ request that will be received by the PEP<sup>[1](#myfootnote1)</sup>.

Optionally, we can also store the result in the _request.csv_ file.
 
The requests are sent using MQTT<sup>[2](#myfootnote2)</sup> which is a M2M<sup>[3](#myfootnote3)</sup>/IoT<sup>[4](#myfootnote4)</sup> open connectivity protocol. It was designed as an extremely lightweight publish/subscribe messaging transport.

# 
<h5>
<a name="myfootnote1">1</a>: Policy Enforcement Point<br>
<a name="myfootnote2">2</a>: Message Queuing Telemetry Transport<br>
<a name="myfootnote3">3</a>: Machine to Machine<br>
<a name="myfootnote4">4</a>: Internet of Things<br>
</h5>
