def upload_user_profile__image(instance, filename):
    """Upload user profile image"""

    return f'images/{instance.user.username}_{instance.user.id}/{filename}'