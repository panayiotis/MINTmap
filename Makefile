.PHONY: format install_hooks lint noteboo spec zip_release

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

zip_release:
	rm -rf dist/* tmp/MINTmap
	poetry build --format wheel
	mkdir -p tmp/MINTmap/dist
	cp -r README.txt ExampleRun tmp/MINTmap
	cp dist/*.whl tmp/MINTmap/dist/
	cd tmp && zip -r ../dist/MINTmap-v3.zip MINTmap
	zipinfo dist/MINTmap-v3.zip
