from django.shortcuts import render
from requests_oauthlib import OAuth1Session
from urllib.parse import parse_qsl
from . import config
# Create your views here.
def post_list(request):
    #カスタマーキー
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    consumer_key = CK
    consumer_secret = CS

    request_token_url = "https://api.twitter.com/oauth/request_token"

    # Twitter Application Management で設定したコールバックURLsのどれか
    oauth_callback = "http://118.27.13.21/"

    twitter = OAuth1Session(consumer_key, consumer_secret)

    response = twitter.post(
        request_token_url,
        params={'oauth_callback': oauth_callback}
    )

    # responseからリクエストトークンを取り出す
    request_token = dict(parse_qsl(response.content.decode("utf-8")))

    # リクエストトークンから連携画面のURLを生成
    authenticate_url = "https://api.twitter.com/oauth/authenticate"
    authenticate_endpoint = '%s?oauth_token=%s' \
        % (authenticate_url, request_token['oauth_token'])
    result = {'result' : authenticate_endpoint}


    return render(request, authenticate_endpoint,result)
