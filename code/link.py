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

def get_files(pattern):
    files = sorted(glob.glob(pattern))
    return files

def process(pattern, text, text2):
    files = get_files(pattern)
    i=0
    for file in files:
        # read the lines from the file
        with open(file, "r") as f:
            lines = f.readlines()

        found = False
        j=0
        for line in lines:
            if line.startswith(text):
                link_line = text2
                if i>0:
                    prev = get_name(files[i-1])
                    link_line += "\[[上一篇]({% post_url " + prev + " %})\] "
                if i<len(files)-1:
                    next = get_name(files[i+1])
                    link_line += "\[[下一篇]({% post_url " + next + " %})\] "
                link_line += "\n"
                lines[j] = link_line
                break
            j += 1

        if j==0:
            print(f"No {text} found in {file}")

        i += 1
        # write the lines back to the file
        with open(file, "w") as f:
            f.writelines(lines)


#process("../_posts/*-birds*.markdown", "《飞鸟集》选译: ", "诗歌选译：")
process("../_posts/*-birds*.markdown", "诗歌选译：", "诗歌选译：")
process("../_posts/*.markdown", "《午后》：", "《午后》：")
