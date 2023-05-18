import threading
from put_photos_to_redis import put_photos_to_redis
from insert_to_postgres import insert_to_postgres


if __name__ == "__main__":
    load_thread = threading.Thread(target=put_photos_to_redis)
    save_thread = threading.Thread(target=insert_to_postgres)

    load_thread.start()
    save_thread.start()
    load_thread.join()
    save_thread.join()
