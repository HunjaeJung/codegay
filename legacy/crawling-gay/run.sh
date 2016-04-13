#!/bin/bash

### bash run.sh
### Beat 크롤링 프로그램을 Autorun 합니다. 자동으로 verticalN*2등분하여 tmux를 split하고, 크롤링을 시작합니다.
verticalN=5
start="0"
end="7318"

file="python3 doori_crawler.py"

cmt="This crawler is going to crawl exhibitors' detail"

###this is going to split the pane into four 
###even horizontal panes
for ((i=1;i<$verticalN;i++)) do
	tmux split-window -v
	tmux select-pane -t $i
done

tmux send-keys -t 1 "clear" C-m
tmux select-layout even-vertical

###this will split each of the four panes
###vertically, resulting in eight seperate panes
for ((i=1;i<$((verticalN*2));i=i+2))
do
	tmux select-pane -t $i
	tmux split-window -h
done

# convert hexadecimal to decimal
jump=$((($end-$start)/(verticalN*2)))
next=$((start+jump))
tmux send-keys -t 1 "clear" C-m

for ((i=1;i<$((verticalN*2));i++))
do
	tmux select-pane -t $i
	# convert decimal to hexadecimal
    start10=$start
    next10=$next
	tmux send-keys -t $i "$file job2 $start10 $next10" C-m
	start=$((start+jump))
	next=$((start+jump))
	sleep 0.5
done

lastPane=$((verticalN*2))
tmux select-pane -t $lastPane
# convert decimal to hexadecimal (end is already hexadecimal)
start10=$start
tmux send-keys -t $lastPane "$file job2 $start10 $end" C-m
