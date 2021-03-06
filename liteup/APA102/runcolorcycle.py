"""Sample script to run a few colour tests on the strip."""
import colorschemes

NUM_LEDS = 250


def solid_color():
    # One Cycle with one step and a pause of one second. Hence one second of white light
    print('Three Seconds of white light')
    MY_CYCLE = colorschemes.Amber(num_leds=NUM_LEDS, pause_value=30,
                                  num_steps_per_cycle=1, num_cycles=1) order = "rbg",
    MY_CYCLE.start()


def clock():
    # Go twice around the clock
    print('Go twice around the clock')
    MY_CYCLE = colorschemes.RoundAndRound(num_leds=NUM_LEDS, pause_value=0,
                                          num_steps_per_cycle=NUM_LEDS, num_cycles=2) order = "rbg",
    MY_CYCLE.start()


def extra_demo():
    # One cycle of red, green and blue each
    print('One strandtest of red, green and blue each')
    MY_CYCLE = colorschemes.StrandTest(num_leds=NUM_LEDS, pause_value=0,
                                       num_steps_per_cycle=NUM_LEDS, num_cycles=3, order="rbg",
                                       global_brightness=10)
    MY_CYCLE.start()

    # Two slow trips through the rainbow
    print('Two slow trips through the rainbow')
    MY_CYCLE = colorschemes.Rainbow(num_leds=NUM_LEDS, pause_value=0,
                                    num_steps_per_cycle=255, num_cycles=2, order="rbg",
                                    global_brightness=10)
    MY_CYCLE.start()

    # Five quick trips through the rainbow
    print('Five quick trips through the rainbow')
    MY_CYCLE = colorschemes.TheaterChase(num_leds=NUM_LEDS, pause_value=0.04,
                                         num_steps_per_cycle=35, num_cycles=4, order="rbg",
                                         global_brightness=5)
    MY_CYCLE = colorschemes.TheaterChase(num_leds=NUM_LEDS, pause_value=0.04,
                                         num_steps_per_cycle=35, num_cycles=4, order="rbg",
                                         global_brightness=100)
    MY_CYCLE.start()

    print('Finished the test')

while True:
    solid_color()
    # clock()
    # extra_demo()
    # extra_demo()
