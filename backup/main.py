from dotenv import load_dotenv

from app.core.config import load_settings

def main() -> None:
    load_dotenv()
    load_settings()

    # print(os.environ)

    # watchers = []
    # paths = os.walk("../video")

    # # for index, path in enumerate(paths):
    # #     if index != 0:
    # #         print(path)
    # client = MongoClient("mongodb://root:admin@localhost:27017", uuidRepresentation="standard")
    # database = client["backup_db"]
    # coll = database["backups"]
    # key_id = "AKIA2XV6ME6PGEAIC66R"
    # key = "C/1g1ZAAtSK8+wG2D5EYejqa/6fDyGrBruVshYkn"

    # repo = BackupRepository(coll)
    # s3 = boto3.client(
    #     service_name="s3",
    #     region_name="us-east-2",
    #     aws_access_key_id=key_id,
    #     aws_secret_access_key=key
    # )
    # s3_service = S3Service(s3)


    # w = Watcher("../video/test001", repo, s3_service)
    # w.run()

if __name__ == "__main__":
    main()