from application.models import *

def get_account_type(user):
    query1 = lawyer.objects.filter(user = user)
    query2 = client.objects.filter(user = user)
    output = {}
    if query1.exists():
        output['status'] = "lawyer"
        output['details'] = query1[0]    
    elif query2.exists():
        output['status'] = "client"  
        output['details'] = query2[0]  
    elif user.is_superuser:
        output['status'] = "admin"
    else:
        output['status'] = None

    return output

