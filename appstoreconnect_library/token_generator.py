import jwt
import datetime
import glob
import sys
import os
from . import PRIVATE_KEY_FOLDER


def generate_jwt_token(key_identifier, issuer):
    algorithm = 'ES256'
    token_duration = 120
    expiration = datetime.datetime.utcnow() + datetime.timedelta(seconds=token_duration)

    header = dict(alg=algorithm, kid=key_identifier, typ="JWT")
    payload = dict(iss=issuer, exp=expiration, aud="appstoreconnect-v1")

    private_keys_folder_path = os.path.join(os.curdir, PRIVATE_KEY_FOLDER, "*.p8")
    private_key_filename_candidates = glob.glob(private_keys_folder_path)
    number_of_private_keys = len(private_key_filename_candidates)
    if number_of_private_keys == 0:
        sys.exit('The private key is not on the folder {}'.format(PRIVATE_KEY_FOLDER))
    elif number_of_private_keys > 1:
        sys.exit('There must be only one private key on folder {}. There are actually {}.'.format(PRIVATE_KEY_FOLDER, number_of_private_keys))
    private_key_filename = private_key_filename_candidates[0]
    private_key = open(private_key_filename, "rb").read()

    encoded = jwt.encode(payload, private_key, algorithm=algorithm, headers=header)
    return encoded.decode()
