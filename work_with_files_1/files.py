#ff = open("work_with_files/file.txt", "a")
#ff.write("hello world\n")
#ff.close()

# reset and write
#ff = open("work_with_files/file1.txt", "w")
#ff.write("hi boiii")
#ff.close

rf = open("work_with_files/file.txt", "r")
text_output = rf.read()
rf.close()

print(text_output)