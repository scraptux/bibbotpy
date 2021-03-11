from http.cookiejar import CookieJar
from urllib import request, parse


cookies = CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cookies))


def login(t, user, pswd):
    # ----------- access login page --------------
    url = t['location']['url'] + "/index.php?login="
    response = opener.open(url)

    # ----------- send login info ----------------
    url = "https://idp.ub.uni-frankfurt.de/idp/profile/SAML2/Redirect/SSO?execution=e1s1"
    data = parse.urlencode(
        {"j_username": user, "j_password": pswd, "_eventId_proceed": ""}
    ).encode()
    response = opener.open(url, data=data)
    html = response.read().decode("utf-8")
    unique_select = 'RelayState" value="'
    relay_state = html[html.index(unique_select)+len(unique_select):]
    relay_state = relay_state[:relay_state.index('"')].replace('&#x3a;', ':')
    unique_select = 'SAMLResponse" value="'
    saml_response = html[html.index(unique_select)+len(unique_select):]
    saml_response = saml_response[:saml_response.index('"')]

    # ----------- redirect to ticket site ------------
    url = "https://buchung.ub.uni-frankfurt.de/Shibboleth.sso/SAML2/POST"
    data = parse.urlencode({"SAMLResponse": saml_response, "RelayState": relay_state}).encode()
    response = opener.open(url, data=data)

    t['location']['url'] = response.url


def logout():
    pass  # TODO
