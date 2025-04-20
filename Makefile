build:
	uv build

install:
	uv sync

package-install:
	uv tool install dist/*.whl

package-uninstall:
	uv tool uninstall hexlet-code

brain-games:
	uv run brain-games

