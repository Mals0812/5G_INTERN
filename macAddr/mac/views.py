from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import hub_status

@csrf_exempt  # Decorator to exempt CSRF verification for this view
def ping(request):
    if request.method == "POST":
        try:
            # Extract the MAC address from the request POST data
            mac_address = request.POST.get('mac_address')
            
            if not mac_address:
                return JsonResponse({'error': 'MAC address is required'}, status=400)
            
            # Validate and save the MAC address to the database
            hub, created = hub_status.objects.get_or_create(mac_address=mac_address)
            
            return JsonResponse({'id': hub.id, 'mac_address': hub.mac_address, 'timestamp': hub.timestamp}, status=201)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    # Handle other HTTP methods (GET, PUT, DELETE)
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
