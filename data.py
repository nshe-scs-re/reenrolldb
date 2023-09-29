"""
User Mock Data
"""
user = {
    "id": "fd2vyoq6",
    "username": "",
    "sso_sub": "0000000-0000-0000-0000-00000000000",
    "sso_preferred_username": "user0",
    "sso_email": "user0@example.com",
    "sso_given_name": "User",
    "sso_family_name": "Name",
    "sso_name": "User Name",
    "preferred_username": "user0",
    "preferred_email": "user1@example.com",
}


"""
Courses Mock Data 
"""
# CS135
cs_135 = {
    "subject": "CS",
    "catalog_number": "135",
    "semester": "F23",
    "hidden": False
}

# CS202
cs_202 = {
    "subject": "CS",
    "catalog_number": "202",
    "semester": "F23",
    "hidden": False
}


"""
Services Mock Data
"""
service = {
    "name": "linux_remote_container",
    "display_name": "Linux Container Remote Desktop",
}


"""
Environment Mock Data
"""
env_dict = {
    "id": "expl_env",
    "name": "Example Environment",
    "type": "simple",
    "instance": {
        "id": "voEyCXba_d",
        "name": "instance0",
        "type": "container",
        "status": "",
        "control": True,
        "location": "localhost",
        "template": "cs135-f23",
        "devices": {
            "novnc": {
                "connect": "tcp:127.0.0.1:5801",
                "listen": "tcp:127.0.1.10:9000",
                "type": "proxy",
            },
            "ttyd": {
                "connect": "tcp:127.0.0.1:7681",
                "listen": "tcp:127.0.1.10:9001",
                "type": "proxy",
            },
            "vscode": {
                "connect": "tcp:127.0.0.1:3300",
                "listen": "tcp:127.0.1.10:9002",
                "type": "proxy",
            },
        },
        "config": None,
        "services": [
            {
                "display_name": "Terminal",
                "name": "ttyd",
                "address": "https://lx3.nevada.dev/expl_env/ttyd/",
            },
            {
                "display_name": "Visual Studio Code",
                "name": "vscode",
                "address": "https://lx3.nevada.dev/expl_env/vscode/",
            },
            {
                "display_name": "Desktop",
                "name": "novnc",
                "address": "https://lx3.nevada.dev/expl_env/novnc/vnc.html?path=expl_env/novnc/websockify&autoconnect=true&resize=remote&quality=8&compression=2",
            },
        ],
    },
    "user": {"id": "fd2vyoq6", "uid_number": "1000000", "username": "user0"},
    "course": None,
}

env_dict_no_vscode = {
    "id": "expl_env",
    "name": "Example Environment",
    "type": "simple",
    "instance": {
        "id": "voEyCXba_d",
        "name": "instance0",
        "type": "container",
        "status": "",
        "control": True,
        "location": "localhost",
        "template": "cs135-f23",
        "devices": {
            "novnc": {
                "connect": "tcp:127.0.0.1:5801",
                "listen": "tcp:127.0.1.10:9000",
                "type": "proxy",
            },
            "ttyd": {
                "connect": "tcp:127.0.0.1:7681",
                "listen": "tcp:127.0.1.10:9001",
                "type": "proxy",
            },
            "vscode": {
                "connect": "tcp:127.0.0.1:3300",
                "listen": "tcp:127.0.1.10:9002",
                "type": "proxy",
            },
        },
        "config": None,
        "services": [
            {
                "display_name": "Terminal",
                "name": "ttyd",
                "address": "https://lx3.nevada.dev/expl_env/ttyd/",
            },
            {
                "display_name": "Desktop",
                "name": "novnc",
                "address": "https://lx3.nevada.dev/expl_env/novnc/vnc.html?path=expl_env/novnc/websockify&autoconnect=true&resize=remote&quality=8&compression=2",
            },
        ],
    },
    "user": {"id": "fd2vyoq6", "uid_number": "1000000", "username": "user0"},
    "course": None,
}

env_test = {
    "id": "expl_env",
    "name": "Example Environment",
    "type": "simple",
    "instance": {
        "id": "voEyCXba_d",
        "name": "instance0",
        "type": "container",
        "status": "",
        "control": True,
        "location": "localhost",
        "template": "cs135-f23",
        "devices": {
            "novnc": {
                "connect": "tcp:127.0.0.1:5801",
                "listen": "tcp:127.0.1.10:9000",
                "type": "proxy",
            },
            "ttyd": {
                "connect": "tcp:127.0.0.1:7681",
                "listen": "tcp:127.0.1.10:9001",
                "type": "proxy",
            },
            "vscode": {
                "connect": "tcp:127.0.0.1:3300",
                "listen": "tcp:127.0.1.10:9002",
                "type": "proxy",
            },
        },
        "config": None,
        "services": [
            {
                "display_name": "Terminal",
                "name": "ttyd",
                "address": "https://lx3.nevada.dev/expl_env/ttyd/",
            },
            {
                "display_name": "Visual Studio Code",
                "name": "vscode",
                "address": "https://lx3.nevada.dev/expl_env/vscode/",
            },
            {
                "display_name": "Desktop",
                "name": "novnc",
                "address": "https://lx3.nevada.dev/expl_env/novnc/vnc.html?path=expl_env/novnc/websockify&autoconnect=true&resize=remote&quality=8&compression=2",
            },
        ],
    },
    "user": {"id": "fd2vyoq6", "uid_number": "1000000", "username": "user0"},
    "course": None,
}

env = {
    "id": env_dict_no_vscode["id"],
    "user": user,
    "document": env_dict_no_vscode
}