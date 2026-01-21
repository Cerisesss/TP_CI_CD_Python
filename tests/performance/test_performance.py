from app.utils import doThing, GLOBAL

def setup():
    GLOBAL["users"].clear()

def test_doThing_performance(benchmark):
    def run():
        doThing("perf", 1,2,3,4,5,6,7,8,9)

    benchmark(run)
