from django.shortcuts import render

# Create your views here.

def systemueberwachung(request):
    ort = "systemüberwachung"
    return render(request, 'website/systemüberwachung.html', {'ort' : ort})
def kamera(request):
    return render(request, 'website/kamera.html')
