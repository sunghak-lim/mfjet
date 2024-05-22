sphinx-apidoc -f -o doc_src ../mfjet/ --ext-autodoc -e &
wait
sphinx-build -b html ./ ../doc #-j 5
