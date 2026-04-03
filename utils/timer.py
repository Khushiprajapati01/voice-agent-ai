import time

class Timer:
    def __init__(self, label=""):
        self.label = label

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.elapsed = time.time() - self.start
        print(f"⏱️  {self.label}: {self.elapsed:.2f}s")
