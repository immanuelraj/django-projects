from python:3.7

RUN apt-get update && apt-get install -y --no-install-recommends \
	git mercurial libpq-dev unzip \
	dpkg-dev libxft-dev libfreetype6-dev libxml2-dev libgeos-dev \
	libgdal-dev libproj-dev libxmlsec1-dev \
	&& rm -rf /var/lib/apt/lists/*

ADD . /django-projects
COPY .netrc /root/.netrc
COPY setup.sh /setup.sh

WORKDIR /django-projects

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt --default-timeout=100
RUN pip install ipython

ENTRYPOINT ["bash", "/setup.sh"]