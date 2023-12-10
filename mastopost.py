import environment
import requests
import json

def registerApp():
    data = {
        "client_name": environment.clientAppName,
        "redirect_uris": "urn:ietf:wg:oauth:2.0:oob",
        "scopes": "read write push",
        "website": environment.webSite
    }

    response = requests.post("{}/api/v1/apps".format(environment.instanceAddress), data=data)

    return response.text

def getAppRegistrationData():
    try:
        with open("appRegistrationData.json", "r") as fp:
            appRegistrationData = json.load(fp)
    except:
        appRegistrationJSON = registerApp()
        appRegistrationData = json.loads(
            appRegistrationJSON
        )
        with open("appRegistrationData.json", "w") as fp:
            fp.write(appRegistrationJSON)

    return appRegistrationData


def getAppAuthorizationLink():
    appRegistrationData = getAppRegistrationData()
    link = ("{}/oauth/authorize?client_id={}&scope=read+write+push&redirect_uri={}&response_type=code"\
                            .format(environment.instanceAddress, appRegistrationData["client_id"], appRegistrationData["redirect_uri"]))
    print(link)
    return link


def getAuthenticationToken():
    appRegistrationData = getAppRegistrationData()
    data = {
        "client_id": appRegistrationData["client_id"],
        "client_secret": appRegistrationData["client_secret"],
        "redirect_uri": appRegistrationData["redirect_uri"],
        "grant_type": "authorization_code",
        "code": environment.authorizationCode,
        "scope": "read write push"
    }
    response = requests.post("{}/oauth/token".format(environment.instanceAddress), data=data)

    responseData = json.loads(response.text)
    if "access_token" in responseData:
        token = responseData["access_token"]
    else:
        token = response.text

    print(token)

    return token


def verifyToken(token):
    headers = {
        "Authorization": "Bearer {}".format(token)
    }

    response = requests.get("{}/api/v1/apps/verify_credentials".format(environment.instanceAddress), headers=headers)

    return response.text


def postStatus(status, idempotencyKey=""):
    headers = {
        "Authorization": "Bearer {}".format(environment.authToken),
        "Idempotency-Key": idempotencyKey
    }

    data = {
        "status": status,
        "visibility": "public"
    }

    response = requests.post("{}/api/v1/statuses".format(environment.instanceAddress), headers=headers, data=data)

    return response



if __name__ == "__main__":
    # getAppAuthorizationLink()
    # token = getAuthenticationToken()
    # print(token)
    # print(verifyToken(environment.authToken))

    # testStatus = 'test7 https://celestial.ink test'
    # print(
    #     postStatus(testStatus, testStatus)
    # )
    pass
