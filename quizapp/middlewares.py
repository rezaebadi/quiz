from django.http import HttpResponseBadRequest
from django.utils.deprecation import MiddlewareMixin
from .models import Tenant

class TenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        host = request.get_host().split(':')[0] 
        parts = host.split('.')

        if len(parts) < 3:
            request.tenant = None
        else:
            subdomain = parts[0]  
            tenant = Tenant.objects.get(schema_name=subdomain)
            request.tenant = tenant



