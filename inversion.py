def read_text(file_name):
    with open(file_name, 'r') as f:
        content = f.readlines()
    elements = [int(line.strip()) for line in content]
    return elements


def merge(left, right):
    count = 0
    left_index, right_index, merged_list = 0, 0, []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1
            count += len(left) - left_index
    merged_list += left[left_index:]
    merged_list += right[right_index:]
    return merged_list, count


def merge_sort(elements):
    if len(elements) <= 1:
        return elements, 0
    left = elements[:int(len(elements)/2)]
    right = elements[int(len(elements)/2):]
    left, a = merge_sort(left)
    right, b = merge_sort(right)
    result, c = merge(left, right)
    return result, (a + b + c)


def count_inversion():
    return merge_sort(read_text('inversions.txt'))


if __name__ == '__main__':
    sorted_list, number_inversions = count_inversion()
    print(number_inversions, sorted_list)
