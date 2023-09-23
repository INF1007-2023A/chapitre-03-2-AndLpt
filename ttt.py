def format_base(value, base, letters):
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		digit_value = abs_value % base
		result += letters[digit_value]
		abs_value //= base
	if value < 0:
		result += "-"
	return result[::-1]