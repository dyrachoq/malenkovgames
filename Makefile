install:
	uv sync

VD_games:
	uv run VD_games

build:
	uv build

package-install:
	uv tool install dist/*.whl
lint:
	uv run ruff check VD_games
