# """
# MAC address finding
# """
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.core.exceptions import ValidationError, MultipleObjectsReturned
# from .models import HubStatus
# def create_response(error_message=None, status_code=200, data=None):
#     """Helper function to create JSON responses."""
#     if error_message:
#         return JsonResponse({'error': error_message}, status=status_code)
#     return JsonResponse(data, status=status_code)
# @csrf_exempt
# def ping(request):
#     """Handle POST requests to store and return MAC address information."""
#     if request.method == "POST":
#         # Extract the MAC address from the request POST data
#         mac_address = request.POST.get('mac_address')
#         if not mac_address:
#             return JsonResponse({'error': 'MAC address is required'}, status=400)
#         try:
#             # Validate and save the MAC address to the database
#             # pylint: disable=no-member
#             hub, created = HubStatus.objects.get_or_create(mac_address=mac_address)
#             response_data = {
#                 'id': hub.id,
#                 'mac_address': hub.mac_address,
#                 'timestamp': hub.timestamp
#             }
#             return JsonResponse(response_data, status=201 if created else 200)
#         except ValidationError as ve:
#             # Handle specific validation errors
#             return JsonResponse({'error': str(ve)}, status=400)
#         except HubStatus.DoesNotExist:
#             # Handle the case where the HubStatus object does not exist
#             return JsonResponse({'error': 'HubStatus object not found'}, status=404)
#         except MultipleObjectsReturned:
#             # Handle the case where multiple HubStatus objects are returned
#             return JsonResponse({'error': 'Multiple HubStatus objects found'}, status=400)
#         except TypeError as te:
#             # Handle type errors
#             return JsonResponse({'error': f'Type error: {str(te)}'}, status=400)
#         except ValueError as ve:
#             # Handle value errors
#             return JsonResponse({'error': f'Value error: {str(ve)}'}, status=400)
#         except Exception as se:
#             # Handle unexpected errors with a generic message
#             return JsonResponse({'error': f'An unexpected error occurred: {str(se)}'}, status=500)
#     # Handle other HTTP methods (GET, PUT, DELETE)
#     return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
"""
 MAC address finding
"""
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError, MultipleObjectsReturned
from .models import HubStatus
def create_response(error_message=None, status_code=200, data=None):
    """Helper function to create JSON responses."""
    if error_message:
        return JsonResponse({'error': error_message}, status=status_code)
    return JsonResponse(data, status=status_code)
@csrf_exempt
def ping(request):
    """Handle POST requests to store and return MAC address information."""
    if request.method != "POST":
        return create_response('Only POST requests are allowed', status_code=405)
    # Extract the MAC address from the request POST data
    mac_address = request.POST.get('mac_address')
    if not mac_address:
        return create_response('MAC address is required', status_code=400)
    try:
        # Validate and save the MAC address to the database
        hub, created = HubStatus.objects.get_or_create(mac_address=mac_address)
        response_data = {
            'id': hub.id,
            'mac_address': hub.mac_address,
            'timestamp': hub.timestamp
        }
        return create_response(data=response_data, status_code=201 if created else 200)
    except ValidationError as ve:
        # Handle specific validation errors
        error_message = str(ve)
        status_code = 400
    except HubStatus.DoesNotExist:
        # Handle the case where the HubStatus object does not exist
        error_message = 'HubStatus object not found'
        status_code = 404
    except MultipleObjectsReturned:
        # Handle the case where multiple HubStatus objects are returned
        error_message = 'Multiple HubStatus objects found'
        status_code = 400
    except TypeError as te:
        # Handle type errors
        error_message = f'TypeError: {str(te)}'
        status_code = 400
    except ValueError as ve:
        # Handle value errors
        error_message = f'ValueError: {str(ve)}'
        status_code = 400

    except Exception as e: # pylint: disable=broad-exception-caught
        # Handle unexpected errors with a generic message
        error_message = f'An unexpected error occurred: {str(e)}'
        status_code = 500
    return create_response(error_message=error_message, status_code=status_code)
