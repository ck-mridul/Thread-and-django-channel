import asyncio
from threading import Thread
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from faker import Faker
from .models import Students
import random
import time

fake = Faker()

class CreateStudentsThread(Thread):
    def __init__(self, total):
        self.total = int(total)
        Thread.__init__(self)

    def run(self):
        try:
            channel_layer = get_channel_layer()
            current_total = 0
            for i in range(self.total):
                current_total += 1
                student_obj = Students.objects.create(
                    student_name=fake.name(),
                    student_email=fake.email(),
                    address=fake.address(),
                    age=random.randint(10, 25)
                )
                
                
                data = {
                    'student_name': student_obj.student_name,
                    'student_email': student_obj.student_email,
                    'address': student_obj.address,
                    'age': student_obj.age,
                    'current_total':current_total,
                    'total' :self.total
                }
                async_to_sync(channel_layer.group_send)(
                    'student_thread_group', {
                        'type': 'send_student_data',
                        'value': data
                    }
                )
                # time.sleep(1)

        except Exception as e:
            print(e)
