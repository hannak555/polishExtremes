import os
## copy this file to mysecrets.py and adapt your private settings (cp mysecrets.orig.py mysecrets.py)

## setings for inquiring articles from newsapi.org
#  Get API Key: https://newsapi.org/register &  https://newsapi.org/account

if(not os.getenv('NEWSAPI_KEY')):
    print("NEWSAPI_KEY not yet set.")
    os.environ['NEWSAPI_KEY'] = '1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7'
else:
    print("NEWSAPI_KEY already set.")

# https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
if(not os.getenv('EXTREME_GH_TOKEN')):
    print("EXTREME_GH_TOKEN not yet set.")
    os.environ['EXTREME_GH_TOKEN'] = 'ghp_1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f'
else:
    print("EXTREME_GH_TOKEN already set.")
