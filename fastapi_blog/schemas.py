from pydantic import BaseModel, Field, ConfigDict

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    ## This is done so that we can use the dot notation to access the fields of the post response
    model_config = ConfigDict(from_attributes=True)

    ## These are generated fields by the system and not the client 
    ## should not provide these fields when creating a post
    id: int
    date_posted: str


