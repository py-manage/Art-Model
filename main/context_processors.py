from .models import MockupType

def global_mockup_types(request):
    """ Maket turlarini barcha shablonlarga avtomat yetkazib beradi """
    return {
        'menu_mockup_types': MockupType.objects.all()
    }