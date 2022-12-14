from sway.checks import CheckStates
from sway.config import Config


def test_check_command(config: Config) -> None:
    assert config.get_check_by_name(name="multiple_words_command").command == [
        "echo",
        "hello",
    ]


def test_check_state_positive(config: Config) -> None:
    assert (
        config.get_check_by_name(name="functional_service").state
        == CheckStates.POSITIVE
    )


def test_check_state_negative(config: Config) -> None:
    assert (
        config.get_check_by_name(name="broken_service").state
        == CheckStates.NEGATIVE
    )
