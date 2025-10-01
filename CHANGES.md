# Changes

Version 2.0.0

- **BREAKING**: Migrate from Pipfile to pyproject.toml and uv package manager
- Update CI workflows to use the latest GitHub Actions and uv
- Replace Pipenv with uv for dependency management
- Add Ruff as the new linter replacing previous linting tools
- Fix UserWarning about deprecated pkg_resources usage
- Update Makefile commands to use uv instead of pipenv
- Remove .editorconfig, Pipfile, Pipfile.lock, and setup.cfg
- Consolidate all project configuration into pyproject.toml
- Fix failing tests and improve test reliability
- Add uv.lock for deterministic dependency resolution

Version 1.1.2

- Add github actions for publishing to pypi
- Add github actions for testing
- add test badge to readme
- Remove requirements.txt

Version 1.1.0

- update readme
- fix version number

Version 1.1.0

- Introduce Auto fetch new versions for all vocabularies
- Bump update dependencies to their latest versions
- Introduce debugging option to 'make run' command
- Refactor convert functionality and add sorting
- Update CESSDA vocabularies to 2024-02-01
- Add error handling to data fetching
- Bump requirements.txt

Version 1.0.0

- Initial public release 2022.11.03
