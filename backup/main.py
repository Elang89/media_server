from app.api.watcher import Watcher

def main() -> None:
    path = "../video"
    w = Watcher(path )
    w.run()

if __name__ == "__main__":
    main()