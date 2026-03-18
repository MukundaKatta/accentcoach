"""Tests for Accentcoach."""
from src.core import Accentcoach
def test_init(): assert Accentcoach().get_stats()["ops"] == 0
def test_op(): c = Accentcoach(); c.learn(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = Accentcoach(); [c.learn() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = Accentcoach(); c.learn(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = Accentcoach(); r = c.learn(); assert r["service"] == "accentcoach"
