from models import AdminUser


def get_admin_user_by_name(username):
    try:
        admin_user = AdminUser.objects.get(name=username)
    except:
        admin_user = None

    return admin_user
