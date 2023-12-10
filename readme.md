# Mastopost 

This is the library of methods to automate posting to Mastodon.

## Preparation

1. Provide your mastodon `instanceAddress`, `clientAppName` (name of your application), `webSite` (if you have one) in `environment.py`
1. Register your app calling `registerApp()`.
1. Call `getAppAuthorizationLink()` - it will print the link - follow it in your browser. You have to log in with your Mastodon account and authorize your app to act on behalf of your account.
Paste the code you received to the `environment.py` as the value of `authorizationCode`.
_You can use the code you received only once. To get a new token you will have to repeat this manual procedure._
1.  Call the `getAuthenticationToken()`. It will print the token - copy it to your `environment.py` as the value of `authToken`.
1. You can verify the token calling `verifyToken(environment.authToken)`

## Post a status

`postStatus(status, idempotencyKey="")`
idempotencyKey is a string (not required) identfying your post to not make it twice in mastodon.

[Mastodon documentation](https://docs.joinmastodon.org/client/authorized/#login)
