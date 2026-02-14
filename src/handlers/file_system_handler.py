from watchdog.events import FileSystemEventHandler

class MyEventHandler(FileSystemEventHandler):

    def on_modified(self, event):
        print(event.src_path, "modificado")
    def on_created(self, event):
        print(event.src_path, "creado.")
    
    def on_moved(self, event):
        print(event.src_path, "movido a", event.dest_path)
    
    def on_deleted(self, event):
        print(event.src_path, "eliminado.")