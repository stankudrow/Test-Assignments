#!/usr/bin/env bash


# >>> This script was made, test and run in Ubuntu 18.04. <<< #
# >>> The descriptions for tasks are copied as they were. <<< # 
 

# Stage 1

printf "Stage 1 in process.\n\n"

## S1, Task 1. How to see if the environment variable ORACLE_HOME is set up and what value it has?

# Note!
# I have no ORACLE_HOME in environment and I didn't write it in .profile or /etc/environment files.
# That is why it is exported here for demonstration purpose
export ORACLE_HOME="Oracle Home Variable"; echo -e "S1T1: $(printenv | grep 'ORACLE_HOME')\n"


## S1, Task2. Set up environment variable TEST_VAR with value "test"

export TEST_HOME="test"; echo -e "S1T2: $(printenv | grep 'TEST_HOME')\n"


## S1, Task3. Name console tools in Linux which could be used for monitoring.

printf "S1T3 -> Some monitoring commands:\n"

printf "top htop iohtop and its variances to monitor statistics on real-time processes.\n"

printf "vmstat - memory statistics (-s)\n"
#vmstat -s | head -5
printf "vmstat - disks statistics (-d)\n"
#vmstat -d | tail -5

printf "netstat - network statistics, however it is considered obsolete.\n"
printf "A proposed replacement for netstat is 'ss' command.\n"
printf "Other commands for netstat options:\n"
printf "netstat -i = ip -s link\n"
printf "netstat -g = ip maddr\n"
printf "netstat -r = ip route\n\n"


## S1, Task 4. Check processes started by user "user"

printf "S1T4 - User processes.\n"
printf "way1: ps -u $USER [the output is not shown here]\n"
printf "way2: top -u $USER [the output is not shown here].\n\n"  # pager, skipped 


# Stage 2

printf "Stage 2 in progress.\n\n"

# Directory "./example/" contains big amount of files of different types.
# 1. Show all files ending on ".sh". The list should be sort by date of the last modification.
# 2. Change permission of all ".sh" files, so that they could be executed by the owner of the file.
# 3. Print all ".cfg" files 
# 4. Show last 25 lines of file "./example/test.log"
# 5. Show the first 25 lines of file "./example/test.log"
# 6. Show line number 25.
# 7. Move all files which have the pattern "trash" in the filename to /tmp/ directory
# 8. Copy all files which have the pattern "trash" in the filename to /tmp/ directory

# S2, preparations

edir="./example/"  # "example" test directory, note last backslash /
tdir="./temp/"  # this directory is instead of /tmp/ for tasks 7 and 8 of this section
elogf="${edir}test.log"  # test.log file being supposed to have content

# if there is no directories, let's make them
for dir in ${edir} ${tdir}
do
    if [ ! -d ${dir} ]
    then
        mkdir ${dir}
    fi
done

# some of the files can be removed from example directory
# so a little restauration may be needed
for fname in {1..9}.txt {a..k}.sh {L..Z}.cfg {w..z}_trash_{2..5}.{dat,txt,sh,cfg}
do
    efile=${edir}${fname}
    if [ ! -e ${efile} ]
    then
        touch ${efile}
    fi
done

if [ -e ${elogf} ]  # with example directory in its value
then
    for i in {1..10000}
    do
        echo "Line ${i} Ligne ${i} Línea ${i}" >> ${elogf}
    done
fi

touch ${edir}{f1,g2,h3}.sh.{zsh,log}

printf "Stage 2 preparations are over.\n\n"


# S2, Task 1
printf "S2T1:\n$(ls -t ${edir} | grep "\.sh$")\n\n"

# S2, Task 2 - just make files executable
for shfile in $(ls ${edir} -t | grep ".sh")
do
    chmod +x ${edir}${shfile}
done
printf "S2T2:\n$(ls ${edir} -ahl)\n\n"

# S2, Task3
printf "S2T3:\n$(ls ${edir} -t | grep '.cfg')\n\n"

# S2, Task 4
printf "S2T4:\n$(tail ${elogf} -n 25)\n\n"

# S2, Task 5
printf "S2T5:\n$(head ${elogf} -n 25)\n\n"

# S2, Task 6
printf "S2T6:\n$(head ${elogf} -n 25 | tail -n 1)\n\n"

# S2, Tasks 7 and 8

printf "Stage 2, tasks 7 and 8.\n"
printf "A chosen way is just to use \`mv\` command, and for copying - \`cp\`.\n"
printf "The moved files are restored when the script is run.\n\n"

for file in $(ls ${edir} | grep trash)
do
    mv ${edir}${file} ${tdir}
done

printf "Stage 2 tasks are over.\n\n"


# Stage III - Optional

printf "Stage 3 in effect.\n\n"

# Directory "./example/" contains a big amount of files of different types and sub-directories with files of different types.
# 1. Find all files in the directory "./example/" (and all sub-directories) which contains text "test_mark". Print only filenames
# 2. Find all files in directory "./example/" (and all sub-directories) ending with ".log", which were modified in the last 2 days and have size >10 MB
# 3. You have file "./example/test.log" which have size > 3GB. What is the fastest way to clean the file content without deleting and recreating the file.
# 4. Find all files in directory "./example/" (and all sub-directories) ending with ".log", which are older than 30 days, zip them with the replacement of source files.


# Preparations

esdir=${edir}"esubdir/"
if [ ! -d ${esdir} ]; then mkdir ${esdir}; fi
for file in ${edir}{a..c}test_mark{1..4}; do if [ ! -e ${file} ]; then touch ${file}; fi; done
for file in ${esdir}{5..8}test_mark{d..f}.{log,test}; do if [ ! -e ${file} ]; then touch ${file}; fi; done

tsdir=${tdir}"tsubdir/"
if test ! -d ${tsdir}; then mkdir ${tsdir}; fi
for file in ${tsdir}{just.in,time.to,tesk_mark_mark.test}; do if [ ! -e ${file} ]; then touch ${file}; fi; done

# create a file with random content more than 10 MB
# two of them -> just provide the size to the function -> would be nice
# it should be test.log -> {elogf}

# S3, Task 1

printf "S3T1\n"
find ${edir} -type f -name "*test_mark*" -printf "%f\n"
printf "\n"

# S3, Task 2
printf "S3T2\n"
find ${edir} -type f -name "*.log" -mtime -2 -ls -size +10M
printf "\n"

# S3, Task 3 - no need were in checking size.
printf "S3T3\n"
truncate ${elogf} -s 0 
printf "File truncated.\n\n"

# S3, T4
printf "S3T4\n"
find ${edir} -name "*.log" -mtime +30 -exec zip ./arch.zip {} \; -exec rm {} \;
printf ".log files older than 30 days are compressed to arch.zip with replacement.\n\n"

printf "The task is over.\n"
