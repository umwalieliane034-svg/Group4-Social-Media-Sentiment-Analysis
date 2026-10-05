from django.db import models


class SentimentResult(models.Model):
    id = models.AutoField(primary_key=True)
    original_text = models.TextField()
    sentiment = models.FloatField(null=True)
    sentiment_label = models.CharField(max_length=20)
    prediction = models.CharField(max_length=20)
    primary_theme = models.CharField(max_length=100, null=True)
    main_emotion = models.CharField(max_length=100, null=True)
    processed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "sentiment_results"
