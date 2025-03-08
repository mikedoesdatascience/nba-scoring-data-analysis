lock:
	@uv lock

sync:
	@uv sync --extra dev

lock-sync: lock sync