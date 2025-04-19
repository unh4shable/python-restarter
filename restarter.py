import time, os
import subprocess, signal

def restart_script():
    while True:
        try:
            process = subprocess.Popen(["python", "main.py"])
            start_time = time.time()

            while True:
                if process.poll() is not None:
                    break

                elapsed_time = time.time() - start_time
                if elapsed_time > 30 * 60:
                    process.terminate()
                    try:
                        process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        process.kill()
                    break

                time.sleep(1)

        except Exception as e:
            print(f"Error running | {e}")

if __name__ == "__main__":
    restart_script()