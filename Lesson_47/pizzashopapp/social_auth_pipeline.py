from pizzashopapp.models import Client

def create_client(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        avatar = 'https://graph.facebook.com/%s/picture?type=large' % response['id']

    if not Client.objects.filter(user_id=user.id):
        Client.objects.create(user_id=user.id, avatar = avatar)
