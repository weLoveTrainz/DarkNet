import subprocess
import time

start = time.time()
file_list = ["File_1.jpeg", "File_2.jpeg", "File_3.jpeg", "File_4.jpeg", "File_5.jpeg", "File_6.jpeg"]
carriage_occupancy = []

init_args = ["./darknet", "detect", "cfg/yolov3-tiny.cfg", "yolov3-tiny.weights"]

child_process = subprocess.Popen(init_args, stdin = subprocess.PIPE, stdout = subprocess.PIPE)


for i in file_list:
    child_process = subprocess.Popen(init_args, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
    child_process_output = child_process.communicate(b"data/" + str.encode(i))[0]
    carriage_occupancy.append(str(child_process_output).count("person"))

end = time.time()
print(carriage_occupancy)
print(end-start)
