find . -type f -printf '%f\n' -name '*\.sh' | sed -r 's/\.sh//g'
