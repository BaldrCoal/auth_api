import sys
import os

import asyncio
import logging
import tornado.web
import tornado.platform.asyncio
import tornado.log
from tornado.options import define, options, parse_config_file
from tornado.ioloop import IOLoop
import urls

define("port", type=int)
define("debug", type=str)
define("filestore", type=str)

parse_config_file("application.conf")
tornado.options.parse_command_line()


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)


if __name__ == '__main__':
    tornado.log.enable_pretty_logging()

    logging_mode = logging.DEBUG if options.debug == 'yes' else logging.INFO
    tornado.log.app_log.setLevel(logging_mode)

    tornado.platform.asyncio.AsyncIOMainLoop().install()

    application = Application(
        urls.urls,
        template_path='./templates',
        debug=(True if options.debug == "yes" else False))

    application.listen(options.port)
    print('server started on port {}'.format(options.port))
    asyncio.get_event_loop().run_forever()
