import pymongo
from pymongo import MongoClient

def checkUsername(username):
    client = MongoClient('db.stuycs.org')
    db=client.admin
    db.authenticate('softdev','softdev')
    ans = False; 
    if (db.info.find_one({'username':username})):
        return ans;
    else: 
        ans = True;
        return ans;

def checkLogin(username, password): 
    client = MongoClient('db.stuycs.org')
    db=client.admin
    db.authenticate('softdev','softdev')
    ans = False;
    if checkUsername(username):
        if ((db.info.find({'username': username} , {"password" : password}))):
            ans = True;
            return ans;
        else: 
            return ans;
    else:
        return ans;

def addLogin(username, password): 
    client = MongoClient('db.stuycs.org')
    db=client.admin
    db.authenticate('softdev','softdev')
    if not checkUsername(username) and not checkLogin(username, password):
        db.info.insert ({'username':username}, {'password':password}, {'count': 0})

    
        
        
def increment(username):
    if checkUsername(username):
        c.info.find_one({'username':username}).update(count: count + 1);
    else:
        pass
    
        
    
