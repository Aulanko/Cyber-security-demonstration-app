# A07: Identification and Authentication Failures

### For this spesific category we have multiple demonstrations:

Such as the user is able to register with a weak password:

![Registering with a weak password](screenshots/Flaw4/flaw4_before_weak_password/image.png)

![Registering with a weak password](screenshots/Flaw4/flaw4_before_weak_password/image%20copy.png)

![Registering with a weak password](screenshots/Flaw4/flaw4_before_weak_password/image%20copy%202.png)

The attacker is able to get useful feedback from failed logins:

![Useful feedback for the attacker](screenshots/Flaw4/flaw4_before_enum_wrongpw/image.png)

![Useful feedback for the attacker](screenshots/Flaw4/flaw4_before_enum_wrongpw/image%20copy.png)

![Useful feedback for the attacker](screenshots/Flaw4/flaw4_before_enum_nouser/image.png)

![Useful feedback for the attacker](screenshots/Flaw4/flaw4_before_enum_nouser/image%20copy.png)

And the there is no rate-limiting, so it is possible to brute force a password guess correctly

![Brute force](screenshots/Flaw4/flaw_4_before_rate_limiting/image.png)