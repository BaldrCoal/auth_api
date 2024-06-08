from handlers.generate_token import GenerateToken
from handlers.link_token import LinkToken
from handlers.valid_check import ValidCheck
from handlers.check_link import CheckLink

urls = [
    (r'/generate_token', GenerateToken,),
    (r'/link_token', LinkToken,),
    (r'/valid_check', ValidCheck,),
    (r'/check_link', CheckLink,),
]
