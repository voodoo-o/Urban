calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(s):
    count_calls()
    cort = (len(s), s.upper(), s.lower())
    return cort


def is_contains(s, list_to_search):
    count_calls()
    new_list_to_search = []

    for i in list_to_search:
        new_list_to_search.append(i.lower())

    if s.lower() in new_list_to_search:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
