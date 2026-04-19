import pytest
from src.engine import SystemCore

def test_system_boot():
    """Verify the system initalizes with the correct status."""
    core = SystemCore()
    assert core.status == "OFFLINE"
    core.boot_sequence()
    assert core.status == "ONLINE"

def test_logic_processing():
    """Ensure the math logic correctly doubles integer inputs."""
    core = SystemCore()
    input_data = [1, 5, 10]
    result = core.run_logic_task(input_data)

    assert result["processed_data"] == [2, 10, 20]
    assert result["count"] == 3

def test_invalid_input():
    """Test that the system handles empty inputs correctly."""
    core = SystemCore()
    with pytest.raises(ValueError):
        core.run_logic_task([])
