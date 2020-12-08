import hashlib


def md5_generator(path):
    with open(path, 'r', encoding='utf-8') as f:
        for string in f:
            md5_hash = hashlib.md5()
            md5_hash.update(string.encode('utf-8'))
            result = md5_hash.hexdigest()
            yield print(result)


if __name__ == '__main__':
    gen_md5 = md5_generator('result.txt')
    for line in gen_md5:
        next(gen_md5)
