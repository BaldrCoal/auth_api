import os

from handlers.base_handler import BaseHandler


class ValidCheck(BaseHandler):
    async def get(self):
        self.set_header('Content-Type', 'application/json')
        print('valid token')
        token = self.get_argument('token')
        pc_id = self.get_argument('pc_id')
        try:
            if os.path.exists(f'./data/{token}/pc_id.txt'):
                with open(f'./data/{token}/pc_id.txt', 'r') as file:
                    local_pc_id = file.read()
                with open(f'./data/{token}/token.txt', 'r') as file:
                    local_token = file.read()

                if pc_id == local_pc_id and token == local_token:
                    answer = {'result': 'true'}
                else:
                    answer = {'result': 'false'}
            else:
                answer = {'result': 'token not exist'}
        except Exception as e:
            print(e)
            answer = {'result': f'{e}'}

        await self.finish(answer)
