import time
import numpy as np

def hourglassSum_numpy(arr):
    hourglass = np.zeros([4,4])
    i_a, i_b = 0, 3
    for i in range(hourglass.shape[0]):
        j_a, j_b = 0, 3
        for j in range(hourglass.shape[1]):
            glass = arr[i_a:i_b, j_a:j_b]
            hourglass[i][j] = np.sum(glass) - (glass[1][0]+glass[1][2])
            j_a += 1
            j_b +=1
        i_a +=1
        i_b +=1
    return hourglass.flatten()[np.argmax(hourglass)]


def hourglassSum_list(arr):
    results = []
    i_a, i_b = 0, 3
    for i in range(4):
        j_a, j_b = 0, 3
        for j in range(4):
            result = sum(arr[i][j_a:j_b])
            result += arr[i+1][j_a+1]
            result += sum(arr[i+2][j_a:j_b])
            results.append(result)
            j_a += 1
            j_b +=1
        i_a +=1
        i_b +=1
    return max(results)


arr_a_numpy = np.array(
    [
        [-9, -9, -9, 1, 1, 1],
        [0, -9,  0,  4, 3, 2],
        [-9, -9, -9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ])

arr_a_list = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0]
    ]

arr_b_list = [
    [1, 1, 1, 0, 0, 0],
    [0 ,1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
    ]

# run pytest -rP
def test_hourglass():
    start = time.time()
    result_a_numpy = hourglassSum_numpy(arr_a_numpy)
    end = time.time()
    time_numpy = end-start

    start = time.time()
    result_a_list = hourglassSum_list(arr_a_list)
    end = time.time()
    time_list = end-start

    result_b_list = hourglassSum_list(arr_b_list)

    print(f"Hourglass challenge: Time in seconds with numpy {time_numpy}. Time in seconds with list {time_list}")
    assert result_a_numpy == 28
    assert result_a_list == 28
    assert result_b_list == 19

# %%

# %%