from imports import *

# --------------------
# Management commands
# --------------------

@command('print_hello')
class HelloCommand(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Hello, Django!')


@command()
def print_hello_func(cmd, **options):
    cmd.stdout.write('Hello from function-based command!')
