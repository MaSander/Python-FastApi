def individual_serial(tool) -> dict:
    return {
        "id": str(tool["_id"]),
        "name": tool["name"],
        "url": tool["url"],
        "type": tool["type"],
        "description": tool["description"],
        "logo_uri": tool["logo_uri"]
    }

def list_serial(tools) -> list:
    return[individual_serial(tool) for tool in tools]