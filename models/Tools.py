from pydantic import BaseModel
import datetime

class Tool(BaseModel):
    name: str
    url: str
    type: str
    description: str
    logo_uri: str

class ProposalTool(BaseModel):
    name: str
    url: str
    description: str
    creationdate: datetime
    user_id: str
