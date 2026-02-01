from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    country: str

class UserProfile(BaseModel):
    name: str
    address: Address  # Nested model

profile = UserProfile(
    name="Talal",
    address={"city": "Karachi", "country": "Pakistan"}
)

print(profile.address.city)



# class Product(BaseModel):
#     name: str
#     price: float = Field(..., gt=0)  # Must be > 0
#     category: str = Field(min_length=3, max_length=50)

# product = Product(name="Laptop", price=0, category="Electronics")
# print(product.model_dump_json)


# class User(BaseModel):
#     name: str
#     age: int
#     is_active: bool = True


# user = User(name="Talal", age="twenty")
# print(user)