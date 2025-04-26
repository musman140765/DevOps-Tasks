import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set up logging
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(event_type)s - %(src_path)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class MonitorHandler(FileSystemEventHandler):
    def on_created(self, event):
        logging.info(f"created - {event.src_path}")

    def on_deleted(self, event):
        logging.info(f"deleted - {event.src_path}")

    def on_modified(self, event):
        logging.info(f"modified - {event.src_path}")

def main(path):
    event_handler = MonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    print(f"Monitoring started on: {path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 file_monitor.py <directory_to_watch>")
        sys.exit(1)

    path_to_watch = sys.argv[1]
    main(path_to_watch)
