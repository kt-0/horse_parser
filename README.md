## Setting up the folder, git repo, and virtualenv from terminal:

### navigate to where ever you'd like the repo to live Documents, Desktop, etc
```
cd ~/Desktop
```

### clone the repo:
```
git clone https://github.com/kt-0/horse_parser
```

### set up the virtual env:
```
pip install virtualenv
pip3 install virtualenv
virtualenv -p python3 env
```

### download chromedriver and move it to our repo folder:
[chromedriver download link](http://chromedriver.chromium.org/downloads)

```
mv ../Downloads/chromedriver /Desktop/horse_parser/
```
### activating the virtualenv:
```
source env/bin/activate
```
### installing selenium in the virtualenv:
```
pip install selenium
```
### starting the python shell:
```
python
```

Open page_scraper.py in any editor(i use Atom) and copy/paste lines one at a time into the python shell -- this is necessary until certain issues are resolved (captchas)
