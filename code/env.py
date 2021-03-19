import ujson

env_file_name = 'env.json'

def get_all():
    file = open(env_file_name, 'r')
    contents = ujson.loads(file.read())
    file.close()

    return contents

def get(var_name):
    print('VAR NAME GET ' + var_name)

    contents = get_all()

    value = contents[var_name]

    print(value)
    print('---')

    return value

def set(var_name, value):
    print('VAR NAME SET ' + var_name + ' TO ' + value)

    contents = get_all()
    contents[var_name] = value

    file = open(env_file_name, 'w')
    file.write(ujson.dumps(contents))
    file.close()

    print('---')
