import time


def ft_progress(lst: list) -> int:
	start_time = time.time()
	time_expected = 0
	bar_len = 24
	for elem in lst:
		percent = elem / len(lst)
		bars = '=' * int(round(percent * bar_len) - 1)
		bars += '>' + ' ' * (bar_len - len(bars) - 1)

		current_time = time.time()
		time_passed = current_time - start_time
		time_expected = time_passed / (percent + 0.001) - time_passed

		if percent >= 0.99:
			bars = '=' * bar_len
			time_expected = 0

		print(f'\rETA: {time_expected:5.2f}s [{int(round(percent * 100)):3d}%][{bars}] | elapsed time {time_passed:.2f}s', end = '')
		yield elem


listy = range(3333)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	time.sleep(0.005)
print()
print(ret)
