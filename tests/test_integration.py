"""Integration tests for Accentcoach."""
from src.core import Accentcoach

class TestAccentcoach:
    def setup_method(self):
        self.c = Accentcoach()
    def test_10_ops(self):
        for i in range(10): self.c.learn(i=i)
        assert self.c.get_stats()["ops"] == 10
    def test_service_name(self):
        assert self.c.learn()["service"] == "accentcoach"
    def test_different_inputs(self):
        self.c.learn(type="a"); self.c.learn(type="b")
        assert self.c.get_stats()["ops"] == 2
    def test_config(self):
        c = Accentcoach(config={"debug": True})
        assert c.config["debug"] is True
    def test_empty_call(self):
        assert self.c.learn()["ok"] is True
    def test_large_batch(self):
        for _ in range(100): self.c.learn()
        assert self.c.get_stats()["ops"] == 100
