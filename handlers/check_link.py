import os
import uuid

from handlers.base_handler import BaseHandler


class CheckLink(BaseHandler):
    async def get(self):
        self.set_header('Content-Type', 'application/json')
        print('check link')
        token = self.get_argument('token')
        try:
            if os.path.exists(f'./used_tokens/{token}'):
                answer = {'result': 'true'}
            else:
                answer = {'result': 'false'}
        except Exception as e:
            print(e)
            answer = {'result': f'{e}'}

        await self.finish(answer)
