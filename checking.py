from database import Database

db = Database('insta_save.db')


def check_user(user):
    db_user = db.get_user_by_chat_id(user.id)
    if db_user:
        return db_user
    else:
        # user create
        db.create_user(full_name=user.full_name,
                       username=user.username,
                       chat_id=user.id,
                       lang='uz')
        return False


def check_channel(user):
    channels = db.get_channels()
    print(channels)
    return channels