import sys
import time
import subprocess
import os

class SystemCore:
  def __init__(self, version="1.0.0"):
    self.version = version
    self.status = "OFFLINE"

  def boot_sequence(self):
    """Simulates an advanced system startup."""
    print(f"Initalizing System Core Alpha v{self.version}...")
    self.status = "LOADING"

    for task in ["Loading Modules", "Checking Logic Gates", "Finalizing"]:
      print(f"  [WAIT] {task}...")
      time.sleep(0.5)

    self.status = "ONLINE"
    print(f"System is now {self.status}.\n")

  def run_logic_task(self, data_input):
    if not data_input:
      raise ValueError("Data input cannot be empty.")

    # Simulated advanced logic processing
    result = [x * 2 for x in data_input if isinstance(x, int)]
    return {"processed_data": result, "count": len(result)}
  
  def run_hardware_module(self):
    print("Bridge Active: Calling C++ Logic Core...")
    # This runs your compiled C++ program and captures the output
    result = subprocess.run(['./src/core_logic'], capture_output=True, text=True)
    print(result.stdout)

  def run_validation_check(self):
        print("\n--- [BRIDGE] Initializing Kotlin Validator ---")
        base_path = os.path.dirname(os.path.abspath(__file__))
        jar_path = os.path.join(base_path, 'system_validator.jar')
        
        # We use 'java -jar' to execute the compiled Kotlin bytecode
        if os.path.exists(jar_path):
            result = subprocess.run(['java', '-jar', jar_path], capture_output=True, text=True)
            print(result.stdout)
        else:
            print("  [ERROR] system_validator.jar not found. Run the build script first.")

if __name__ == "__main__":
  # Execution block
  core = SystemCore()
  core.boot_sequence()

  sample_data = [10, 20, 30, 40, 50]
  output = core.run_logic_task(sample_data)

  print(f"Results: {output}")
  core.run_hardware_module()
  core.run_validation_check()
