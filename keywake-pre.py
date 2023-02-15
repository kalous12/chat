from precise_runner import PreciseEngine, PreciseRunner




engine = PreciseEngine('precise-engine/precise-engine', 'athena.pb')
runner = PreciseRunner(engine, on_activation=lambda: print('hello'))
print('good morning ')
runner.start()

# Sleep forever
from time import sleep
while True:
    sleep(10)