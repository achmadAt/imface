cd ..

echo "deleting existing release related files"
rm -rf dist/*
rm -rf build/*

echo "creating a package for current release - pypi compatible"
python setup.py sdist

echo "pushing the release to pypi"
twine upload dist/*