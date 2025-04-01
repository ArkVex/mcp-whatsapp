from typing import Any
import os
import sys
import asyncio
import pywhatkit as kit
import datetime
from mcp.server.fastmcp import FastMCP

# Setup virtual environment path
VENV_PATH = os.path.join(os.path.dirname(__file__), '.venv')
if os.path.exists(VENV_PATH):
    sys.path.insert(0, os.path.join(VENV_PATH, 'Lib', 'site-packages'))

mcp = FastMCP("whatsapp")

def schedule_message(phone_number: str, message: str) -> dict[str, Any]:
    """Schedule and send a WhatsApp message."""
    try:
        now = datetime.datetime.now()
        send_hour = now.hour
        send_minute = now.minute + 1

        # Send message using pywhatkit
        kit.sendwhatmsg(phone_number, message, send_hour, send_minute)
        return {"status": "success", "message": "Message scheduled successfully"}

    except Exception as e:
        return {"status": "error", "message": str(e)}

@mcp.tool()
async def send_whatsapp(phone_number: str, message: str) -> str:
    """Send a WhatsApp message to a specified number.

    Args:
        phone_number: The recipient's phone number (include country code)
        message: The message to send
    """
    result = schedule_message(phone_number, message)
    return result["message"]

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
