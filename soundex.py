def soundex_prepare(s):
	"""Prepare string for Soundex encoding.

	Remove non-alpha characters (and the not-of-interest W/H/Y),
	convert to upper case, and remove all runs of repeated letters."""
	p = re.compile("[^a-gi-vxz]", re.IGNORECASE)
	s = re.sub(p, "", s).upper()
	for c in set(s):
		s = re.sub(c + "{2,}", c, s)
	return s

def soundex_encode(s):
	"""Encode a name string using the Soundex algorithm."""
	result = s[0].upper()
	s = soundex_prepare(s[1:])
	letters = 'ABCDEFGIJKLMNOPQRSTUVXZ'
	codes   = '.123.12.22455.12623.122'
	d = dict(zip(letters, codes))
	prev_code=""
	for c in s:
		code = d[c]
		if code != "." and code != prev_code:
			result += code
	 if len(result) >= 4: break
		prev_code = code
	return (result + "0000")[:4]