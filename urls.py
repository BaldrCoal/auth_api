from handlers.generate_key import GenerateKey
from handlers.link_key import LinkKey
from handlers.valid_check import ValidCheck

urls = [
    (r'/generate_key', GenerateKey,),
    (r'/link_key', LinkKey,),
    (r'/valid_check', ValidCheck,),
]
