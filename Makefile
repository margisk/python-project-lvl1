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

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-prime:
	uv run brain-prime

lint:
	uv run ruff check brain_games

