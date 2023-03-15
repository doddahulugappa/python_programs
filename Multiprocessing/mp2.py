def child_program(child_conn):
    rec = {}
    for i in range(1, 50):
        if i % 10 == 0:
            rec[i] = i**i
            child_conn.send(rec)
        else:
            child_conn.send("")
    child_conn.close()