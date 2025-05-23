from django.shortcuts import render
from .forms import ImageUploadForm
from django.conf import settings
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from io import BytesIO
import os

def predict(request):
    if request.method == 'GET':
        form = ImageUploadForm()
        return render(request, 'top.html', {'form': form})
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img_file = form.cleaned_data['image']
            img_file = BytesIO(img_file.read())
            img = load_img(img_file, target_size=(256, 256))
            img_array = img_to_array(img)
            img_array = img_array.reshape((1, 256, 256, 3))
            img_array = img_array/255
            model_path = os.path.join(settings.BASE_DIR, 'prediction', 'models', 'model.h5') 
            model = load_model(model_path)
            result = model.predict(img_array)
            probabilities = max(result[0].tolist())
            probabilities = round(probabilities * 100)
            if result[0][0] > result[0][1]:
                prediction = 'ブタクサ'
            else:
                prediction = 'セイタカアワダチソウ'
            img_data = request.POST.get('img_data')
            return render(request, 'top.html', {'form': form, 'prediction': prediction, 'img_data': img_data, 'probabilities': probabilities})
        else:
            form = ImageUploadForm()
            return render(request, 'top.html', {'form': form})

# gallery
from .models import PredictionResult

def gallery(request):
    results = PredictionResult.objects.order_by('-timestamp')  # 新しい順
    return render(request, 'gallery.html', {'results': results})