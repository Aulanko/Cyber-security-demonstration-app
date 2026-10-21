# A02: Cryptographic Failures After Fix

Let us create 2 accounts with the same password:

![Creating the same password](Demonstrations/screenshots/Flaw2%20fix/image.png)

![Creating the same password](Demonstrations/screenshots/Flaw2%20fix/image%20copy.png)

![Creating the same password](Demonstrations/screenshots/Flaw2%20fix/image%20copy%202.png)

![Creating the same password](Demonstrations/screenshots/Flaw2%20fix/image%20copy%203.png)

![Creating the same password](Demonstrations/screenshots/Flaw2%20fix/image%20copy%204.png)

And after running a script in the terminal to compare the newly made users passwords, we can see that the hashes indeed differ, unlike their predecessors above which were created before this fix.