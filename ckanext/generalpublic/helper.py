import ckan.plugins.toolkit as tk

# Checks if the user is logged in
# Logged in users with have a tk.c.userobj
# Users not logged in will not have a tk.c.userobj
def is_logged_in():
    if tk.c.userobj is not None:
        return True
    else:
        return False

def is_public(packageid):

    data = {'packageid': packageid}

    visibility = tk.get_action('get_package_visibility')({'ignore_auth': True}, data)

    try: 
        if visibility.visibility == "Public":
            return True
        else:
            return False
    except:
        return False
    