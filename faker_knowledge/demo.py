# import random
#
from faker import Faker
#
# # Faker.seed(10000)
fake = Faker(locale='zh_CN')
# fake = Faker()
#
#
print(fake.name())
#
# print(fake.phone_number())
#
# print(fake.date())
#
# print(fake.date_between('-30y', '-1y'))
# print(type(fake.date_between('-30y', '-1y')))
# print(str(fake.date_between('-10y', '-1y'))[:-3])
#
print(fake.random_int(1,21))
# #
# #
# # print(fake.date_this_month())
# #
#
# print(f"身份证号：{fake.ssn()}")
# print(fake.random_number(digits=9))
print(fake.text())
#
# print(str(fake.date_between('-10y', '-1y'))[:4])
#
#
# l = [ _ for _ in range(5, 101, 5) ]
#
# # random.seed(9001)
# print(random.choice([ _ for _ in range(5, 101, 5) ]))
# # print(random.choice([ _ for _ in range(5, 101, 5) ]))
#
#
#
# print(random.randint(0,1000000))
#
#
# print(fake.uuid4())
#
#
#
#
#
