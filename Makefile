.DEFAULT_GOAL:=help

help: ## List available commands
	@grep '^[^#[:space:]].*:' Makefile | sort

install: ## Install project and test dependencies
	@uv sync --extra tests

freeze: ## Show installed dependencies
	@uv pip freeze

format: ## Format code with Ruff
	@uv run ruff format .

lint: ## Lint code with Ruff
	@uv run ruff check .

run: ## Fetch and convert the latest CESSDA vocabularies
	@uv run python main.py

package: ## Build source and wheel distributions
	@rm -rf dist
	@uvx --from build pyproject-build

package-check: ## Validate built distributions with Twine
	@uvx --from twine twine check dist/*

clean: ## Remove build artifacts
	@rm -rf dist build .pytest_cache *.egg-info

test: ## Run packaging checks, linters, and pytest suite
	@uv run ./run-tests.sh
