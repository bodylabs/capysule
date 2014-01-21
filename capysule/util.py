def split_full_name(full_name):
    '''
    Returns a tuple with a first and last name, from the given full
    name. If there is only one name component, returns a 2-tuple
    with None as the second element. If there are no name components,
    returns None.

    '''
    full_name = full_name.strip()
    if not full_name:
        return None

    names = full_name.strip().split(' ')
    if len(names) <= 1:
        return (full_name, None)

    last_name = names.pop(-1)
    first_name = ' '.join(names)
    return (first_name, last_name)
