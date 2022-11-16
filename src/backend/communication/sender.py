from asyncio import open_connection

async def send_message(ip : str, port : int, message : str) -> None:
    try:
        _, writer = await open_connection(ip, port)
        writer.write(message.encode())
        await writer.drain()
        writer.close()
        return True
    except Exception as _:
        return False