from pydantic import BaseModel

class ImageData(BaseModel):
    image: str
    dict_of_vars: dict
    
    
# what type of data should we allow for a class - ImageDate here, basic @types using pydantic