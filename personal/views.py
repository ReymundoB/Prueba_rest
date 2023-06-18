from django.shortcuts import render,redirect,get_object_or_404
from . models import Persona
from . form import PersonaForm
from django.contrib import messages

# Create your views here.

def index(request):
    dato=Persona.objects.all()


    return render(request, 'personal/index.html',{
        'datos':dato
    })


#Valida que pasa con el messages de success
def agregar(request):
    form=None

    if request.method=='POST':
        form_dato=PersonaForm(request.POST)
        if form_dato.is_valid():
            form_dato.save()
            #messages.SUCCESS(request,'Persona registrada con exito')
            redirect ('index_personal')
        else:
            messages.ERROR(request,'Lo siento, validar tus datos en el formulario')
            return render(request, 'personal/agregar.html',{
                'form':form_dato
            })

    else:
        form= PersonaForm()

    return render (request, 'personal/agregar.html',{
        'form':form
    })


def editar(request,id):
    #extraemos la info del id que no compartieron
    dato=get_object_or_404(Persona,pk=id)
    if request.method =='POST':
        #generamos un form con los datos nuevos
        actualizar=PersonaForm(request.POST, instance=dato)
        if actualizar.is_valid():
            actualizar.save()
            return redirect('index_personal')
        else:
            messages.ERROR(request, 'Favor de verificar tus campos del formulario')
            return render(request, 'personal/editar.html',{
                'form':actualizar
            })
        
    else:
        #generamos el form acorde a la info
        form=PersonaForm(instance=dato)

    return render(request, 'personal/editar.html',{
        'form':form
    })
    
def ver(request, id):
    dato=get_object_or_404(Persona,pk=id)
    form=PersonaForm(instance=dato)
    return render(request, 'personal/ver.html',{
        'form':form
    })

def eliminar(request, id):
    dato=get_object_or_404(Persona, pk=id)
    dato.delete()
    return redirect('index_personal')
    

