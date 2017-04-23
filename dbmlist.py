#!/usr/bin/env python3
import dbm.gnu

db = dbm.gnu.open("oaiharvest.dbm", "r")

for key in db.keys():
    print(key)
    print(db[key])
