from handlers.file_system_handler import MyEventHandler

from watchdog.observers import Observer

observer = Observer()
observer.schedule(MyEventHandler(), ".")
observer.start()
def test():
    try:
        while observer.is_alive():
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
