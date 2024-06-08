import os
import uuid

from handlers.base_handler import BaseHandler


class LinkToken(BaseHandler):
    async def post(self):
        self.set_header('Content-Type', 'application/json')
        print('link token')
        token = self.get_argument('token')
        pc_id = self.get_argument('pc_id')
        try:
            if os.path.exists(f'./non_used_tokens/{token}'):
                os.mkdir(f'./used_tokens/{token}')
                os.rmdir(f'./non_used_tokens/{token}')
                with open(f'./used_tokens/{token}/token.txt', 'w') as file:
                    file.write(token)
                with open(f'./used_tokens/{token}/pc_id.txt', 'w') as file:
                    file.write(pc_id)
                answer = {'result': 'success link'}
                print('success link')
            else:
                answer = {'result': 'token not exist'}
        except Exception as e:
            print(e)
            answer = {'result': f'{e}'}

        await self.finish(answer)