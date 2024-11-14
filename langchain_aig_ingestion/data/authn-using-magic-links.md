Overview
Magic link authentication is a passwordless [user authentication](/securebydesign/authn-intro/#value-of-authn) method that sends a single-use link to the user’s email address (or, less commonly, via SMS) to verify their identity. When the user clicks on the link, they are automatically (“magically”) logged in to the application (or there may be additional login steps that follow).
It can be used by itself for a potentially fully passwordless experience, for cases in which it provides an adequate level of security. More commonly though, it is used for [multi-factor authentication](/securebydesign/authn-intro/#mfa-and-2fa) (MFA), for example on top of [password-based authentication](/securebydesign/authn-using-passwords/), providing an additional layer of security. In terms of MFA, magic links are considered a “something the user has” factor since it proves the user has access to their email account – the presumption being that they are the only ones with access.
As a form of authentication, magic link authentication [provides](/securebydesign/authn-intro/#value-of-authn) gatekeeping, enhanced data security, and reduced abuse to your app. Having robust authentication bolsters the security of your application, builds trust with users by demonstrating a commitment to protecting their data, helps to safeguard your reputation, and can facilitate adherence to compliance standards. Magic links can provide strong authentication and do so in a way that is convenient for users. No standards govern magic link authentication. Each application can implement it in its own unique way, resulting in various variations and approaches and a lack of interoperability.
Magic link authentication
A dive into magic link authentication
This diagram presents an overview of the magic link authentication process:

As shown, the active entities involved in magic link authentication are:

- The user that needs to authenticate.
- The application the user is attempting to access. This must include a website.
- An email relay, used to transmit the magic link email.
- The user’s email service.
  When initializing a user session, the application will construct a unique URL. The initial elements of the URL correspond to the web server being used and specifically the handling logic for magic links. The URL contains a direct or indirect reference to the user (or the specific user session ID, if session initiation has begun). The session’s persistent state is updated with the specific details of the URL.
  The URL is then sent via email to the user. Once they receive it, they click on the hyperlink and it opens on the device they were viewing the email on. That causes the URL to be received by the magic link handling endpoint, which checks if the URL is valid and matches a magic link that was sent out. If it does, magic link authentication has succeeded for that session and the user may be logged in for that session. If there is no match to a valid transmitted magic link, no user session is established (see [below](#higher-security-implementation) for some best practices for this situation).
  This authentication mechanism is similar to how emails supporting email address verification or account recovery operate, though those are for different situations. Magic link authentication is also similar to [emailed one-time passcode (OTP) authentication](/securebydesign/authn-using-trx-otp/), but a URL is transmitted instead of an OTP and the user clicks on the URL rather than personally viewing and entering a code.
  Diving deeper
  To add magic link authentication to their app, developers will need to use a third-party authentication provider or build their own magic link authentication system.
  Typically, clicking the URL opens a new tab for the user and that is where the established authenticated session is located. The magic link handler could instead have the original browser tab become logged on. This is especially valuable for cases such as where:
- Users use your app on one device (such as a laptop) and read their email on a different device (such as their mobile phone).
- They use a different browser for reading email.
- They use your app in a browser or browser profile different from the one email links open to.

In such cases, without this special handling, the authenticated session could be in a suboptimal or incompatible location.
Often you will want to recognize the user as the same person across different sessions, so you will have an account database, holding information collected during user registration. This may be updated over time. To help protect against spamming and typos, you will likely want to verify the email address provided by the user.
Enhancing the security of magic links authentication
The strength of authentication offered by magic link authentication and imparted on your application depends on (1) the security of the user’s email account and (2) the application’s magic link implementation choices.
Raising the security of the user’s email account
You should inform and remind users that their email security may be the weakest security link. Encourage (and require if possible) the user to follow strong security practices for their email account such as requiring strong [authentication](/securebydesign/authn-intro/) on the account, such as by using a hard-to-guess unique password plus 2FA or using FIDO passkeys or WebAuth. Also, educate them about phishing.
