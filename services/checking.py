from database import Database

db = Database('insta_save.db')


def check_user(user):
    db_user = db.get_user_by_chat_id(user.id)
    if db_user:
        return db_user
    else:
        full_name = f"{user.first_name or ''} {user.last_name or ''}".strip()
        username = user.username or ""

        # create new user
        db.create_user(
            full_name=full_name,
            username=username,
            chat_id=user.id,
            lang='uz'
        )
        return None  # or return "created"