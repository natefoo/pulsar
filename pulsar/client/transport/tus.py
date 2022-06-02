import io
import logging
import os.path

try:
    from tusclient import client
    tus_available = True
except ImportError:
    tus_available = False


TUSCLIENT_UNAVAILABLE_MESSAGE = \
    "You are attempting to use the tusclient version of the Pulsar client but tusclient is unavailable."

CHUNK_SIZE = 10**7

NO_SUCH_FILE_MESSAGE = "Attempt to post file %s to URL %s, but file does not exist."
POST_FAILED_MESSAGE = "Failed to post_file properly for url %s, remote server returned status code of %s."
GET_FAILED_MESSAGE = "Failed to get_file properly for url %s, remote server returned status code of %s."


#class TusTransport:
#
#    def __init__(self, timeout=None, **kwrgs):
#        self.timeout = timeout
#

def post_file(url, path):
    if not os.path.exists(path):
        # pycurl doesn't always produce a great exception for this,
        # wrap it in a better one.
        message = NO_SUCH_FILE_MESSAGE % (path, url)
        raise Exception(message)


#def upload_file(url, path, api_key, history_id, file_type="auto", dbkey="?", filename=None, storage=None):
    #headers = {"x-api-key": api_key}
    #my_client = client.TusClient(f"{url}{UPLOAD_ENDPOINT}", headers=headers)
    #my_client = client.TusClient(f"{url}{UPLOAD_ENDPOINT}", headers=headers)
    my_client = client.TusClient(url)
    #filename = filename or os.path.basename(path)
    filename = path
    metadata = {
        "filename": filename,
        #"history_id": history_id,
        #"file_type": file_type,
        #"dbkey": dbkey,
    }

    # Upload a file to a tus server.
    storage = None
    if storage:
        storage = filestorage.FileStorage(storage)
    uploader = my_client.uploader(path, metadata=metadata, url_storage=storage)
    uploader.chunk_size = CHUNK_SIZE
    uploader.upload()


__all__ = [
    'post_file'
]
