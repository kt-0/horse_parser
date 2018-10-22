cd ~/Desktop && mkdir selenium_test
cd selenium_test
pip install virtualenv
pip3 install virtualenv
virtualenv -p python3 env
# download http://chromedriver.chromium.org/downloads
mv ../Downloads/chromedriver /Desktop/selenium_test/

source env/bin/activate #activating the virtualenv
pip install selenium
python #python shell
