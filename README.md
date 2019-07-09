# MaizeDIG: Maize Database of Images and Genomes #

MaizeDIG allows users to tag phenotypes in images and link them to specific genes.
In this document, we focus on the following topics:

* What is prerequisites to set up MaizeDIG?
* How do I get system set up?
* How do I get MaizeDIG set up?
* Deployment Instruction
* Example of usage.


## What is prerequisites to set up MaizeDIG?

There are some prerequisites to set up MaizeDIG system such as installation 
of Django framework, Database system, Python and related libraries, and other dependencies.
Since MaizeDIG is based on [BioDIG](https://github.com/idoerg/BioDIG), 
most of system set up and configurations are followed by BioDIG.
MaizeDIG requires followings:

* Django framework
* ProgreSQL database
* Python and related libraries
* Apache web server
* Chado database schema

MaizeDIG is web-based system and it uses [Django](https://www.djangoproject.com/) 
framework for web development.
In addition, Django framework based on Python.

## How do I get set up?

The summary of set up as follows and we discuss more details in following sub sections.

* Summary of set up
  1. System set up
      - Install Linux (CentOS 7) and create user account, *'mdig'*
      - Apache Web server set up
      - Firewall set up
      - mod-wsgi set up
  2. Installation of Django framework (1.3.7)
      - create super user for Django
  3. Database set up
      - Install/Configuration PostgreSQL
      - Chado
      - SQLite
  4. Dependencies
      - Sorl-thumnail
      - BioPython
      - GFFParser


### System set up

In this project, we used CentOS 7 and we will use linux commends base on CentOS 7 in this document.
If you are not familiar with any Linux system, then we recommend you to install same version of 
Linux system we use to avoid unexpected issues.
Because the most hardest part in system set up is installation/configuration in Linux system.
However, if you are familiar with different version of Linux rather than CentOS 7 or 
if you already have your own Linux system, you can use it as well.


#### Installation of CentOS 7 and create user account, *'mdig'*
To download CentOS 7, you can use this link [Download CentOS 7](https://www.centos.org/download/).
We skip the details how to install CentOS 7 because it is beyond the scope of this document, 
but you should include at least **Apache web server (Httpd), PostgreSQL database, Python 2.7** 
or above when you install Linux server.
If you are not familiar on installation of Linux, we recommend you to install everything if possible.

Once you have a Linux system, we recommend to create an account for handling maizedig in Linux. 
Following example shows that how to add 'mdig' user account and initialize its password.

    $ sudo adduser mdig
    $ sudo passwd mdig
    Changing password for user mdig.
    New password: ********
    Retype new password: ********
    passwd: all authentication tokens updated successfully.


#### Start Apache Web server (Httpd)

You can start Apache as follows:

    $ sudo systemctl start httpd.service

If you have an issue to start httpd with above commend, you are either case: 
1. Apache web server is not installed on your Linux server, or
2. It is installed but disabled.

If a service is disabled on your machine, you should enable it using ‘systemctl enable’ commend. 
If httpd service is disabled in your system, you should enable httpd.service first 
and then start httpd.service as following:

    $ sudo systemctl enable httpd.service
    $ sudo systemctl start httpd.service



#### Firewall set up

In this section, we will briefly discuss how to allow your web service using firewalld. 
Please note that **‘firewalld’** is used in CentOS 7 as a default firewall instead of ‘iptables’. 
If your system uses 'iptables', please follow 
[How to migrate from FirewallD to Iptables on CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-migrate-from-firewalld-to-iptables-on-centos-7).

Here is an example to allow httpd service using **firewalld**.
First, we can check which services are already allowed on the system:

    $ sudo firewall-cmd --zone=public --list-services --permanent

and we can add new service to allow remote connections for web server as follows:

    $ sudo firewall-cmd --zone=public --permanent --add-service=http

Then, do not forget to restart firewalld.service to apply new changes:

    $ sudo systemctl restart firewalld.service

For more information about FirewallD, please see the article, 
[How to set up a Firewall using FirewallD on CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-firewalld-on-centos-7).


### Installation of Python and Python-devel

If Python is not installed in your system, please see followings:

    $ sudo yum install python
    $ sudo yum install python-devel


### Django Installation

BioDIG was developed based on Django 1.3.7 and we use same version of Django for MaizeDIG.
We can install Django with **pip** as follows:

    $ sudo pip install Django==1.3.7

and then we can verify the installation as belows:

    $ python
    Python 2.7.5 (default, Aug 18 2016, 15:58:25)
    [GCC 4.8.5 20150623 (Red Hat 4.8.5-4)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import django
    >>> print(django.get_version())
    1.3.7

If you see the version of Django as above, Django framework is successfully installed on your system.

#### Start Django project for MaizeDIG

The first thing to do use Django
Now, we need to start MaizeDIG project.
To start Django project, we can use *'django-admin.py'* as below:

    $ cd /var/www
    $ sudo django-admin.py startproject MaizeDIG

Then, MaizeDIG project will be created in *'/var/www/MaizeDIG'* with configuration files.
It will be cloned git repository into the *'/var/www/MaizeDIG'*. 
We will discuss details about this in 'Deployment Instruction' section.


### Database set up

In this section, we discuss database such as installation, initial configuration, 
and how to set up **chado** database schema.


#### Installation of PostgreSQL

MaizeDig uses PostgreSQL 9.5.4 as a main database. 
You may skip this section, if PostgreSQL is installed in your system. 
In addition, if your system has different version of PostgreSQL above 9.4, it's okay to use it.

First, we can install the repository RPM as follows:

    $ sudo yum install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm

Next, install the client packages:

    $ sudo yum install postgresql95

and install the server packages:

    $ sudo yum install postgresql95-server

Now we can install additional packages as follows:

    $ sudo yum install postgresql95-contrib
    $ sudo yum install postgresql95-devel

and we may initialize PostgreSQL database using *postgresql95-setup* as follows:

    $ sudo /usr/pgsql-9.5/bin/postgresql95-setup initdb
    Initializing database ... OK

To enable automatic start PostgreSQL database when your system rebooted:

    $ sudo systemctl enable postgresql-9.5

Finally, we can start PostgreSQL server:

    $ sudo systemctl start postgresql-9.5

We can verify PostgreSQL installation as follows:

    $ sudo su - postgres
    -bash-4.2$ psql
    psql (9.5.4)
    Type "help" for help.
    
    postgres=#

If you can see like above, you have successfully installed PostgreSQL.
For detail information, please see [PostgreSQL: Linux Download](https://www.postgresql.org/download/linux/redhat/) 
page for detail information about download and installation PostgreSQL.


#### Chado

Chado provides a generic database schema for most organism.
For using chado database schema, you can follow steps belows:

##### 1. Create a PostgreSQL user

    $ sudo su - postgres
    -bash-4.2$ createuser [USER_NAME_HERE]
    -bash-4.2$ psql
    psql (9.5.4)
    Type "help" for help.
    
    postgres=# ALTER USER "[USER_NAME_HERE]" WITH PASSWORD '[PASSWORD_HERE]';
    ALTER ROLE
    postgres=# ALTER USER [USER_NAME_HERE] WITH SUPERUSER;
    ALTER ROLE 
    postgres=# CREATE DATABASE [DB_NAME_HERE] OWNER [USER_NAME_HERE];
    CREATE DATABASE


##### 2. *pg_hba.conf*

Now, we need to allow connection to PostgreSQL with editing 
*/var/lib/pgsql/9.5/data/pg_hba.conf* file as belows:

    # TYPE  DATABASE        USER            ADDRESS                 METHOD
    
    # "local" is for Unix domain socket connections only
    #local   all             all                                     peer
    local   all             all                                     trust
    # IPv4 local connections:
    #host    all             all             127.0.0.1/32            ident
    host    all             all             127.0.0.1/32            trust
    # IPv6 local connections:
    #host    all             all             ::1/128                 ident
    host    all             all             ::1/128                 trust

and don't forgot to restart PostgreSQL:

    $ sudo systemctl restart postgresql-9.5.service


##### 3. Download and install Chado

Chado 1.31 used in this project and it can be downloaded from 
[Source Forge](https://sourceforge.net/projects/gmod/files/gmod/). 

First, extract zip file and configuration for installation as belows:

    $ tar xzvf chado-1.31.tar.gz
    $ cd chado-1.31/
    $ export VARNAME=value
    $ perl Makefile.PL GMOD_ROOT=/usr/local/gmod CHADO_DB_NAME=chado
    Use the simple install (uses default database schema, which contains
    all of the modules and extensions to the schema and all of the non-trigger functions.
    This is probably what you want) [Y] y
    What database server will you be using? [PostgreSQL] PostgreSQL
    What is the Chado database name? [chado] maizedig
    What is the database username? [mdig] mdig
    What is the password for 'mdig'? [************] ************
    What is the database host? [localhost] localhost
    What is your database port? [5432] 5432
    What schema will Chado reside in? [public] public
    Where shall downloaded ontologies go? [./tmp] ./tmp
    What is the default organism (common name, or "none")? [] 
    Do you want to make this the default chado instance? [y] y
    
    Building with the following database options:
      GMOD_ROOT=/usr/local/gmod
      DBDRIVER=PostgreSQL
      DBNAME=maizedig
      DBUSER=mdig
      DBPASS=************
      DBHOST=localhost
      DBPORT=5432
      SCHEMA=public
      LOCAL_TMP=./tmp
      DBORGANISM=
      DEFAULT=y
      VERSION=1.31
    ...

Next, we can do the following, in order:

    $ make
    $ sudo make install
    $ make load_schema
    $ make prepdb
    $ make ontologies

Now, we have chado database schema into the PostgreSQL database. 
For detail information for chado installation, please see **INSTALL.Chado** file 
which is included in chado-1.31.tar.gz.


### Other Dependancies

#### mod_wsgi

    $ sudo yum install mod_wsgi


#### psycopg2

    $ sudo pip install psycopg2==2.5

#### pillow

    $ sudo pip install pillow


#### sorl-thumbnail

    $ sudo pip install sorl-thumbnail

#### BioPython

    $ sudo yum install python-biopython

#### GFFParser

    $ sudo pip install bcbio-gff

Verify the installation of GFFParser:

    $ python
    Python 2.7.5 (default, Aug 18 2016, 15:58:25)
    [GCC 4.8.5 20150623 (Red Hat 4.8.5-4)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from BCBio.GFF  import GFFExaminer
    >>> from BCBio import GFF
    >>>

If you see no errors like above, *GFFParser* is installed and works correctly.


## Deployment Instructions

Now, you are all set to deploy MaizeDIG in your machine. 
You can follow steps belows for finishing up of MaizeDIG set up. 


1. Clone git repository into **'/var/www/MaizeDIG/'**
2. Set proper ownership under **'/var/www/MaizeDIG/'**

        $ sudo chown mdig:mdig -R /var/www
   
3. Edit 'settings.py' for your system environment such as database URL or IP address, 
user login credentials, and so on.

4. Create admin user account

        $ cd /var/www/MaizeDIG/
        $ python manager.py createsuperuser --username=mdig
        E-mail address: totaks@gmail.com
        Password: ********
        Password (again): ********
        Superuser created successfully.

5. Web server configurations - VirtualHost and WSGI set up:

        [EDIT] /etc/httpd/conf/httpd.conf
        
        ...
        ##################################################################
        #
        # Virtual Host Settings
        #
        
        #
        # MaizeDIG
        #
        <VirtualHost maizedig.usda.iastate.edu:80>
            ServerName maizedig.maizegdb.org
            DocumentRoot /var/www/MaizeDIG
            ServerAlias maizedig.maizegdb.org
            ServerAdmin totaks@gmail.com
            
            WSGIDaemonProcess maizedig.maizegdb.org user=mdig group=mdig processes=2 threads=25 python-path=/var/www/MaizeDIG:/usr/lib/python2.7/site-packages
            WSGIProcessGroup maizedig.maizegdb.org
            
            WSGIScriptAlias / "/var/www/MaizeDIG/apache/django.wsgi"
            <Directory "/var/www/MaizeDIG">
                Order allow,deny
                Allow from all
            </Directory>

            ErrorLog logs/MaizeDIG-error_log
            CustomLog logs/MaizeDIG-access_log common
        </VirtualHost>
        ...

6. Connect your MaizeDIG main page in web browser.


## FAQ

* Public mode and curator (admin) mode
* curator login (Administration)
* Create Gene Links
    - Add Tag Group
    - Add Tag(s)
    - Create a link between Tag and Gene model
* Image Search
* GBrowse


## Who do I talk to? ###

* Repo admin: Kyoung Tak Cho mailto:totaks@gmail.com
* team contact: MaizeGDB Team

