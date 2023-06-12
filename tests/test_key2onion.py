from key2onion import onion_address_v3, onion_address_v2

def test_v3(tmp_path):
	priv_key = ("-----BEGIN PRIVATE KEY-----\n"
				"MC4CAQAwBQYDK2VwBCIEIFKL9sm9nefA8WlUmWK3KnPjlPdTSVjOzqhmC2xV9VVF\n"
				"-----END PRIVATE KEY-----")
	p = tmp_path / "ed25519.priv"
	p.write_text(priv_key)
	addr = onion_address_v3(p)
	assert addr == b"q6jfbqd6pqddrsmkwq6xwakxfzfpelmxx3jgzzojhlmrkamo5ln6twad"

def test_v2(tmp_path):
	priv_key = ("-----BEGIN RSA PRIVATE KEY-----\n"
				"MIICXQIBAAKBgQC/3ancqN/SRYOEMKsgbIULDwTq543T6RQpWXKSFM5ako034fkE\n"
				"/TcyLNk6oUt+QauRXOVTokuC2iLuk65vlLYC+UcSSmGxjbg2uCNyRAGM2idMkhuu\n"
				"Nfr4ieDRKIzUh53DcTQEQpXF3A4nnZWHTYPKDgw6bNsOYCYGVkNSspv0NwIEAQAA\n"
				"AwKBgFtM7ZcySlDyRytYiQXWJPTKM2geCjCZqpdEDif6l5/O6n8t340+SKEcsEno\n"
				"FEO9XrM3xDSxJLlEAWko2atbHwKCMnbnsWf3Bb9Y46AeqNycd3qk2tClrX8pfpqx\n"
				"Kf3+nXaw+YkSPTEexDOvOyam4C1C89AjF3+hAaWYcNepfPt7AkEA6jT6gLcXyk+W\n"
				"muwxgyd59b/veFOF4pgR+OH5zmOD6/hVL36BP/pGiBGU3A7BU4UOMgxG8g2QA8E0\n"
				"l2EhHM92wwJBANG4FRCX9TYVvy7JoDdAGhrUS6PZcOqcSckzy7uF9MkDTLazJte1\n"
				"imWyqfyK0HkMKMcwbiBHi5nYFuTV0u7LvX0CQHyqthfSJ8aR8KP/Oj4FqUt1YEXh\n"
				"rvc/v3E+AZltOiVh+OCvg18saBM+FzWnv9CT5WQeuoXrTgnXiqAW7z0nINkCQF/1\n"
				"+OhpPp8QUuTq5vnu8GuNYf5Zlep6kNSTDCTCsVBPi/jAZd5udfdmXqslt4Wp7kQv\n"
				"LSt4z+ISzc8TbXrZ+WMCQQCUGJf/zn6lzzru9jBWxjPzfUkUnWSh6dYlkruKzOJ8\n"
				"G9SygLMEnE/C9GsYfpMnBp0NPf+Gk3a1IHIy/NhETlW1\n"
				"-----END RSA PRIVATE KEY-----")
	p = tmp_path / "rsa.priv"
	p.write_text(priv_key)
	addr = onion_address_v2(p)
	assert addr == b"a6w2bp7sz5wzvp52"