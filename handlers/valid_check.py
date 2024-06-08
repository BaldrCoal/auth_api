import os

from handlers.base_handler import BaseHandler


class ValidCheck(BaseHandler):
    async def get(self):
        self.set_header('Content-Type', 'application/json')
        print('link key')
        project_id = self.get_argument('project_id')
        pc_id = self.get_argument('pc_id')
        try:
            if os.path.exists(f'./data/{project_id}/pc_id.txt'):
                with open(f'./data/{project_id}/pc_id.txt', 'r') as file:
                    local_pc_id = file.read()
                with open(f'./data/{project_id}/key.txt', 'r') as file:
                    local_project_id = file.read()

                if pc_id == local_pc_id and project_id == local_project_id:
                    answer = {'result': 'true'}
                else:
                    answer = {'result': 'false'}
            else:
                answer = {'result': 'project id not exist'}
        except Exception as e:
            print(e)
            answer = {'error': f'{e}'}

        await self.finish(answer)
