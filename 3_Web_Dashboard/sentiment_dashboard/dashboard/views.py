from django.shortcuts import render
from .models import SentimentResult


def dashboard(request):
    total = SentimentResult.objects.count()

    positive = SentimentResult.objects.filter(
        prediction="Positive"
    ).count()

    negative = SentimentResult.objects.filter(
        prediction="Negative"
    ).count()

    positive_percent = round((positive / total) * 100, 2) if total else 0
    negative_percent = round((negative / total) * 100, 2) if total else 0

    selected_sentiment = request.GET.get("sentiment", "")

    recent_results = SentimentResult.objects.order_by("-processed_at")

    if selected_sentiment in ["Positive", "Negative"]:
        recent_results = recent_results.filter(
            prediction=selected_sentiment
        )

    recent_results = recent_results[:10]

    accuracy = 69.45

    context = {
        "total": total,
        "positive": positive,
        "negative": negative,
        "positive_percent": positive_percent,
        "negative_percent": negative_percent,
        "recent_results": recent_results,
        "accuracy": accuracy,
        "selected_sentiment": selected_sentiment,
    }

    return render(request, "dashboard/dashboard.html", context)