outer_loop_counter = 1
while outer_loop_counter <= 3:
    print(f"Outer loop iteration: {outer_loop_counter}")

    inner_loop_counter = 1
    while inner_loop_counter <= 2:
        print(f"Inner loop iteration: {inner_loop_counter}")
        inner_loop_counter += 1

    outer_loop_counter += 1