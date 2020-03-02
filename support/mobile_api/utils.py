from account.models import Profile

def get_user_by_token(token):
    try:
        pr = Profile.objects.get(sign=token)
        return pr.user
    except:
        return False