# exercise-docker
short interview exercise for backend position

----
Please create two docker containers:
container1 - should be able to accept a string through http
container2 - hosts a simple mongodb database

Once container1 receives a string (e.g. “foo”) it will append something to it (e.g. “bar”) and will then send the original string as well as the modified one (“foo” + “foobar”) to container2. Both strings are then saved in the database of container2 together with a timestamp.

Ideally the two containers are not on the same host, but are instead linked through a private network which they use for communication.

If  needed we can create a digital ocean (or similar) account for you to deploy this.

As a result please provide access to the deployed system as well as the code itself incl. deployment instructions.

Needless to say this does not need to be super polished, just a rough working prototype.
Security for the transmission of the data is of no concern whatsoever.
----
