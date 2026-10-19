

# A01: Broken Access Control

### Register a new user:
![Registering a new user](screenshots/Flaw1/image.png)


### Login with that user:
![Login the new user](screenshots/Flaw1/image%20copy.png)


### Create a new note with that user:

![Going to notes section](screenshots/Flaw1/image%20copy%203.png)


### New note has been created now:
![Making a new Note](screenshots/Flaw1/image%20copy%204.png)

![Making a new Note](screenshots/Flaw1/image%20copy%205.png)


### Lets create another account and make a note with that one too:

![Making a new Note](screenshots/Flaw1/image%20copy%207.png)

![Making a new Note](screenshots/Flaw1/image%20copy%208.png)

![Making a new Note](screenshots/Flaw1/image%20copy%209.png)

![Making a new Note](screenshots/Flaw1/image%20copy%2010.png)

![Making a new Note](screenshots/Flaw1/image%20copy%2011.png)

### Here comes the Flaw:

### The user is able to see and even delete another users notes just by changing the Note ID value from the URL:

![Making a new Note](screenshots/Flaw1/image%20copy%2012.png)

### This applies for all users.

![Making a new Note](screenshots/Flaw1/image%20copy%2013.png)

### And after deleting a note:

![Making a new Note](screenshots/Flaw1/image%20copy%2014.png)
