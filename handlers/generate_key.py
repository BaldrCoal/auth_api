import os
import uuid

from handlers.base_handler import BaseHandler


class GenerateKey(BaseHandler):
    async def get(self):
        self.set_header('Content-Type', 'application/json')
        print('generate key')
        project_id = str(uuid.uuid4())
        try:
            os.mkdir(f'./data/{project_id}')
            with open(f'./data/{project_id}/key.txt', 'w') as file:
                file.write(project_id)
            answer = {'project_id': {project_id}}
        except Exception as e:
            print(e)
            answer = {'error': f'{e}'}

        await self.finish(answer)
