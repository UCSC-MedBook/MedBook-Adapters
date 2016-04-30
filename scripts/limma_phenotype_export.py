#! /usr/bin/env python

"""Export MedBook expression3 data into rectangular files.

Usage:
./limma_phenotype_export.py [group A sample group _id] [group B sample group _id]

File format:
```
Sample\tGroup
DTB-001\tFirst
DTB-002\tFirst
DTB-003\tSecond
DTB-004\tSecond
```

Dependancies:
pymongo
"""

import sys
import getopt
import pymongo

def writeGroupSamples(samples, name):
    for sample in samples:
        sys.stdout.write(sample + "\t" + name + "\n")

def exportLimmaPhenotype(db, sampleGroupAId, sampleGroupBId):
    sys.stdout.write("Sample\tGroup\n")

    sampleGroupA = db["sample_groups"].find_one({ "_id": sampleGroupAId })
    sampleGroupB = db["sample_groups"].find_one({ "_id": sampleGroupBId })

    for study in sampleGroupA["studies"]:
        writeGroupSamples(study["sample_labels"], "Group A")

    for study in sampleGroupB["studies"]:
        writeGroupSamples(study["sample_labels"], "Group B")

def main():
    argv = sys.argv

    # set up the database client
    db = pymongo.MongoClient()["MedBook"]

    if len(argv) == 3:
        exportLimmaPhenotype(db, argv[1], argv[2])
        sys.exit(0)

    print __doc__

if __name__ == "__main__":
    main()
