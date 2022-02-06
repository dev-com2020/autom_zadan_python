from faker import Faker

fake = Faker('pl_PL')
# for _ in range(10):
#     print(fake.name())

print(fake.name())
print(fake.email())
print(fake.country())
print(fake.profile())
