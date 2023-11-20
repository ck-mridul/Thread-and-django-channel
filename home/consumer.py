from channels.generic.websocket import AsyncWebsocketConsumer
import json

class StudentsThread(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = "student_thread"
        self.room_group_name = "student_thread_group"
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        await self.send(text_data= json.dumps({'status':'connected to student thread'}))
        
    async def receive(self,data):
        await self.send(text_data= json.dumps({'status':data}))
        
        
    async def disconnect(self, code):
        return await super().disconnect(code)

        
    async def send_student_data(self,event):
        data = event.get('value')
        await self.send(text_data= json.dumps({'payload':data}))