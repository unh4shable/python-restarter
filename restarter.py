import subprocess, time

def restart_script():
    while True:
        start_time = time.time()
        try:
            process = subprocess.Popen(["python", "main.py"])

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

        total_elapsed = time.time() - start_time
        if total_elapsed < 30 * 60:
            time.sleep(30 * 60 - total_elapsed)

if __name__ == "__main__":
    restart_script()
