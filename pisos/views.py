from django.shortcuts import render
from django.core.mail import send_mail
import json
from django.shortcuts import redirect
from django.http import  JsonResponse

# Create your views here.


def index(request):
    return render(request,'pisos/index.html')


def getContactForm(request):

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'POST':
        try:
            dats = json.loads(request.POST.get('dats'))
            print("enviando email")
            send_mail(
                'Solicitud de contacto',
                'nombre: %s \ncorreo: %s\ntelefono: %s'%(dats['nombre'],dats['correo'],dats['telefono']),
                'lavadodetanquessiamcosas@gmail.com',
                ['lavadodetanquessiamcosas@gmail.com'],
                fail_silently=False,
                )
            return JsonResponse({'success': True, 'msj': 'Solicitud de contacto enviada.\nEn un momento un asesor se pondra en contacto con usted'})

        except Exception as error:
            return JsonResponse({'success': False, 'msj': 'No pudimos procesar la solicitus \n error: %s.'%error})
    else:
        return redirect('index')
