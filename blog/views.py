from django.shortcuts import render

# we just built a view called 'post_list', it takes a request and returns a rendered version of 'blog/post_list.html'
def post_list(request):
    return render(request, 'blog/post_list.html', {})
