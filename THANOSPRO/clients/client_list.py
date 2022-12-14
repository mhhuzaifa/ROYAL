from telethon.utils import get_peer_id
from telethon.tl.functions.users import GetFullUserRequest

from .session import rishu, H2, H3, H4, H5
from THANOSPRO.sql.gvar_sql import gvarstat


async def clients_list():
    user_ids = []
    if gvarstat("SUDO_USERS"):
        a = gvarstat("SUDO_USERS").split(" ")
        for b in a:
            c = int(b)
            user_ids.append(c)
    main_id = await rishu.get_me()
    user_ids.append(main_id.id)

    try:
        if H2 is not None:
            id2 = await H2.get_me()
            user_ids.append(id2.id)
    except:
        pass

    try:
        if H3 is not None:
            id3 = await H3.get_me()
            user_ids.append(id3.id)
    except:
        pass

    try:
        if H4 is not None:
            id4 = await H4.get_me()
            user_ids.append(id4.id)
    except:
        pass

    try:
        if H5 is not None:
            id5 = await H5.get_me()
            user_ids.append(id5.id)
    except:
        pass

    return user_ids


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        ultronceo = uid.user.id
        rishu_USER = uid.user.first_name
        rishu_mention = f"[{rishu_USER}](tg://user?id={ultronceo})"
    else:
        client = await event.client.get_me()
        uid = get_peer_id(client)
        ultronceo = uid
        rishu_USER = client.first_name
        rishu_mention = f"[{rishu_USER}](tg://user?id={ultronceo})"
    return ultronceo, rishu_USER, rishu_mention
