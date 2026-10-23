

The user is no longer able to create an account with a weak password:

![Trying to create an account with a weak password](screenshots/Flaw4-fix/weak-password-fix/image.png)

![Trying to create an account with a weak password](screenshots/Flaw4-fix/weak-password-fix/image%20copy.png)

![Trying to create an account with a weak password](screenshots/Flaw4-fix/weak-password-fix/image%20copy%202.png)

![Trying to create an account with a weak password](screenshots/Flaw4-fix/weak-password-fix/image%20copy%203.png)


In addition the user is no longer able to get useful feedback from login that could help him with guessing an existing password or an username

![Unable to get pw data](screenshots/Flaw4-fix/wrongpw-log-fix/image.png)

![Unable to get pw data](screenshots/Flaw4-fix/wrongpw-log-fix/image%20copy.png)

![Unable to get pw data](screenshots/Flaw4-fix/wrongpw-log-fix/image%20copy%202.png)

![Unable to get username data](screenshots/Flaw4-fix/nouser-log-fix/image.png)

![Unable to get username data](screenshots/Flaw4-fix/nouser-log-fix/image%20copy.png)

Also after adding rate-limiting here, brute-force attacks no longer work the same way:

![unable to brute-force efficiently](screenshots/Flaw4-fix/after_rate_limiting-fix/image.png)

![unable to brute-force efficiently](screenshots/Flaw4-fix/after_rate_limiting-fix/image%20copy.png)