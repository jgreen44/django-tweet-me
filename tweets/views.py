from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Tweet


def home_view(request, *args, **kwargs):
    print(kwargs)
    return HttpResponse('<H1>Hello World</H1>')


def tweet_detail_view(request, tweet_id):
    """
    REST API VIEW
    Consume by JavaScript or Swift or Java or iOS/Android
    return json data
    """

    data = {
        "id": tweet_id,
        # "content": obj.content,
        # "image_path": obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(pk=tweet_id)
        data['content'] = obj.content
    except:
        # raise Http404
        data['message'] = "Not Found!"
        status = 404

    # return HttpResponse(f'<H1>Hello {tweet_id} - {obj.content}</H1')
    return JsonResponse(data, status=status)
