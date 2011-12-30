from google.appengine.ext import db
import cgi
import os
import time

class Entry(db.Model):
    name = db.StringProperty(required=True)
    id = db.IntegerProperty(required=True)
    value = db.StringProperty(required=True)
    timestamp = db.IntegerProperty(required=True)

form = cgi.FieldStorage()
print "Content-Type: text/javascript\n"

def process():
    if not "since" in form:
        return '{error: "Missing since-parameter"}'
    since = int(form["since"].value)

    if not "name" in form:
        return '{error: "Missing name-parameter"}'
    name = form["name"].value

    if "id" in form and "value" in form:
        id = int(form["id"].value)
        value = form["value"].value
        key_name = name + str(id)
        if not Entry.get_by_key_name(key_name) is None:
            return '{error: "Name/id combination already exists"}'
        entry = Entry(
            name = name,
            id = id,
            value = value,
            timestamp = int(time.time()*1000),
            key_name = key_name
            )
        entry.put()


    result = db.GqlQuery("SELECT * FROM Entry WHERE name = :1 AND timestamp >= :2 LIMIT 1000", name, since)
    result = ['{id:%d,value:"%s",timestamp:%d}' % (x.id, x.value, x.timestamp) for x in result]
    return "[" + ",".join(result) + "]"

if "callback" in form:
    print form["callback"].value + "(" + process() + ");"
else:
    print process()
