.PHONY: format install_hooks lint noteboo spec

format:
	poetry run yapf --in-place --recursive --parallel \
	  --verbose .

install_hooks:
	@for f in $(shell ls config/hooks); do \
	  echo ln -f -s ../../config/hooks/$${f} .git/hooks/$${f}; \
	  ln -f -s ../../config/hooks/$${f} .git/hooks/$${f}; \
	  done

lint:
	poetry run flake8
	find . -name '*.yaml' | xargs --no-run-if-empty poetry run yamllint 

notebook:
	poetry run jupyter contrib nbextension install --user
	poetry run jupyter nbextension enable execute_time/ExecuteTime
	poetry run jupyter notebook

spec:
	poetry run mamba --format=documentation --enable-coverage
