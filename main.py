from model.pb import user_pb2

person = user_pb2.Person()
person.id = 5
person.name = "python write hong"
person.email = "write@python.com"
phone = person.phones.add()
phone.number = "555"
phone.type = user_pb2.Person.PhoneType.PHONE_TYPE_HOME

with open('sample.txt', "wb") as f:
  f.write(person.SerializeToString())