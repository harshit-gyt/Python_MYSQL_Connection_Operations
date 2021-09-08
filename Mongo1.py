import pymongo

myclient = pymongo.MongoClient("localhost")
mydb = myclient["Blog_Database"]
mycol = mydb["Blog_collection"]

user1=[
    {"name":"Harshit" , "email" : "harshit@gmail.com", "blog": " harshit's blog "},
    {"name":"Mike" , "email" : "miku@gmail.com", "blog": " miku's blog "}
    ]
#user= {"name":"Harshit" , "email" : "harshit@gmail.com", "blog": " harshit's blog "}

mycol.insert_many(user1)

for x in mycol.find():
  print(x)

mycol.delete_many({
    "name":"Mike"
})
#
print('----------------------')
for x in mycol.find():
   print(x)


