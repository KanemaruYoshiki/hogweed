from django.db import models

class PredictionResult(models.Model):
    image = models.ImageField(upload_to='uploads/')
    label = models.CharField(max_length=100)  # 例: 'ブタクサ' または 'セイタカアワダチソウ'
    confidence = models.FloatField()  # 信頼度（0.0〜1.0の範囲）
    timestamp = models.DateTimeField(auto_now_add=True)  # アップロード日時

    def __str__(self):
        return f"{self.label} ({self.confidence:.2f})"
