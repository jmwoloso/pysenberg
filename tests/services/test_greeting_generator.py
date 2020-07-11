import pytest
from src.greeting_service.services import GreetingGenerator


@pytest.fixture
def service():
    service = GreetingGenerator()
    return service


class TestSayHelloWorld(object):

    @pytest.mark.parametrize(
        "target", ['world', 'you'])
    def should_log_various_greetings(self, capsys, service, target):
        service.say_hello_world(target)
        captured = capsys.readouterr()
        assert captured.out == f'Hello {target}!\n'
