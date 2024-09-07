import sys

randomlist=['a',0,2]
for entry in randomlist:
    try:
        print("thr entry is ",entry)
        r=1/int(entry)
        break
    except:
        print("oops!",sys.exc_info()[0],"occurred:")
        print("next entry.")
        print()
        print("the reciprocal of ",entry,"is",r)