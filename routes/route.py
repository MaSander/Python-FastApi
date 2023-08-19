from fastapi import APIRouter
from models.Tools import Tool
from repository.database import collection_name
from schema.tools import list_serial
from bson import ObjectId

router = APIRouter()

# TODO Ta certo isso não, mexendo no banco direto no Router cadé as camadas?

@router.get("/tools")
async def get_tools():
    tool = list_serial(collection_name.find())
    return tool

@router.post("/tool")
async def post_tool(tool: Tool):
    collection_name.insert_one(dict(tool))

@router.put("/tool/{id}")
async def put_tool(id: str, tool: Tool):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(tool)})

@router.delete("/tool/{id}")
async def delete_tool(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})