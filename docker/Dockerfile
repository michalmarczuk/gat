FROM python:3.6

# Source folder has to be mounted under: /usr/src/gat when running this container

ENV PYTHONPATH /usr/src/gat

# Install requirements
RUN mkdir -p /usr/src/gat_tests_requirements
COPY requirements.txt /usr/src/gat_tests_requirements
RUN pip install -r /usr/src/gat_tests_requirements/requirements.txt
RUN rm -rf /usr/src/gat_tests_requirements

WORKDIR /usr/src/gat/tests

COPY cleanup_cache.sh /usr/src/

# Update package lists and install basic stuff
RUN apt-get -qq update
RUN apt-get -qq install wget unzip gstreamer1.0-libav

# Install Google Chrome
RUN wget --quiet https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get -qq install libgconf-2-4 libnspr4 libnss3 libxss1 libpango1.0-0
RUN apt-get -qq install fonts-liberation libappindicator3-1 libatk-bridge2.0-0 libgtk-3-0 xdg-utils lsb-release
RUN dpkg -i google-chrome-stable_current_amd64.deb

# Install chromedriver
RUN wget --quiet https://chromedriver.storage.googleapis.com/2.43/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN chmod +x chromedriver
RUN mv -f chromedriver /usr/local/share/chromedriver
RUN ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
RUN ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
