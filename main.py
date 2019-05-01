import hashlib

import requests


def request_img(url, params=None):
    response = requests.get(url, params)
    if response.status_code != 200:
        e = Exception("HTTP status: " + response.status_code)
        raise e

    content_type = response.headers["content-type"]
    if 'image' not in content_type:
        e = Exception("Content-Type: " + content_type)
        raise e

    return response.content


def save_img(filename, image):
    with open(filename, "wb") as fout:
        fout.write(image)


###
# https://ja.gravatar.com/site/implement/images/
# d=
#   404: do not load any image if none is associated with the email hash, instead return an HTTP 404 (File Not Found) response
#   mp: (mystery-person) a simple, cartoon-style silhouetted outline of a person (does not vary by email hash)
#   identicon: a geometric pattern based on an email hash
#   monsterid: a generated 'monster' with different colors, faces, etc
#   wavatar: generated faces with differing features and backgrounds
#   retro: awesome generated, 8-bit arcade-style pixelated faces
#   robohash: a generated robot with different colors, faces, etc
#   blank: a transparent PNG image (border added to HTML below for demonstration purposes)
# r=
#   g: suitable for display on all websites with any audience type.
#   pg: may contain rude gestures, provocatively dressed individuals, the lesser swear words, or mild violence.
#   r: may contain such things as harsh profanity, intense violence, nudity, or hard drug use.
#   x: may contain hardcore sexual imagery or extremely disturbing violence.
# s=
#   You may request images anywhere from 1px up to 2048px, however note that many users have lower resolution images, so requesting larger sizes may result in pixelation/low-quality images.
###
BASE_URL = 'https://www.gravatar.com/avatar/'


def make_gravatar(source_txt, params=None):
    m = hashlib.md5()
    bytes_txt = source_txt.encode('utf-8')
    m.update(bytes_txt)
    url = BASE_URL + m.hexdigest()
    print(url)
    content = request_img(url, params)
    file_name = './avatar.jpg'
    save_img(file_name, content)


if __name__ == "__main__":
    txt = 'blah blah blah'
    params = {
        'd': 'monsterid',
        's': 200,
        'r': 'x'
    }
    make_gravatar(txt, params)
