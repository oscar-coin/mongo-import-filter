import os
import bz2
import json
import mongo_connection
import pymongo
import grossing_filter



path = "E:\Archive\Reddit"
report = ""
db = mongo_connection.MongoConnection().get_db()
# go through every folder
folders = os.listdir(path)


def _tryinsertmany(_collection, _bulk):
    if not _bulk:
        return
    success = False
    failed = False
    while not success:
        try:
            _collection.insert_many(_bulk)
            success = True
            if failed:
                print("I COULD CONNECT TO THE MONGO! (YAY! \\o/")
        except (pymongo.errors.ServerSelectionTimeoutError, pymongo.errors.WTimeoutError, pymongo.errors.ExecutionTimeout):
            if not failed:
                print("ERROR MONGO CONNECTION TIMED OUT - WILL KEEP TRYING - PLEASE FIX CONNECTION :(")
            failed = True


try:
    for dirpath, subdirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            # it is expected that the folder name is the year
            year = os.path.basename(os.path.normpath(dirpath))
            if year.startswith("_"):
                continue
            # exclude non bz2 files
            if not filepath.endswith(".bz2"):
                continue
            # open file with gzip
            try:
                print("opening file " + filename)
                file = bz2.open(filepath)
            except IOError:
                error = "ERROR opening file: " + filepath + " - file will be ignored"
                print(error)
                report += error + "\n"
                continue
            # drop collection if it already exists (!! so make sure the filenames are distinct! for reddit they are ^.^)
            if filename in db.collection_names():
                print("Dropping Collection " + filename)
                db[filename].drop()
            collection = db[filename]
            # go through every row (a line)
            bulk = []
            lines = 0
            filtered = 0
            print("reading lines now")
            for line in file:
                lines += 1
                row = json.loads(line.decode("utf-8"))
                row = grossing_filter.filter_row(row, year)
                if row is None:
                    continue
                # load object into bulk
                bulk.append(row)
                filtered += 1
                # insertmany is supposed to be faster, whatever
                if len(bulk) >= 15:
                    _tryinsertmany(collection, bulk)
                    bulk = []
            _tryinsertmany(collection, bulk)
            output = "Added " + str(filtered) + "documents from " + str(
                lines) + " in file " + filename + " in year " + str(year)
            print(output)
            report += output + "\n"
finally:
    print(report)




