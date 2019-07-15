import pymongo  
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.text1
collection = db.info
#inff={ 'name':"hjfffhjas",
#     'age':2332,
#     'a':[{'qwe':'as',
#           'asd':'qwe'
#         },
#          {'ert':'tyu',
#           'rty':212
#              }
#          ]
#    }
#result = collection.insert(inff)
#print(result)
a = collection.find()[1]#.count()  
#
print(type(a))
for i in a.items():
    print(i)
#    b=i.get("a")
#    if b:
#        print(b[1].get('rty'))
#        c=b[1].get('rty')
#db2 = client.text2
#collection2 = db2.abc
#iff={
#    'qwe':b,
#    'ab':[{'qwe':'as',
#           'asd':'qwe'
#         },
#          {'ert':c,
#           'rty':212
#              }
#          ]

#    }
#result2 = collection2.insert(iff)
#print(result2)
