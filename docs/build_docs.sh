sphinx-apidoc -f -o docs_src ../mfjet --ext-autodoc -e 
#wait
sphinx-build -b html ./ ./docs #-j 5
