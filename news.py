# -*- coding: utf-8 -*-

import http.client, urllib.parse, json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the subscriptionKey string value with your valid subscription key.
subscriptionKey = "fuck"

# Verify the endpoint URI.  At this writing, only one endpoint is used for Bing
# search APIs.  In the future, regional endpoints may be available.  If you
# encounter unexpected authorization errors, double-check this value against
# the endpoint for your Bing search instance in your Azure dashboard.
host = "api.cognitive.microsoft.com"
path = "/bing/v7.0/news/search"

term = "Microsoft"

def BingNewsSearch(search):
    "Performs a Bing News search and returns the results."

    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
    conn = http.client.HTTPSConnection(host)
    query = urllib.parse.quote(search)
    conn.request("GET", path + "?q=" + query, headers=headers)
    response = conn.getresponse()
    headers = [k + ": " + v for (k, v) in response.getheaders()
                   if k.startswith("BingAPIs-") or k.startswith("X-MSEdge-")]
    return headers, response.read().decode("utf8")

print('Searching news for: ', term)

headers, result = BingNewsSearch(term)
print("\nRelevant HTTP Headers:\n")
print("\n".join(headers))
print("\nJSON Response:\n")
print(json.dumps(json.loads(result), indent=4))