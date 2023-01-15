import os
import boto3

from pymongo import MongoClient

from app.api.watcher import Watcher
from app.db.repositories.backup_repository import BackupRepository
from app.aws.services.s3_service import S3Service


def main() -> None:
    watchers = []
    paths = os.walk("../video")

    # for index, path in enumerate(paths):
    #     if index != 0:
    #         print(path)
    client = MongoClient("mongodb://root:admin@localhost:27017", uuidRepresentation="standard")
    database = client["backup_db"]
    coll = database["backups"]
    key_id = "AKIA2XV6ME6PGEAIC66R"
    key = "C/1g1ZAAtSK8+wG2D5EYejqa/6fDyGrBruVshYkn"



    repo = BackupRepository(coll)
    s3 = boto3.resource(
        service_name="s3",
        region_name="us-east-2",
        aws_access_key_id=key_id,
        aws_secret_access_key=key
    )

    for bucket in s3.buckets.all():
        print(bucket.name)
        
    w = Watcher("../video/test001", database)
    w.run()

if __name__ == "__main__":
    main()