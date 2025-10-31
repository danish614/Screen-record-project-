# screen_recorder_video_fixed.py
import time
import numpy as np
import mss
import cv2
import os

OUTPUT = r"F:\python_project\screen_capture.avi"  
FPS = 20                                         
MONITOR = 1                                    
CODEC = "XVID"                                    
SHOW_PREVIEW = True                               

def main():
    with mss.mss() as sct:
        monitor = sct.monitors[MONITOR]
        width = monitor["width"]
        height = monitor["height"]


        fourcc = cv2.VideoWriter_fourcc(*CODEC)
        out = cv2.VideoWriter(OUTPUT, fourcc, FPS, (width, height))

        print("=" * 60)
        print(f"Recording {width}x{height} @ {FPS} FPS")
        print("Saving to:", os.path.abspath(OUTPUT))
        print("Press 'q' to stop recording.")
        print("=" * 60)

        start = time.time()
        frame_count = 0

        try:
            while True:
                t0 = time.time()
                img = sct.grab(monitor)
                frame = np.array(img)[:, :, :3]  
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                out.write(frame)
                frame_count += 1

                if SHOW_PREVIEW:
                    preview = cv2.resize(frame, (int(width * 0.3), int(height * 0.3)))
                    cv2.imshow("REC PREVIEW - Press Q to stop", preview)
                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        break

                elapsed = time.time() - t0
                sleep = max(0, (1.0 / FPS) - elapsed)
                time.sleep(sleep)

        except KeyboardInterrupt:
            print("Recording stopped by user.")

        finally:
            duration = time.time() - start
            out.release()
            cv2.destroyAllWindows()
            print(f"\nSaved successfully to: {os.path.abspath(OUTPUT)}")
            print(f"Frames recorded: {frame_count}")
            print(f"Duration: {duration:.2f} seconds")
            print(f"Average FPS: {frame_count / duration:.2f}")

if __name__ == "__main__":
    main()
