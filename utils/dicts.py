def get_val(collection, key, default='git'):
    return collection[key] if collection.get(key) else default
