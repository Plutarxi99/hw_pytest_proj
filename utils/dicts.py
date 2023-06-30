#collection = {"vcs": "mercurial"}
#'mercurial'
#>>> get_val(data, "vcs", "git")
#'mercurial'
#>>> data = {}
#>>> get_val({}, "vcs", "git")
#'git'
#>>> get_val({}, "vcs", "bazaar")
#'bazaar'

def get_val(collection, key, default='git'):
    if collection == {}: return default
    for k, v in collection.items():
        if k == key:
            return v


#print(get_val(collection, "vcs"))