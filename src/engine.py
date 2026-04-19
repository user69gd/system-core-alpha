import logging
import os
import subprocess
import datetime

# 1. Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("system.log"),
        logging.StreamHandler()
    ]
)

class SystemCore:
    def __init__(self):
        # Satisfies: assert core.status == "OFFLINE"
        self.status = "OFFLINE"
        logging.info("--- System Core Alpha v1.0.0 Initializing ---")

    def boot_sequence(self):
        """ Satisfies: core.boot_sequence() in test_system_boot """
        logging.info("Executing Boot Sequence...")
        self.status = "ONLINE"
        logging.info(f"System status updated: {self.status}")

    def run_logic_task(self, data):
        """ Satisfies: test_logic_processing expectations (Dictionary + Count) """
        if not data:
            logging.error("Logic Task Error: Received empty dataset.")
            raise ValueError("Input data cannot be empty")
        
        logging.info(f"Executing Logic Task on {len(data)} items...")
        processed_list = [x * 2 for x in data]
        
        # FIX: Added "count" key to satisfy: assert result["count"] == 3
        result = {
            "processed_data": processed_list,
            "count": len(data)
        }
        
        logging.info(f"Logic Task Complete. Result Summary: {result}")
        return result

    def run_hardware_module(self):
        """ Execution bridge for the C++ Core Logic """
        logging.info("Bridge Active: Calling C++ Logic Core...")
        base_path = os.path.dirname(os.path.abspath(__file__))
        cpp_executable = os.path.join(base_path, 'core_logic')
        
        try:
            if not os.path.exists(cpp_executable):
                logging.error(f"Binary missing: {cpp_executable}")
                return

            result = subprocess.run([cpp_executable], capture_output=True, text=True, check=True)
            logging.info(f"C++ Output:\n{result.stdout.strip()}")
        except Exception as e:
            logging.error(f"C++ Bridge Error: {e}")

    def run_validation_check(self):
        """ Execution bridge for the Kotlin Validator """
        logging.info("Bridge Active: Initializing Kotlin Validator...")
        base_path = os.path.dirname(os.path.abspath(__file__))
        jar_path = os.path.join(base_path, 'system_validator.jar')
        
        try:
            if not os.path.exists(jar_path):
                logging.warning("Kotlin JAR missing.")
                return

            result = subprocess.run(['java', '-jar', jar_path], capture_output=True, text=True, check=True)
            logging.info(f"Kotlin Results:\n{result.stdout.strip()}")
        except Exception as e:
            logging.warning(f"Kotlin Error: {e}")

if __name__ == "__main__":
    core = SystemCore()
    
    # Standard operational flow
    core.boot_sequence()
    
    sample_data = [10, 20, 30]
    core.run_logic_task(sample_data)
    core.run_hardware_module()
    core.run_validation_check()
    
    logging.info("All Polyglot Modules finalized.")