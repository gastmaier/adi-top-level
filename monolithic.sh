mkdir -p repos
cd repos

if [[ ! -d hdl ]]
then
	git clone git@github.com:analogdevicesinc/hdl.git
else
	(cd hdl ; git pull)
fi

cd ..
if [[ -d docs-mono ]]
then
	rm -rf docs-mono
fi

mkdir docs-mono
cd docs-mono
cp -r ../docs/* .
# Convert external references into local
find . -type f -exec sed -i "s|ref:\`hdl:|ref:\`|g" {} \;
find . -type f -exec sed -i "s|<hdl:|<|g" {} \;
cat general-information/docs_guidelines.rst

mkdir hdl
cp -r ../repos/hdl/docs/index.rst hdl
cp -r ../repos/hdl/docs/projects hdl
cp -r ../repos/hdl/docs/user_guide hdl
cp -r ../repos/hdl/docs/library hdl
cp -r ../repos/hdl/docs/regmap hdl
mkdir hdl/sources
cp ../repos/hdl/docs/sources/HDL_logo.svg hdl/sources

#(cd repos/hdl/library; make all)

make html
