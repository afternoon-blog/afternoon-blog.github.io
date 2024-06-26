# create links in the posts for Stray Birds.

# collect all the files with the pattern *-birds*.markdown in the _posts directory
# for each file, read the content and create a link to the previous and next post at the end of the post.
# write the content back to the file.

import os
import re
import sys
import glob

def get_name(file):
    return os.path.basename(file).split(".")[0]

def get_files():
    files = sorted(glob.glob("../_posts/*-birds*.markdown"))
    return files

files = get_files()
i=0
for file in files:
    # read the lines from the file
    with open(file, "r") as f:
        lines = f.readlines()

    last_line = lines[-1]
    print("last line: ", last_line)
    insert = True
    if last_line.startswith("\[[上一篇]") or last_line.startswith("\[[下一篇]"): 
        insert = False
    print("insert: ", insert)
    if insert:
        link_line = "\n"
    else:
        link_line = ""
    if i>0:
        prev = get_name(files[i-1])
        link_line += "\[[上一篇]({% post_url " + prev + " %})\] "
    if i<len(files)-1:
        next = get_name(files[i+1])
        link_line += "\[[下一篇]({% post_url " + next + " %})\] "
    if insert:
        lines.append(link_line)
    else:
        lines[-1] = link_line
    i += 1

    print(link_line)

    # write the lines back to the file
    with open(file, "w") as f:
        f.writelines(lines)


