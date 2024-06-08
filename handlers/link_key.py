import os
import uuid

from handlers.base_handler import BaseHandler


class LinkKey(BaseHandler):
    async def post(self):
        self.set_header('Content-Type', 'application/json')
        print('link key')
        project_id = self.get_argument('project_id')
        pc_id = self.get_argument('pc_id')
        try:
            if os.path.exists(f'./data/{project_id}'):
                with open(f'./data/{project_id}/pc_id.txt', 'w') as file:
                    file.write(pc_id)
            answer = {'result': 'success link'}
            print('success link')
        except Exception as e:
            print(e)
            answer = {'error': f'{e}'}

        await self.finish(answer)