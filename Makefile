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

brain-even:
	uv run brain-even

brian-calc:
	uv run brain-calc

lint:
	uv run ruff check brain_games

