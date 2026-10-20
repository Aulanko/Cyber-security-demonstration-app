# A02: Cryptographic Failures

### Addition to the Previously Created users, Lets create 2 "fan accounts" with the same exact passwords as their currently existing predecessors:

![Making Fan Accounts With the same passwords as the original ones](screenshots/Flaw2/image.png)

![Making Fan Accounts With the same passwords as the original ones](screenshots/Flaw2/image%20copy.png)

### And if we now run a command in the terminal to show all of our users and their hashed passwords we get:

![Making Fan Accounts With the same passwords as the original ones](screenshots/Flaw2/CheckingPasswordHashes.png)

### as we can see, the same exact passwords share the same hash