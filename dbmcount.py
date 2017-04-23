#!/usr/bin/env python3
import dbm.gnu

db = dbm.gnu.open("oaiharvest.dbm", "r")
print(len(db))
