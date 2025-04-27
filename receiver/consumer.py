from channels.generic.websocket import AsyncWebsocketConsumer
import os
import datetime

class AudioConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.filename = f"audio_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pcm"
        self.filepath = os.path.join('audio_files', self.filename)
        os.makedirs('audio_files', exist_ok=True)
        self.file = open(self.filepath, 'wb')
        await self.accept()
        print(f"Connection accepted, saving to {self.filepath}")

    async def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            self.file.write(bytes_data)

    async def disconnect(self, close_code):
        self.file.close()
        print(f"Connection closed, file saved: {self.filepath}")
