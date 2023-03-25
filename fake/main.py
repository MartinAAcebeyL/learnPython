from faker import Faker
fake = Faker()
# first, import a similar Provider or use the default one
from faker.providers import BaseProvider, DynamicProvider

# create new provider class
class MyProvider(BaseProvider):
    def first(self) -> str:
        return 'my first provider'

# then add new provider to faker instance
fake.add_provider(MyProvider)

# now you can use:
print(fake.first())
# 'bar'


#dynamic provider
medical_professions_provider = DynamicProvider(
    provider_name="medical_profession",
    elements=["dr.", "doctor", "nurse", "surgeon", "clerk"],
)


fake.add_provider(medical_professions_provider)
print(fake.medical_profession())