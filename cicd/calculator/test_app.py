import pytest

from app import calculator

def test_add(monkeypatch, capsys):
    inputs = iter(["2 + 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    calculator()
    captured = capsys.readouterr()
    assert "= 5.0" in captured.out

def test_invalid_input(monkeypatch, capsys):
    inputs = iter(["2++3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    calculator()
    captured = capsys.readouterr()
    assert "❌ Invalid input format" in captured.out
