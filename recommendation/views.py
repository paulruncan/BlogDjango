from django.shortcuts import render

from recommendation.recommendation import get_recommendations


# Create your views here.
def recommend_view(request):
    if not request.user.is_authenticated:
        return render(request, 'recommended_posts.html',{'error':'You are not logged in'})
    recommendations = get_recommendations(request.user)

    return render(request, 'recommended_posts.html',{'recommendations':recommendations})
