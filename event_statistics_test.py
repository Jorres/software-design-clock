import event_statistics as ES
import mocked_clock as MC

MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60
EPS = 10 ** -6


def compare_doubles_with_eps(a, b):
    return abs(a - b) < EPS


def test_return_empty_statistics_with_no_events():
    statistics = ES.EventStatistics(MC.MockedClock())
    assert len(statistics.getAllEventStatistic()) == 0


def test_return_zero_on_new_event():
    statistics = ES.EventStatistics(MC.MockedClock())
    statistics.incEvent("first")
    assert compare_doubles_with_eps(
        statistics.getEventStatisticByName("second"), 0)


def test_return_one_rpm_for_one_new_event():
    statistics = ES.EventStatistics(MC.MockedClock())
    statistics.incEvent("first")
    assert compare_doubles_with_eps(
        statistics.getEventStatisticByName("first"), 1 / MINUTES_IN_HOUR)


def test_event_expires_after_one_hour():
    clock = MC.MockedClock()
    statistics = ES.EventStatistics(clock)
    statistics.incEvent("first")
    clock.add_seconds(MINUTES_IN_HOUR * SECONDS_IN_MINUTE + 1)

    assert compare_doubles_with_eps(
        statistics.getEventStatisticByName("first"), 0)


def test_return_all_statistics():
    statistics = ES.EventStatistics(MC.MockedClock())
    statistics.incEvent("first")
    statistics.incEvent("second")
    result = statistics.getAllEventStatistic()
    assert compare_doubles_with_eps(
        statistics.getEventStatisticByName("second"), 1 / MINUTES_IN_HOUR)

    for name, rpm in result:
        assert name == "first" or name == "second"
        assert compare_doubles_with_eps(rpm, 1 / MINUTES_IN_HOUR)
