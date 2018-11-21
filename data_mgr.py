import os

def dict_to_file(dict_to_save, filename):
    filename = get_filepath(filename)
    with open(filename, 'w') as f_write:
        for method, count in dict_to_save.items():
            f_write.write(method +": "+str(count)+'\n')


def get_filepath(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path + '/' + filename


def method_to_file(method, filename):
    d = text_to_dict(filename)
    d[method] += 1
    dict_to_file(d, filename)
    return d


def text_to_dict(filename):
    d = {}
    with open(filename, 'r') as f_write:
        for line in f_write:
            line.replace("\n", "")
            (key, val) = line.split(":")
            d[key] = int(val)
    print(d)
    return d

