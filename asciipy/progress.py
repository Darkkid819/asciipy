import sys
import threading
import time


def spinning_cursor(event):
    while not event.is_set():  # Continue until the event is set
        for cursor in '|/-\\':
            sys.stdout.write(f'\rPlease wait while processing... {cursor}')
            sys.stdout.flush()
            time.sleep(0.1)
            if event.is_set():  # Break the inner loop if the event is set
                break
    sys.stdout.write('\rProcessing complete!                                \n')
    sys.stdout.flush()


def start_spinner():
    stop_event = threading.Event()
    spinner_thread = threading.Thread(target=spinning_cursor, args=(stop_event,))
    spinner_thread.start()
    return stop_event


def stop_spinner(stop_event):
    stop_event.set()
