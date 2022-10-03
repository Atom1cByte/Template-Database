from prisma import Prisma

class Database():
    def __init__(self):
        self.client = Prisma(auto_register=True)
        self.connected = False

    async def _connect(self):
        if self.connected:
            return self.client
        await self.client.connect()
        self.connected = True
        return self.client
    
    async def _disconnect(self):
        if not self.connected:
            return self.client
        await self.client.disconnect()
        self.connected = False
        return self.client