import pytest
import calculator

def test_add():
    assert calculator.calculate(2, 3, "add") == 5

# Add more functional tests for subtract, multiply, and divide
def test_subtract():
    assert calculator.calculate(10, 4, "subtract") == 6

def test_multiply():
    assert calculator.calculate(3, 4, "multiply") == 12

def test_divide():
    assert calculator.calculate(10, 2, "divide") == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.calculate(10, 0, "divide")

def test_terminal_output(capsys):
    calculator.calculate(10, 2, "multiply")
    captured = capsys.readouterr()
    assert captured.out == "Result: 20\n"

def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0

# Add more tests to cover edge cases and negative scenarios
def test_unknown_operation():
    assert calculator.calculate(5, 5, "modulo") == 0


def test_terminal_output_divide_by_zero(capsys):
    with pytest.raises(ValueError):
        calculator.calculate(5, 0, "divide")
    captured = capsys.readouterr()
    assert captured.out == ""
