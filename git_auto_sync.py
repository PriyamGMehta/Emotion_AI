import time
import subprocess
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configuration
SYNC_DELAY = 10  # Seconds to wait after the last file change before syncing

class GitSyncHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified_time = 0
        self.last_sync_time = time.time()
        
    def on_any_event(self, event):
        # Ignore Git directory and temporary files
        if ".git" in event.src_path or "__pycache__" in event.src_path or ".pytest_cache" in event.src_path:
            return
            
        # Update the last modified timestamp
        self.last_modified_time = time.time()

def sync_worker(handler):
    while True:
        time.sleep(1)
        current_time = time.time()
        
        # If files were modified AND we've waited 'SYNC_DELAY' seconds since the LAST modification
        if handler.last_modified_time > handler.last_sync_time and (current_time - handler.last_modified_time) >= SYNC_DELAY:
            print("\n[Auto-Sync] Changes stabilized. Pushing to GitHub...")
            try:
                # Add all changes
                subprocess.run(["git", "add", "."], check=True, stdout=subprocess.DEVNULL)
                
                # Check if there are actually things to commit
                status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
                if status.stdout.strip():
                    subprocess.run(["git", "commit", "-m", "Auto-sync update"], check=True, stdout=subprocess.DEVNULL)
                    subprocess.run(["git", "push"], check=True, stdout=subprocess.DEVNULL)
                    print("[Auto-Sync] Successfully synced to GitHub! ✅")
                else:
                    print("[Auto-Sync] No actual changes to commit.")
                
            except subprocess.CalledProcessError as e:
                print(f"[Auto-Sync] Error during git operations: {e}")
            
            # Update sync time so we don't sync again until new changes occur
            handler.last_sync_time = time.time()

if __name__ == "__main__":
    print("🚀 Starting Git Auto-Sync Watcher...")
    print(f"Monitoring folder for changes. Will auto-push to GitHub {SYNC_DELAY} seconds after you stop typing.")
    print("Press Ctrl+C to stop.\n")
    
    path = "."
    event_handler = GitSyncHandler()
    
    # Start the background sync worker thread
    worker_thread = threading.Thread(target=sync_worker, args=(event_handler,), daemon=True)
    worker_thread.start()
    
    # Start the watchdog directory observer
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n[Auto-Sync] Stopped monitoring.")
    observer.join()
