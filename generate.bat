hugo
git add .
git commit -m "generated"
git push origin content
cd docs
git add .
git commit -m "generated"
git push origin master
git push coding master
cd ..