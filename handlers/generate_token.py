import os
import uuid

from handlers.base_handler import BaseHandler


class GenerateToken(BaseHandler):
    async def get(self):
        self.set_header('Content-Type', 'application/json')
        print('generate token')
        token = str(uuid.uuid4())
        try:
            os.mkdir(f'./non_used_tokens/{token}')
            with open(f'./non_used_tokens/{token}/token.txt', 'w') as file:
                file.write(token)
            answer = {'result': f'{token}'}
        except Exception as e:
            print(e)
            answer = {'result': f'{e}'}

        await self.finish(answer)
